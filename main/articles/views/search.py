from whoosh.qparser import MultifieldParser
from whoosh import sorting
from django.views.generic import ListView
from django.shortcuts import redirect
import ast

from whoosh.query import And, Term
from whoosh.query import DateRange
from dateutil.parser import parse as parse_date

from django.urls import reverse
from datetime import datetime

from articles.models.article import Article
from articles.models.article_author import ArticleAuthor
from articles.schema import ArticleSchema
from .article_common_contex_mixin import CommonContextMixin


class SearchView(CommonContextMixin, ListView):
    '''
    Pohled pro zpracování dotazu pro vyhledávání v článcích.
    '''

    model = Article
    template_name = '3_articles/30__base__.html'
    paginate_by = 4
    display_text = ""

    def get(self, request, *args, **kwargs):
        '''
        Metoda pro zpracování dotazu pro vyhledávání v článcích.

        Při prvním průchodu metoda předspracuje data a při druhém data předá dál na vyhledávání

        :param request: Objekt HttpRequest, obsahující informace o HTTP požadavku.
        :param args: Pozicí argumenty, které mohou být předány metodě.
        :param kwargs: Klíčové argumenty, které mohou být předány metodě.
        :return: HTTP odpověď s přesměrováním na výsledky vyhledávání nebo výsledek z předchozího volání nadřazené metody.
        '''

        current_url = request.build_absolute_uri()
        print("Current URL:", current_url)

        # Slovník pro jednotlivé položky z dotazu
        search_parameters = {
            'query': self.request.GET.get('q', ''),
            'title': self.request.GET.get('title_checkbox', ''),
            'overview': self.request.GET.get('overview_checkbox', ''),
            'content': self.request.GET.get('content_checkbox', ''),
            'before': self.request.GET.get('before_date', ''),
            'after': self.request.GET.get('after_date', ''),
            'author': self.request.GET.get('author_select', '')
        }

        # Zpětné přeposlání zpracovaného dotazu
        if any(value for value in search_parameters.values()):
            return redirect(reverse('article-search-results', kwargs={'query': search_parameters}))

        # Pokud se jedná o zpětné přeposlání dotazu (má kwargs) pokračuj na vyhledání výsledku
        else:
            return super().get(request, *args, **kwargs)

    def get_queryset(self):
        '''
        Metody pro získání dat z databáze na základě dotazu

        :return: Výsledek pro dané hledání
        '''

        # Vytvoření dotazu pro hledání ve Whoosh
        search_parameters = ast.literal_eval(self.kwargs.get('query'))
        article_schema = ArticleSchema()
        query = self.create_query(search_parameters, article_schema)

        # Vyhledání dotazu Whoosh a získání ID článků
        if query:
            with article_schema.ix.searcher() as searcher:
                results = searcher.search(query, sortedby=sorting.FieldFacet('updated', reverse=True))
                article_ids = [int(hit['id']) for hit in results]

        # Pokud nebyl zadán žádný parametr pro hledání
        else:
            self.display_text = "No search parameters were provided."
            article_ids = []

        # Získání článků z hlavní databáze podle nalezených ID
        queryset = Article.objects.filter(id__in=article_ids)

        return queryset


    def create_query(self, search_parameters, article_schema):
        '''
        Metoda vytváří dotaz pro whoosh index na základě hledaných parametrů a schématu indexu

        :param search_parameters: Hledané výrazy
        :param article_schema: Schema pro Whoosh
        :return: Dotaz pro hledání v indexech Whoosh
        '''

        # Vytvoření dotazu pro hledání dle zadaného slova:
        term_query = None
        if search_parameters['query']:
            therm = search_parameters['query']
            search_fields = [i for i in ('title', 'overview', 'content') if search_parameters[i]]
            term_query = MultifieldParser(search_fields,
                                          schema=article_schema.get_schema()).parse(therm)

            # Vytvoření popisného textu pro výsledek hledání
            self.display_text = f"with the therm {therm}"
            if len(search_fields) == 1:
                self.display_text += f" in {search_fields[0]}"
            elif len(search_fields) == 2:
                self.display_text += f" in {search_fields[0]} and {search_fields[1]}"
            self.display_text += "<br>"

        # Vytvoření dotazu pro hledání dle data:
        date_query = None
        if search_parameters['before'] or search_parameters['after']:
            before_date = parse_date(search_parameters['before']) if search_parameters['before'] else None
            after_date = parse_date(search_parameters['after']) if search_parameters['after'] else None
            date_query = DateRange("updated", before_date, after_date, startexcl=False, endexcl=False)

            def format_date(date):
                '''
                Metoda pro změnu formátu datumu

                :param date: Datum z formuláře (%Y-%m-%d)
                :return: Upravené datum (%d. %m. %Y)
                '''
                input_date = datetime.strptime(date, "%Y-%m-%d")
                return input_date.strftime("%d. %m. %Y")

            # Vytvoření popisného textu pro výsledek hledání
            if before_date:
                self.display_text += f"published before {format_date(search_parameters['before'])}"
                if after_date:
                    self.display_text += f" and after {format_date(search_parameters['after'])}"
            elif after_date:
                self.display_text += f"published after {format_date(search_parameters['after'])}"
            self.display_text += "<br>"




        # Vytvoření dotazu pro hledání dle autora:
        author_query = None
        if search_parameters['author']:
            author_name = ArticleAuthor.objects.get(id=search_parameters['author']).author
            author_query = Term('author', author_name.lower())

            # Vytvoření popisného textu pro výsledek hledání
            self.display_text += f"written by the author {author_name}"


        # Vytvoření dotazu ze seznamu zadaných podmínek
        query = None
        queries = [i for i in (term_query, date_query, author_query) if i]
        if queries:
            query = queries[0] if len(queries) == 1 else And(queries)

        return query


    def get_context_data(self, **kwargs):
        '''
        Metoda pro vložení kontextu

        :return: Kontext s vloženými daty
        '''

        # Získání běžného kontextu a přidání vyhledávacího dotazu
        context = super().get_context_data(**kwargs)

        # Přidání výsledku dotazu
        context['query'] = self.kwargs.get('query') or self.request.GET.get('q')
        print(repr(self.display_text))
        context['display_text'] = self.display_text

        # Navrácení kontextu
        return context
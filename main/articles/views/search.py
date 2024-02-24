### Definice třídy pohledu pro hledání v článcích

from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
import ast
from functools import reduce
from operator import or_
from articles.models.article import Article

from .article_common_contex_mixin import CommonContextMixin


class SearchView(CommonContextMixin, ListView):
    '''
    Pohled pro vyhledávání článků
    '''

    # Použitý model pro zobrazení výsledků vyhledávání
    model = Article

    # Cesta k šabloně pro zobrazení výsledků vyhledávání
    template_name = '3_articles/30__base__.html'

    # Počet výsledků na stránku
    paginate_by = 4

    def get(self, request, *args, **kwargs):
        '''
        Metoda pro zpracování dotazu ze stránky.

        Metoda zjistí, zda se jedná o požadavek zadaný do vyhledávacího pole a nebo již touto metodou předspracovaný
        '''

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

        # Pokud se jedná o zpětné přeposlání dotazu (má kwargs) posuň dotaz dál
        else:
            return super().get(request, *args, **kwargs)

    def get_queryset(self):
        '''
        Metoda pro získání dotazu pro databázi

        :return:
        '''

        # Získání hodnoty kwargs a převod na slovník
        search_parameters = ast.literal_eval(self.kwargs.get('query'))

        # Kontrola zda slovník obsahuje i hodnoty
        if any(value for value in search_parameters.values()):

            # Základ dotazu pro získání všech článků
            queryset = Article.objects.all()

            # Přidání filtrace dle autora
            if search_parameters['author']:
                queryset = queryset.filter(author=search_parameters['author'])

            # Přidání filtrace dle data před
            if search_parameters['before']:
                queryset = queryset.filter(created__lte=search_parameters['before'])

            # Přidání filtrace dle data po
            if search_parameters['after']:
                queryset = queryset.filter(created__gte=search_parameters['after'])

            # Přidání filtrace podle pole pro dotaz
            if search_parameters['query']:
                fields = []

                # Když je zaškrtlé pole pro nadpis
                if search_parameters['title']:
                    fields.append('title')

                # Když je zaškrtlé pole pro přehled
                if search_parameters['overview']:
                    fields.append('overview')

                # Když je zaškrtlé pole pro obsah
                if search_parameters['content']:
                    fields.append('content')

                # Vytvoření společného filtru
                queryset = queryset.filter(
                    reduce(or_, (Q(**{f"{field}__icontains": search_parameters['query']}) for field in fields))
                )

            # Navrácení dotazu
            return queryset.distinct().order_by('-created')

        # V případě, že slovník neobsahuje i hodnoty, vrátit prázdnou množinu
        else:
            return Article.objects.none()

    # Přidání kontext dat
    def get_context_data(self, **kwargs):
        '''
        Metoda pro vložení kontextu

        :return:
        '''

        # Získání běžného kontextu a přidání vyhledávacího dotazu
        context = super().get_context_data(**kwargs)

        # Přidání výsledku dotazu
        context['query'] = self.kwargs.get('query') or self.request.GET.get('q')

        # Navrácení kontextu
        return context


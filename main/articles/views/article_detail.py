from django.views.generic import DetailView
from django.shortcuts import redirect, reverse

from common_data.base_view import BaseView

from ..models.article import Article
from ..models.article_view import ArticleView
from ..forms.comment_form import ArticleCommentForm


class ArticleDetailView(BaseView, DetailView):
    '''
    Pohled pro stránku s výpisem jednoho článku.

    Tento pohled zpracovává následující URL adresu:
    - article-detail: Stránka zobrazující jeden vybraný článek.

    Pohled dědí od základní třídy DetailView a vlastní třídy BaseView.

    Atributy přetížené z ListView:
    - self.template_name: Určuje cestu k šabloně, která bude použita pro zobrazení výsledků.
    - self.context_object_name: Název proměnné v kontextu šablony, která bude obsahovat výsledný seznam objektů.

    Atributy zděděné z BaseView:
    - self.user: Instance uživatele (buď CustomUser, nebo AnonymousUserWithSettings).
    - self.url_name: URL jméno adresy, ze které přišel požadavek.

    Metody definované v tomto pohledu:
    - get_object: Metoda pro získání objektu (instance článku) a zaznamenání jeho zhlédnutí.
    - handle_comment_form: Metoda pro zpracování formuláře pro komentář k článku.
    - get_context_data: Metoda, která vrací obsah pro vykreslení šablony.
    '''
    model = Article
    template_name = '4_article/40__base__.html'
    context_object_name = 'article'

    def get_object(self):
        '''
        Metoda pro získání objektu (instance článku) a zaznamenání jeho zhlédnutí.

        Nejprve získává instanci článku z nadřazené třídy.
        Poté volá metodu record_view třídy ArticleView pro zaznamenání zhlédnutí.
        Kromě instance článku a autora předává i IP adresu získanou ze slovníku 'META'.
        Metoda navrací instanci článku.
        '''
        obj = super().get_object()
        ArticleView.record_view(obj, self.request.user, self.request.META.get('REMOTE_ADDR'))
        return obj

    def handle_comment_form(self, request, *args, **kwargs):
        '''
        Metoda pro zpracování formuláře pro komentář k článku.

        Nejprve načte formulář pro komentáře k článku a pokud jsou data validní,
        přidává k formuláři instanci uživatele a instanci článku a ukládá data do databáze.
        Po úspěšném uložení komentáře přesměruje uživatele na stránku s článkem.
        '''
        form = ArticleCommentForm(request.POST)

        if form.is_valid():
            article = self.get_object()
            form.instance.user = request.user
            form.instance.article = article
            form.save()

            return redirect(reverse("article-detail", kwargs={'slug': article.slug}))

    def get_context_data(self, **kwargs):
        '''
        Metoda pro předání kontextu potřebného pro vykreslení stránky.

        Kontext zděděný z BaseView:
        - context['user']: Instance uživatele.
        - context['url_name']: URL jménu adresy z které požadavek přišel.
        - context['sidebar_search_form']: Formulář pro hledání (pro postranní panel).
        - context['published_categories']: Publikované kategorie (pro dropdown menu a postranní panel).
        - context['footer']: Data pro vykreslení patičky (na domácí stránce je již zahrnuto)
        - context['user_thumbnail']: Miniatura profilového obrázku (pro přihlášeného a nepřihlášeného uživatele).

        Kontext vytvořený tímto pohledem:
        - context['form']: Formulář pro zanechání komentáře k článku.
        '''
        context = super().get_context_data(**kwargs)

        context['form'] = ArticleCommentForm()
        return context

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.urls import reverse

from .article_create import ArticleCreateView


@method_decorator(login_required, name='dispatch')
class ArticleUpdateView(ArticleCreateView, UpdateView):
    '''
    Pohled pro úpravu vytvořeného článku (jen pro přihlášené uživatele).

    Pohled zpracovává následující URL:
    - article-update: Stránka pro úpravu vytvořeného článku.

    Pohled dědí ze základní třídy UpdateView a vlastní třídy pro vytvoření článku ArticleCreateView.

    Atributy poděděné z ArticleCreateView:
    - self.model: Určuje model, se kterým tento pohled pracuje.
    - self.template_name: Určuje cestu k šabloně, která bude použita pro zobrazení výsledků.
    - self.user: Instance uživatele (buď CustomUser, nebo AnonymousUserWithSettings).
    - self.url_name: URL jméno adresy, ze které požadavek přišel.

    Metody poděděné z ArticleCreateView:
    - get_form_class: Metoda, která vrací formulář na základě zvolené záložky stránky.
    - form_valid: Metoda, která do formuláře přidává informace o autorovi (instanci autora).
    - get_success_url: Metoda, která vytváří adresu pro přesměrování po úspěšném založení článku.

    Metody přetížené z ArticleCreateView:
    - get_context_data: Metoda, která vytváří obsah pro vykreslení šablony.
    '''

    def get_context_data(self, **kwargs):
        '''
        Metoda pro vytvoření kontextu.

        Kontext poděděný z ArticleCreateView:
        - context['user']: Instance uživatele.
        - context['url_name']: URL jménu adresy z které požadavek přišel.
        - context['sidebar_search_form']: Formulář pro hledání (pro postranní panel).
        - context['published_categories']: Publikované kategorie (pro dropdown menu a postranní panel).
        - context['footer']: Data pro vykreslení patičky (na domácí stránce je již zahrnuto)
        - context['user_thumbnail']: Miniatura profilového obrázku (pro přihlášeného a nepřihlášeného uživatele).

        Kontext vytvořený tímto pohledem:
        - context['tab_urls']: Reverzní cesty na jednotlivé záložky.
        - context['current_tab']: Aktuální záložka stránky.
        - context['title']: Název stránky.
        '''

        # Vytvoření URL adres pro jednotlivé záložky stránky
        tab_urls = {
            'for_overview': reverse('article-update', kwargs={'slug': self.object.slug, 'current_tab': 'overview'}),
            'for_content': reverse('article-update', kwargs={'slug': self.object.slug, 'current_tab': 'content'}),
            'for_settings': reverse('article-update', kwargs={'slug': self.object.slug, 'current_tab': 'settings'}),
        }

        context = super().get_context_data(**kwargs)
        context['tab_urls'] = tab_urls
        context['title'] = 'Update Your Article'

        return context

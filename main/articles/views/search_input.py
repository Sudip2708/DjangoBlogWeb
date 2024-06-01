from django.views.generic import TemplateView

from common_data.base_view import BaseView

from ..forms.search_form import ArticleSearchForm


class SearchInputView(BaseView, TemplateView):
    '''
    Pohled pro zobrazení stránky pro vyhledávání (a pro oznam chyb ve vyhledávání)

    Pohled zpracovává následující URL:
    - article-search-input: Stránka pro zadání vyhledávání.
    - article-search-error: Stránka pro oznámení chyb vyhledávání.

    Atributy přetížené z TemplateView:
    - template_name: Určuje cestu k šabloně, která bude použita pro zobrazení výsledků.

    Pohled dědí ze základní třídy TemplateView a vlastní třídy BaseView
    a následně vytváří obsah pro vykreslení stránky pro hledání
    a pro vykreslení stránky oznamující chybu v zadání vyhledávání.
    '''

    template_name = '2_main/22__search__.html'

    def get_context_data(self, **kwargs):
        '''
        Metoda pro předání kontextu potřebného pro vykreslení stránky.

        Metoda dědí z třídy BaseView následující obsah:
        - context['user']: Instance uživatele.
        - context['url_name']: URL jménu adresy z které požadavek přišel.
        - context['sidebar_search_form']: Formulář pro hledání (pro postranní panel).
        - context['published_categories']: Publikované kategorie (pro dropdown menu a postranní panel).
        - context['footer']: Data pro vykreslení patičky (na domácí stránce je již zahrnuto)
        - context['user_thumbnail']: Miniatura profilového obrázku (pro přihlášeného a nepřihlášeného uživatele).

        Metoda přepsuje tento obsah (pouze v případě chyby):
        - context['sidebar_search_form']:  Formulář pro hledání (pro postranní panel).

        Metoda přidává tento obsah:
        - context['page_title']: Nadpis stránky.
        - context['search_form']: Formulář pro hledání na stránce

        Metoda nejprve načte kontext nadřazené třídy
        a po té zkontroluje, zda požadavek přišel ze stránky pro vyhledávání,
        pokud ano, vytvoří pro ní nadpis a prázdný formulář.

        Následně metoda zkontroluje zda přišel požadavek ze stránbky pro oznam chyb,
        pokud ano, získá přeposlaná data a následně z nich vytáhne
        formulář s oznamem o chybě a předvyplněnými daty.
        Ten pak předá jako kontext pro vykreslení vlastního formuláře
        a zároveň s ním i přepíše formulář obdržený z BaseView,
        určený pro hledání z postranního panelu.
        A následně vytvoří a přidá nadpis.

        Metoda vrací obsah potřebný pro vykreslení stránky
        '''
        context = super().get_context_data(**kwargs)

        # Kontex pro stránku vyhledávání
        if self.url_name == 'article-search-input':
            context['page_title'] = 'Search in Articles'
            context['search_form'] = ArticleSearchForm()

        # Kontex pro stránku s výpisem chyb
        elif self.url_name == 'article-search-error':
            error_data = self.request.session.pop('search_error_data', None)
            if error_data:
                form_data = error_data['form_data']
                form = ArticleSearchForm(form_data)
                context['sidebar_search_form'] = form
                context['search_form'] = form
            context['page_title'] = 'Search in Articles - Error'

        return context

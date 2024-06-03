from django.views.generic import ListView
from django.shortcuts import redirect
from django.urls import reverse

from common_data.base_view import BaseView

from ..forms.search_form import ArticleSearchForm
from .common_data.get_paginate_by import get_paginate_by
from .search_data.get_search_parameters import get_search_parameters
from .search_data.get_queryset import get_queryset
from .search_data.get_context_data import get_context_data


class SearchView(BaseView, ListView):
    '''
    Pohled pro zpracování vyhledávání v článcích.

    Pohled zpracovává následující URL:
    - article-search: Základní adresa sloužící k zadání a vyhodnocení parametrů hledání.
    - article-search-results: Stránka pro zobrazení výsledků vyhledávání.
    - article-search-similar: Stránka pro zobrazení podobných článků pro články z výsledku vyhledávání.
    - article-search-results-category: Stránka pro zobrazení kategorií pro vásledek vyhledávání.
    - article-search-similar-category: Stránka pro zobrazení kategorií pro podobné články.

    Pohled dědí ze základní třídy ListView a vlastní třídy BaseView.

    Atributy přetížené z ListView:
    - template_name: Určuje cestu k šabloně, která bude použita pro zobrazení výsledků.
    - context_object_name: Název proměnné v kontextu šablony, která bude obsahovat výsledný seznam objektů.

    Atributy poděděné z BaseView:
    - self.user: Instance uživatele (buď CustomUser, nebo AnonymousUserWithSettings).
    - self.url_name: URL jménu adresy z které požadavek přišel.

    Atributy definované tímto pohledem:
    - self.search_parameters: Atribut obsahující slovník s parametry dotazu
    - self.article_ids: Atribut pro ID článku na základě hledaných dat.
    - self.page_title: Atribut pro nadpis stránky
    - self.page_title_mobile: Atribut pro nadpis stránky pro mobilní zařízení.
    - self.display_text: Atribut pro popisný text, informující o tom, co bylo hledáno.
    - self.info_text: Informační text (zobrazí se, když není nalezen žádný podobný článek).
    - self.category_items: Atribut pro výčet kategorií pro výsledek hledání.
    - self.current_category_tab: Atribut pro aktuálně vybranou záložku kategorie.

    Metody definované v tomto pohledu:
    - get: Metoda pro získání dat formuláře pro vykreslení stránky.
    - get_queryset: Metoda slouží k získání instancí článků a dat potřebných pro vykreslení stránky.
    - get_paginate_by: Metoda pro určení počtu článků na stránce při stránkování výsledků vyhledávání.
    - get_context_data: Metoda pro předání kontextu potřebného pro vykreslení stránky.
    '''

    template_name = '3_articles/30__base__.html'
    context_object_name = 'articles_results'

    def get(self, request, *args, **kwargs):
        '''
        Metoda pro zpracování příchozího požadavku.

        Metoda nejprve ověří dle jména URL, zda jde o požadavek ze stránky article-search,
        sloužící k zadání a vyhodnocení parametrů hledání.

        Pokud ano, načte instanci formuláře a provede kontrolu zadaných dat.
        Pokud jsou data v pořádky volá funkci pro vytvoření slovníku s parametry pro hledání,
        a přepošle tento slovník na adrsu article-search-results,
        pro získání dat potřebných pro zobrazení výsledků hledání.

        Pokud data nejsou validní volá stránku pro zobrazení chyb v zadání.

        Pokud metoda get obdrží již předpřipravená data, volá metodu get nadřazené třídy
        a předává data na další zpracování.
        '''

        # Zachycení dotazu od uživatele
        if self.url_name == 'article-search':

            form = ArticleSearchForm(request.GET)
            if form.is_valid():

                # Vytvoření slovníků s parametry pro hledání a přeposlání zpracovaných dat
                search_parameters = get_search_parameters(form.cleaned_data)
                return redirect(reverse('article-search-results',kwargs={'query': search_parameters}))

            else:

                # Přeposlání formuláře na stránku pro zobrazení chyby
                request.session['search_error_data'] = {'form_data': form.data,}
                return redirect(reverse('article-search-error'))

        else:

            # Pokud se jedná přeposlání zpracovaných dat, je volána metoda get nadřazené třídy
            return super().get(request, *args, **kwargs)

    def get_queryset(self):
        '''
        Metoda slouží k získání instancí článků a dat potřebných pro vykreslení stránky.

        Metoda volá stejnojmenou metodu uloženou v samostatném souboru
        a vrací její výsledek.
        '''
        return get_queryset(self)

    def get_paginate_by(self, queryset):
        '''
        Metoda pro určení počtu článků na stránce při stránkování výsledků vyhledávání.

        Metoda volá stejnojmenou metodu uloženou v samostatném souboru
        a vrací její výsledek.
        '''
        return get_paginate_by(self, queryset)

    def get_context_data(self, **kwargs):
        '''
        Metoda pro předání kontextu potřebného pro vykreslení stránky.

        Metoda nejprve načte kontext nadřazené třídy,
        a po té volá stejnojmenou metodu uloženou v samostatném souboru,
        které kontext předá a následně vrací její výsledek.
        '''
        context = super().get_context_data(**kwargs)
        return get_context_data(self, context, **kwargs)

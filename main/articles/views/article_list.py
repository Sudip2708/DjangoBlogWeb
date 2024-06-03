from django.views.generic import ListView

from common_data.base_view import BaseView

from .common_data.get_paginate_by import get_paginate_by
from .article_list_data.get_queryset import get_queryset
from .article_list_data.get_context_data import get_context_data


class ArticleListView(BaseView, ListView):
    '''
    Pohled pro stránku s výpisem článků.

    Pohled zpracovává následující URL:
    - article-list: Stránka zobrazující všechny publikované články.
    - article-category-list: Stránka zobrazující všechny publikované články roztříděné do kategorií.
    - article-tag-list: Stránka pro zobrazení článků pro daný tag.
    - article-tag-list-similar: Stránka pro zobrazení podobných článků pro daný tag.
    - article-tag-list-category: Stránka pro zobrazení kategorií pro články pro daný tag.
    - article-tag-list-similar-category: Stránka pro zobrazení kategorií pro podobné články pro daný tag.

    Pohled dědí ze základní třídy ListView a vlastní třídy BaseView.

    Atributy přetížené z ListView:
    - self.template_name: Určuje cestu k šabloně, která bude použita pro zobrazení výsledků.
    - self.context_object_name: Název proměnné v kontextu šablony, která bude obsahovat výsledný seznam objektů.

    Atributy poděděné z BaseView:
    - self.user: Instance uživatele (buď CustomUser, nebo AnonymousUserWithSettings).
    - self.url_name: URL jménu adresy z které požadavek přišel.

    Atributy definované tímto pohledem:
    - self.page_title: Název stránky.
    - self.page_title_mobile: Atribut pro nadpis stránky pro mobilní zařízení.
    - self.page_subtitle: Podnázev stránky (zobrazí se, když je navigace pro kategorie skrytá).
    - self.info_text: Informační text (zobrazí se, když není nalezen žádný podobný článek).
    - self.current_category: Instance aktuálně vybrané kategorie (pouze pro kategorie).
    - self.category_tabs = Seznam kategorií pro obsah self.article_ids (pouze pro kategorie).

    Metody definované v tomto pohledu:
    - get_queryset: Metoda slouží k získání instancí článků a dat potřebných pro vykreslení stránky.
    - get_paginate_by: Metoda pro určení počtu článků na stránce při stránkování výsledků vyhledávání.
    - get_context_data: Metoda pro předání kontextu potřebného pro vykreslení stránky.
    '''

    template_name = '3_articles/30__base__.html'
    context_object_name = 'articles_results'

    def get_queryset(self, *args, **kwargs):
        '''
        Metoda slouží k získání instancí článků a dat potřebných pro vykreslení stránky.

        Metoda volá stejnojmenou metodu uloženou v samostatném souboru
        a vrací její výsledek.
        '''
        return get_queryset(self, *args, **kwargs)

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
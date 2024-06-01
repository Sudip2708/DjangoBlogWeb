from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from common_data.base_view import BaseView

from .common_data.get_paginate_by import get_paginate_by
from .my_articles_data.get_queryset import get_queryset
from .my_articles_data.get_context_data import get_context_data


@method_decorator(login_required, name='dispatch')
class MyArticlesView(BaseView, ListView):
    '''
    Pohled pro stránku s vlastními články uživatele (jen pro přihlášené uživatele).

    Pohled zpracovává následující URL:
    - my-articles: Stránka pro články od autora navázaného na uživatele.

    Stránka má následující záložky:
    - all: Všechny články řazené dle data vytvoření sestupně.
    - drafted: Rozepsané články.
    - publish: Publikované články (články pro veřejnost).
    - archive: Archivované články.

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
    - self.current_tab: Atribut pro název aktuálně zobrazené záložky.

    Metody definované v tomto pohledu:
    - get_queryset: Metoda slouží k získání instancí článků a dat potřebných pro vykreslení stránky.
    - get_paginate_by: Metoda pro určení počtu článků na stránce při stránkování výsledků vyhledávání.
    - get_context_data: Metoda pro předání kontextu potřebného pro vykreslení stránky.
    '''

    template_name = '3_articles/30__base__.html'
    context_object_name = 'articles_results'

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

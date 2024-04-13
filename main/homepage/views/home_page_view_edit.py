from django.shortcuts import render
from django.views.generic import View

from .home_page_mixins import HomePageEditViewMixin
from .home_page_mixins import HomePageViewMixin

class HomePageEditView(View, HomePageEditViewMixin, HomePageViewMixin):
    '''
    Třída pro úpravu obsahu domovské stránky.

    Tato třída zahrnuje zobrazení domovské stránky a také umožňuje úpravu obsahu
    prostřednictvím příslušných formulářů.
    '''

    def get(self, request, *args, **kwargs):
        '''
        Metoda pro zobrazení domovské stránky nebo stránky pro úpravu obsahu domovské stránky.

        :param request: HttpRequest
        :param args: Pozicinální argumenty
        :param kwargs: Klíčové argumenty
        :return: HttpResponse
        '''

        # Načtení kontextu pro zobrazení domovské stránky
        context = self.get_home_page_data()

        # Přidání formulářů pro editaci obsahu
        self.add_edit_forms_to_context(context)

        # Navrácení stránky
        return render(request, '1_home/10__base__.html', context)

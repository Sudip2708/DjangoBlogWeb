from django.shortcuts import render
from django.views.generic import View

from .home_page_mixins import HomePageViewMixin


class HomePageView(View, HomePageViewMixin):
    '''
    Třída pro zobrazení obsahu domovské stránky.
    '''

    def get(self, request, *args, **kwargs):
        '''
        Metoda pro zobrazení domovské stránky.

        :param request: HttpRequest
        :param args: Pozicinální argumenty
        :param kwargs: Klíčové argumenty
        :return: HttpResponse
        '''

        # Načtení kontextu pro zobrazení domovské stránky
        context = self.get_home_page_data()

        # Navrácení stránky
        return render(request, '1_home/10__base__.html', context)



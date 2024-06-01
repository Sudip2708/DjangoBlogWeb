from django.urls import path

from ..views.home_page_view import HomePageView


# Definování adres začínajících s prefixem '' (zobrazení domácí stránky)
urlpatterns = [

    # Zobrazení domácí stránky
    path('', HomePageView.as_view(), name='home-page'),

]













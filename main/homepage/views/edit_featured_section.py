from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages

from ..forms.featured_section_form import FeaturedArticlesForm
from ..models.featured_section import HomePageFeaturedArticles


class EditFeaturedArticlesSection(View):
    '''
    Pohled pro zpracování dat formuláře pro sekci označených článků na Home Page

    Tato třída postupuje následovně:
    Po obdržení POST požadavku na zpracování dat z formuláře vytvoří instanci formuláře FeaturedArticlesForm.
    Ověří, zda je formulář platný. Pokud ano, pokračuje.
    Získává nebo vytváří instanci modelu HomePageFeaturedArticles.
    Nastavuje hodnoty z formuláře do příslušných polí instance modelu.
    Uložení změn do databáze voláním metody save() na instanci modelu.
    Nakonec provede přesměrování na stránku home-page-edit.
    '''

    def post(self, request, *args, **kwargs):
        '''
        Zpracování HTTP POST požadavku.

        Tato metoda zpracovává odeslaný formulář pro úpravu HomePageFeaturedArticles na domovské stránce.
        Pokud je formulář validní, aktualizuje hodnoty v databázi
        a přesměruje uživatele na stránku pro úpravu domovské stránky.
        Pokud formulář není validní, zobrazí chybovou zprávu
        a přesměruje uživatele zpět na stránku pro úpravu s neuloženými změnami.
        '''

        # Načtení formuláře
        form = FeaturedArticlesForm(request.POST)

        # Kontrola, zda je formulář validní
        if form.is_valid():

            # Získání nebo vytvoření instance modelu HomePageFeaturedArticles
            featured_articles = HomePageFeaturedArticles.singleton()

            # Nastavení hodnot z formuláře do instance modelu
            featured_articles.featured_article_1 = form.cleaned_data['featured_article_1']
            featured_articles.featured_article_2 = form.cleaned_data['featured_article_2']
            featured_articles.featured_article_3 = form.cleaned_data['featured_article_3']
            featured_articles.display_featured_section = form.cleaned_data['display_featured_section']

            # Uložení změn do databáze a přesměrování na stránku home-page-edit
            featured_articles.save()
            return redirect('home-page-edit')

        # Pokud formulář validní není
        else:
            # Navrácení na stránku úprav a zobrazení zprávu o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('home-page-edit')

    def get(self, request, *args, **kwargs):
        '''
        Zpracování HTTP GET požadavku.

        Tato metoda kontroluje, zda požadavek GET obsahuje parametr 'show_featured_section'.
        Pokud ano, nastaví hodnotu pro zobrazení sekce patičky na True a provede přesměrování
        na stránku pro úpravu domovské stránky. Jinak pokračuje v běžném chování.
        '''

        # Kontrola zda požadavek get v sobě obsahuje pořadavek na zviditelnění sekce
        if 'show_featured_section' in request.GET:

            # Pokud ano - změna hodnoty a návrat na stránku pro úpravu HomePage
            featured_articles = HomePageFeaturedArticles.singleton()
            featured_articles.display_featured_section = True
            featured_articles.save()
            return redirect('home-page-edit')

        # Pokud ne, pokračuj normálně
        else:
            return super().get(request, *args, **kwargs)
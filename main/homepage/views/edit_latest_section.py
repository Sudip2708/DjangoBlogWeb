from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages

from ..forms.latest_section_form import LatestArticlesForm
from ..models.latest_section import HomePageLatestArticles


class EditLatestArticlesSection(View):
    '''
    Pohled pro zpracování dat formuláře pro sekci nejnovějších článků na Home Page

    Tato třída postupuje následovně:
    Po obdržení POST požadavku na zpracování dat z formuláře vytvoří instanci formuláře LatestArticlesForm.
    Ověří, zda je formulář platný. Pokud ano, pokračuje.
    Získává nebo vytváří instanci modelu HomePageLatestArticles.
    Nastavuje hodnoty z formuláře do příslušných polí instance modelu.
    Uložení změn do databáze voláním metody save() na instanci modelu.
    Nakonec provede přesměrování na stránku home-page-edit.
    '''

    def post(self, request, *args, **kwargs):
        '''
        Zpracování HTTP POST požadavku.

        Tato metoda zpracovává odeslaný formulář pro úpravu HomePageLatestArticles na domovské stránce.
        Pokud je formulář validní, aktualizuje hodnoty v databázi
        a přesměruje uživatele na stránku pro úpravu domovské stránky.
        Pokud formulář není validní, zobrazí chybovou zprávu
        a přesměruje uživatele zpět na stránku pro úpravu s neuloženými změnami.
        '''

        # Načtení formuláře
        form = LatestArticlesForm(request.POST)

        # Kontrola, zda je formulář validní
        if form.is_valid():

            # Získání nebo vytvoření instance modelu HomePageLatestArticles
            latest_articles_section, _ = HomePageLatestArticles.objects.get_or_create(pk=1)

            # Nastavení hodnot z formuláře do instance modelu
            latest_articles_section.latest_title = form.cleaned_data['latest_title']
            latest_articles_section.latest_description = form.cleaned_data['latest_description']
            latest_articles_section.latest_article_1 = form.cleaned_data['latest_article_1']
            latest_articles_section.latest_article_2 = form.cleaned_data['latest_article_2']
            latest_articles_section.latest_article_3 = form.cleaned_data['latest_article_3']
            latest_articles_section.display_latest_section = form.cleaned_data['display_latest_section']

            # Uložení změn do databáze a přesměrování na stránku home-page-edit
            latest_articles_section.save()
            return redirect('home-page-edit')

        # Pokud formulář validní není
        else:
            # Navrácení na stránku úprav a zobrazení zprávy o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('home-page-edit')

    def get(self, request, *args, **kwargs):
        '''
        Zpracování HTTP GET požadavku.

        Tato metoda kontroluje, zda požadavek GET obsahuje parametr 'show_latest_section'.
        Pokud ano, nastaví hodnotu pro zobrazení sekce patičky na True a provede přesměrování
        na stránku pro úpravu domovské stránky. Jinak pokračuje v běžném chování.
        '''

        # Kontrola zda požadavek get v sobě obsahuje požadavek na zviditelnění sekce
        if 'show_latest_section' in request.GET:

            # Pokud ano - změna hodnoty a návrat na stránku pro úpravu HomePage
            latest_articles_section, _ = HomePageLatestArticles.objects.get_or_create(pk=1)
            latest_articles_section.display_latest_section = True
            latest_articles_section.save()
            return redirect('home-page-edit')

        # Pokud ne, pokračuj normálně
        else:
            return super().get(request, *args, **kwargs)

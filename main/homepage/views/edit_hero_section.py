from django.shortcuts import redirect
from django.views.generic import View
from homepage.forms.hero_section_form import HeroSectionForm
from homepage.models.hero_section import HomePageHeroSection
from django.contrib import messages


class EditHeroSection(View):
    '''
    Třída pro zpracování dat formuláře pro Hero sekci z Home Page

    Tato třída postupuje následovně:
    Po obdržení POST požadavku na zpracování dat z formuláře vytvoří instanci formuláře HeroSectionForm.
    Ověří, zda je formulář platný. Pokud ano, pokračuje.
    Získává nebo vytváří instanci modelu HomePageHeroSection.
    Nastavuje hodnoty z formuláře do příslušných polí instance modelu.
    Uložení změn do databáze voláním metody save() na instanci modelu.
    Nakonec provede přesměrování na stránku home-page-edit.
    '''

    def post(self, request, *args, **kwargs):
        '''
        Zpracování HTTP POST požadavku.

        Tato metoda zpracovává odeslaný formulář pro úpravu HomePageHeroSection na domovské stránce.
        Pokud je formulář validní, aktualizuje hodnoty v databázi
        a přesměruje uživatele na stránku pro úpravu domovské stránky.
        Pokud formulář není validní, zobrazí chybovou zprávu
        a přesměruje uživatele zpět na stránku pro úpravu s neuloženými změnami.

        :param request: Objekt HttpRequest obsahující data zaslaná klientem.
        :param args: Další pozicinální argumenty.
        :param kwargs: Další klíčové argumenty.
        :return: HttpResponse objekt reprezentující odpověď serveru na požadavek.
        '''

        # Načtení formuláře
        form = HeroSectionForm(request.POST, request.FILES)

        # Kontrola, zda je formulář validní
        if form.is_valid():

            # Získání nebo vytvoření instance modelu HomePageHeroSection
            hero_section = HomePageHeroSection.singleton()

            # Nastavení hodnot z formuláře do instance modelu
            hero_section.hero_image = form.cleaned_data['hero_image']
            hero_section.hero_title = form.cleaned_data['hero_title']
            hero_section.hero_link_title = form.cleaned_data['hero_link_title']
            hero_section.hero_link = form.cleaned_data['hero_link']
            hero_section.display_hero_section = form.cleaned_data['display_hero_section']

            # Uložení změn do databáze a přesměrování na stránku home-page-edit
            hero_section.save()
            return redirect('home-page-edit')

        # Pokud formulář validní není
        else:
            # Navrácení na stránku úprav a zobrazení zprávu o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('home-page-edit')

    def get(self, request, *args, **kwargs):
        '''
        Zpracování HTTP GET požadavku.

        Tato metoda kontroluje, zda požadavek GET obsahuje parametr 'show_hero_section'.
        Pokud ano, nastaví hodnotu pro zobrazení sekce patičky na True a provede přesměrování
        na stránku pro úpravu domovské stránky. Jinak pokračuje v běžném chování.

        :param request: Objekt HttpRequest obsahující data zaslaná klientem.
        :param args: Další pozicinální argumenty.
        :param kwargs: Další klíčové argumenty.
        :return: HttpResponse objekt reprezentující odpověď serveru na požadavek.
        '''

        # Kontrola zda požadavek get v sobě obsahuje pořadavek na zviditelnění sekce
        if 'show_hero_section' in request.GET:

            # Pokud ano - změna hodnoty a návrat na stránku pro úpravu HomePage
            hero_section = HomePageHeroSection.singleton()
            hero_section.display_hero_section = True
            hero_section.save()
            return redirect('home-page-edit')

        # Pokud ne, pokračuj normálně
        else:
            return super().get(request, *args, **kwargs)

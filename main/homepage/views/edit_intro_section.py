from django.shortcuts import redirect
from django.views.generic import View
from homepage.forms.intro_section_form import IntroSectionForm
from homepage.models.intro_section import HomePageIntroSection
from django.contrib import messages


class EditIntroSection(View):
    '''
    Třída pro zpracování dat formuláře pro úvodní sekci na Home Page

    Tato třída postupuje následovně:
    Po obdržení POST požadavku na zpracování dat z formuláře vytvoří instanci formuláře IntroSectionForm.
    Ověří, zda je formulář platný. Pokud ano, pokračuje.
    Získává nebo vytváří instanci modelu HomePageIntroSection.
    Nastavuje hodnoty z formuláře do příslušných polí instance modelu.
    Uložení změn do databáze voláním metody save() na instanci modelu.
    Nakonec provede přesměrování na stránku home-page-edit.
    '''

    def post(self, request, *args, **kwargs):
        '''
        Zpracování HTTP POST požadavku.

        Tato metoda zpracovává odeslaný formulář pro úpravu HomePageIntroSection na domovské stránce.
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
        form = IntroSectionForm(request.POST)

        # Kontrola, zda je formulář validní
        if form.is_valid():

            # Získání nebo vytvoření instance modelu HomePageIntroSection
            intro_section = HomePageIntroSection.singleton()

            # Nastavení hodnot z formuláře do instance modelu
            intro_section.intro_title = form.cleaned_data['intro_title']
            intro_section.intro_description = form.cleaned_data['intro_description']
            intro_section.display_intro_section = form.cleaned_data['display_intro_section']

            # Uložení změn do databáze a přesměrování na stránku home-page-edit
            intro_section.save()
            return redirect('home-page-edit')

        # Pokud formulář validní není
        else:
            # Navrácení na stránku úprav a zobrazení zprávu o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('home-page-edit')

    def get(self, request, *args, **kwargs):
        '''
        Zpracování HTTP GET požadavku.

        Tato metoda kontroluje, zda požadavek GET obsahuje parametr 'show_intro_section'.
        Pokud ano, nastaví hodnotu pro zobrazení sekce patičky na True a provede přesměrování
        na stránku pro úpravu domovské stránky. Jinak pokračuje v běžném chování.

        :param request: Objekt HttpRequest obsahující data zaslaná klientem.
        :param args: Další pozicinální argumenty.
        :param kwargs: Další klíčové argumenty.
        :return: HttpResponse objekt reprezentující odpověď serveru na požadavek.
        '''

        # Kontrola zda požadavek get v sobě obsahuje pořadavek na zviditelnění sekce
        if 'show_intro_section' in request.GET:

            # Pokud ano - změna hodnoty a návrat na stránku pro úpravu HomePage
            intro_section = HomePageIntroSection.singleton()
            intro_section.display_intro_section = True
            intro_section.save()
            return redirect('home-page-edit')

        # Pokud ne, pokračuj normálně
        else:
            return super().get(request, *args, **kwargs)
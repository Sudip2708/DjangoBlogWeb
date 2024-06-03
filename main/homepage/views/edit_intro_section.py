from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages

from ..forms.intro_section_form import IntroSectionForm
from ..models.intro_section import HomePageIntroSection


class EditIntroSection(View):
    '''
    Pohled pro zpracování dat formuláře pro úvodní sekci na Home Page.

    Tato třída postupuje následovně:
    Po obdržení POST požadavku na zpracování dat z formuláře vytvoří instanci formuláře IntroSectionForm.
    Ověří, zda je formulář platný. Pokud ano, pokračuje.
    Získává nebo vytváří instanci modelu HomePageIntroSection.
    Nastavuje hodnoty z formuláře do příslušných polí instance modelu.
    Uložení změn do databáze voláním metody save() na instanci modelu.
    Nakonec provede přesměrování na stránku homepage-edit.
    '''

    def post(self, request, *args, **kwargs):
        '''
        Zpracování HTTP POST požadavku.

        Tato metoda zpracovává odeslaný formulář pro úpravu HomePageIntroSection na domovské stránce.
        Pokud je formulář validní, aktualizuje hodnoty v databázi
        a přesměruje uživatele na stránku pro úpravu domovské stránky.
        Pokud formulář není validní, zobrazí chybovou zprávu
        a přesměruje uživatele zpět na stránku pro úpravu s neuloženými změnami.
        '''

        # Načtení formuláře
        form = IntroSectionForm(request.POST)

        # Kontrola, zda je formulář validní
        if form.is_valid():

            # Získání nebo vytvoření instance modelu HomePageIntroSection
            intro_section, _ = HomePageIntroSection.objects.get_or_create(pk=1)

            # Nastavení hodnot z formuláře do instance modelu
            intro_section.intro_title = form.cleaned_data['intro_title']
            intro_section.intro_description = form.cleaned_data['intro_description']
            intro_section.display_intro_section = form.cleaned_data['display_intro_section']

            # Uložení změn do databáze a přesměrování na stránku homepage-edit
            intro_section.save()
            return redirect('homepage-edit')

        # Pokud formulář validní není
        else:
            # Navrácení na stránku úprav a zobrazení zprávy o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('homepage-edit')

    def get(self, request, *args, **kwargs):
        '''
        Zpracování HTTP GET požadavku.

        Tato metoda kontroluje, zda požadavek GET obsahuje parametr 'show_intro_section'.
        Pokud ano, nastaví hodnotu pro zobrazení sekce patičky na True a provede přesměrování
        na stránku pro úpravu domovské stránky. Jinak pokračuje v běžném chování.
        '''

        # Kontrola zda požadavek get v sobě obsahuje požadavek na zviditelnění sekce
        if 'show_intro_section' in request.GET:

            # Pokud ano - změna hodnoty a návrat na stránku pro úpravu HomePage
            intro_section, _ = HomePageIntroSection.objects.get_or_create(pk=1)
            intro_section.display_intro_section = True
            intro_section.save()
            return redirect('homepage-edit')

        # Pokud ne, pokračuj normálně
        else:
            return super().get(request, *args, **kwargs)

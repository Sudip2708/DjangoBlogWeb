from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages

from ..forms.divider_section_form import DividerSectionForm
from ..models.divider_section import HomePageDividerSection


class EditDividerSection(View):
    '''
    Pohled pro zpracování dat formuláře pro Divider sekci na Home Page.

    Tato třída postupuje následovně:
    Po obdržení POST požadavku na zpracování dat z formuláře vytvoří instanci formuláře DividerSectionForm.
    Ověří, zda je formulář platný. Pokud ano, pokračuje.
    Získává nebo vytváří instanci modelu HomePageDividerSection.
    Nastavuje hodnoty z formuláře do příslušných polí instance modelu.
    Ukládá změny do databáze voláním metody save() na instanci modelu.
    Nakonec provede přesměrování na stránku homepage-edit.
    '''

    def post(self, request, *args, **kwargs):
        '''
        Zpracování HTTP POST požadavku.

        Tato metoda zpracovává odeslaný formulář pro úpravu HomePageDividerSection na domovské stránce.
        Pokud je formulář validní, aktualizuje hodnoty v databázi
        a přesměruje uživatele na stránku pro úpravu domovské stránky.
        Pokud formulář není validní, zobrazí chybovou zprávu
        a přesměruje uživatele zpět na stránku pro úpravu s neuloženými změnami.
        '''

        # Načtení formuláře
        form = DividerSectionForm(request.POST, request.FILES)

        # Kontrola, zda je formulář validní
        if form.is_valid():

            # Získání nebo vytvoření instance modelu HomePageDividerSection
            divider_section = HomePageDividerSection.singleton()

            # Nastavení hodnot z formuláře do instance modelu
            divider_section.divider_image = form.cleaned_data['divider_image']
            divider_section.divider_text = form.cleaned_data['divider_text']
            divider_section.divider_link = form.cleaned_data['divider_link']
            divider_section.display_divider_section = form.cleaned_data['display_divider_section']

            # Uložení změn do databáze a přesměrování na stránku homepage-edit
            divider_section.save()
            return redirect('homepage-edit')

        # Pokud formulář validní není
        else:
            # Navrácení na stránku úprav a zobrazení zprávu o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('homepage-edit')

    def get(self, request, *args, **kwargs):
        '''
        Zpracování HTTP GET požadavku.

        Tato metoda kontroluje, zda požadavek GET obsahuje parametr 'show_divider_section'.
        Pokud ano, nastaví hodnotu pro zobrazení sekce patičky na True a provede přesměrování
        na stránku pro úpravu domovské stránky. Jinak pokračuje v běžném chování.
        '''

        # Kontrola zda požadavek get v sobě obsahuje pořadavek na zviditelnění sekce
        if 'show_divider_section' in request.GET:

            # Pokud ano - změna hodnoty a návrat na stránku pro úpravu HomePage
            divider_section = HomePageDividerSection.singleton()
            divider_section.display_divider_section = True
            divider_section.save()
            return redirect('homepage-edit')

        # Pokud ne, pokračuj normálně
        else:
            return super().get(request, *args, **kwargs)
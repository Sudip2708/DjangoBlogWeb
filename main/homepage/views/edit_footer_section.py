from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages

from ..forms.footer_section_form import FooterSettingsForm
from ..models.footer_section import FooterSettings
from ..models.data.save_footer_data import save_footer_data

class EditFooterSection(View):
    '''
    Pohled pro zpracování dat formuláře pro sekci patičky na Home Page

    Tato třída postupuje následovně:
    Po obdržení POST požadavku na zpracování dat z formuláře vytvoří instanci formuláře FooterSettingsForm.
    Ověří, zda je formulář platný. Pokud ano, pokračuje.
    Uložení dat z formuláře voláním funkce save_footer_data().
    Nakonec provede přesměrování na stránku home-page-edit.
    '''

    def post(self, request, *args, **kwargs):
        '''
        Zpracování HTTP POST požadavku.

        Tato metoda zpracovává odeslaný formulář pro úpravu FooterSettingsForm.
        Pokud je formulář validní, volá metodu pro uložení dat
        a přesměruje uživatele na stránku pro úpravu domovské stránky.
        Pokud formulář není validní, zobrazí chybovou zprávu
        a přesměruje uživatele zpět na stránku pro úpravu s neuloženými změnami.
        '''

        # Načtení formuláře
        form = FooterSettingsForm(request.POST)

        # Kontrola, zda je formulář validní
        if form.is_valid():

            # Volání metody pro uložení dat do databáze a přesměrování na stránku home-page-edit
            save_footer_data(form)
            return redirect('home-page-edit')

        # Pokud formulář validní není
        else:
            # Navrácení na stránku úprav a zobrazení zprávy o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('home-page-edit')

    def get(self, request, *args, **kwargs):
        '''
        Zpracování HTTP GET požadavku.

        Tato metoda kontroluje, zda požadavek GET obsahuje parametr 'show_footer_section'.
        Pokud ano, nastaví hodnotu pro zobrazení sekce patičky na True a provede přesměrování
        na stránku pro úpravu domovské stránky. Jinak pokračuje v běžném chování.
        '''

        # Kontrola, zda požadavek get obsahuje požadavek na zviditelnění sekce
        if 'show_footer_section' in request.GET:

            # Pokud ano - změna hodnoty a návrat na stránku pro úpravu HomePage
            footer_settings = FooterSettings.singleton()
            footer_settings.display_footer_section = True
            footer_settings.save()
            return redirect('home-page-edit')

        # Pokud ne, pokračujte normálně
        else:
            return super().get(request, *args, **kwargs)

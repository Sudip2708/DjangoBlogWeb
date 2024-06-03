from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages

from ..forms.newsletter_section_form import NewsletterSectionForm
from ..models.newsletter_section import HomePageNewsletterSection


class EditNewsletterSection(View):
    '''
    Pohled pro zpracování dat formuláře pro sekci newsletteru na Home Page.

    Tato třída postupuje následovně:
    Po obdržení POST požadavku na zpracování dat z formuláře vytvoří instanci formuláře NewsletterSectionForm.
    Ověří, zda je formulář platný. Pokud ano, pokračuje.
    Získává nebo vytváří instanci modelu HomePageNewsletterSection.
    Nastavuje hodnoty z formuláře do příslušných polí instance modelu.
    Uložení změn do databáze voláním metody save() na instanci modelu.
    Nakonec provede přesměrování na stránku homepage-edit.
    '''

    def post(self, request, *args, **kwargs):
        '''
        Zpracování HTTP POST požadavku.

        Tato metoda zpracovává odeslaný formulář pro úpravu HomePageNewsletterSection na domovské stránce.
        Pokud je formulář validní, aktualizuje hodnoty v databázi
        a přesměruje uživatele na stránku pro úpravu domovské stránky.
        Pokud formulář není validní, zobrazí chybovou zprávu
        a přesměruje uživatele zpět na stránku pro úpravu s neuloženými změnami.
        '''

        # Načtení formuláře
        form = NewsletterSectionForm(request.POST)

        # Kontrola, zda je formulář validní
        if form.is_valid():

            # Získání nebo vytvoření instance modelu HomePageNewsletterSection
            newsletter_section, _ = HomePageNewsletterSection.objects.get_or_create(pk=1)

            # Nastavení hodnot z formuláře do instance modelu
            newsletter_section.newsletter_title = form.cleaned_data['newsletter_title']
            newsletter_section.newsletter_description = form.cleaned_data['newsletter_description']
            newsletter_section.newsletter_subscribers = form.cleaned_data['newsletter_subscribers']
            newsletter_section.display_newsletter_section = form.cleaned_data['display_newsletter_section']

            # Uložení změn do databáze a přesměrování na stránku homepage-edit
            newsletter_section.save()
            return redirect('homepage-edit')

        # Pokud formulář validní není
        else:
            # Navrácení na stránku úprav a zobrazení zprávy o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('homepage-edit')

    def get(self, request, *args, **kwargs):
        '''
        Zpracování HTTP GET požadavku.

        Tato metoda kontroluje, zda požadavek GET obsahuje parametr 'show_newsletter_section'.
        Pokud ano, nastaví hodnotu pro zobrazení sekce patičky na True a provede přesměrování
        na stránku pro úpravu domovské stránky. Jinak pokračuje v běžném chování.
        '''

        # Kontrola zda požadavek get v sobě obsahuje požadavek na zviditelnění sekce
        if 'show_newsletter_section' in request.GET:

            # Pokud ano - změna hodnoty a návrat na stránku pro úpravu HomePage
            newsletter_section, _ = HomePageNewsletterSection.objects.get_or_create(pk=1)
            newsletter_section.display_newsletter_section = True
            newsletter_section.save()
            return redirect('homepage-edit')

        # Pokud ne, pokračuj normálně
        else:
            return super().get(request, *args, **kwargs)

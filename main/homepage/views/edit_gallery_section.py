from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages

from ..forms.gallery_section_form import GallerySectionForm
from ..models.gallery_section import HomePageGallerySection


class EditGallerySection(View):
    '''
    Pohled pro zpracování dat formuláře pro sekci galerie článků na Home Page

    Tato třída postupuje následovně:
    Po obdržení POST požadavku na zpracování dat z formuláře vytvoří instanci formuláře GallerySectionForm.
    Ověří, zda je formulář platný. Pokud ano, pokračuje.
    Získává nebo vytváří instanci modelu HomePageGallerySection.
    Nastavuje hodnoty z formuláře do příslušných polí instance modelu.
    Uložení změn do databáze voláním metody save() na instanci modelu.
    Nakonec provede přesměrování na stránku home-page-edit.
    '''

    def post(self, request, *args, **kwargs):
        '''
        Zpracování HTTP POST požadavku.

        Tato metoda zpracovává odeslaný formulář pro úpravu HomePageGallerySection na domovské stránce.
        Pokud je formulář validní, aktualizuje hodnoty v databázi
        a přesměruje uživatele na stránku pro úpravu domovské stránky.
        Pokud formulář není validní, zobrazí chybovou zprávu
        a přesměruje uživatele zpět na stránku pro úpravu s neuloženými změnami.
        '''

        # Načtení formuláře
        form = GallerySectionForm(request.POST)

        # Kontrola, zda je formulář validní
        if form.is_valid():

            # Získání nebo vytvoření instance modelu HomePageGallerySection
            gallery_instance = HomePageGallerySection.singleton()

            # Nastavení hodnot z formuláře do instance modelu
            gallery_instance.gallery_article_1 = form.cleaned_data['gallery_article_1']
            gallery_instance.gallery_article_2 = form.cleaned_data['gallery_article_2']
            gallery_instance.gallery_article_3 = form.cleaned_data['gallery_article_3']
            gallery_instance.gallery_article_4 = form.cleaned_data['gallery_article_4']
            gallery_instance.display_gallery_section = form.cleaned_data['display_gallery_section']

            # Uložení změn do databáze a přesměrování na stránku home-page-edit
            gallery_instance.save()
            return redirect('home-page-edit')

        # Pokud formulář validní není
        else:
            # Navrácení na stránku úprav a zobrazení zprávu o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('home-page-edit')

    def get(self, request, *args, **kwargs):
        '''
        Zpracování HTTP GET požadavku.

        Tato metoda kontroluje, zda požadavek GET obsahuje parametr 'show_gallery_section'.
        Pokud ano, nastaví hodnotu pro zobrazení sekce patičky na True a provede přesměrování
        na stránku pro úpravu domovské stránky. Jinak pokračuje v běžném chování.
        '''

        # Kontrola zda požadavek get v sobě obsahuje pořadavek na zviditelnění sekce
        if 'show_gallery_section' in request.GET:

            # Pokud ano - změna hodnoty a návrat na stránku pro úpravu HomePage
            gallery_section = HomePageGallerySection.singleton()
            gallery_section.display_gallery_section = True
            gallery_section.save()
            return redirect('home-page-edit')

        # Pokud ne, pokračuj normálně
        else:
            return super().get(request, *args, **kwargs)
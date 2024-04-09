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

        # Načtení formuláře
        form = HeroSectionForm(request.POST, request.FILES)

        # Kontrola, zda data odpovídají formuláři
        if form.is_valid():

            # Získání nebo vytvoření instance modelu HomePageHeroSection
            hero_section = HomePageHeroSection.singleton()

            # Nastavení hodnot z formuláře do instance modelu
            hero_section.hero_image = form.cleaned_data['hero_image']
            hero_section.hero_title = form.cleaned_data['hero_title']
            hero_section.hero_link_title = form.cleaned_data['hero_link_title']
            hero_section.hero_link = form.cleaned_data['hero_link']
            hero_section.display_hero_section = form.cleaned_data['display_hero_section']

            # Uložení změn do databáze
            hero_section.save()

            # Přesměrování na stránku home-page-edit
            return redirect('home-page-edit')

        # Pokud data neodpovídají formuláři
        else:

            # Vrať se zpět na stránku úprav a zobraz zprávu o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('home-page-edit')

    def get(self, request, *args, **kwargs):



        # Zkontroluj, zda byla kliknuta kotva
        if 'show_hero_section' in request.GET:

            # Získání nebo vytvoření instance modelu HomePageHeroSection
            hero_section = HomePageHeroSection.singleton()

            # Nastavení pole display_hero_section na True
            hero_section.display_hero_section = True
            hero_section.save()

            # Přesměrování na stránku home-page-edit
            return redirect('home-page-edit')

        else:
            # Pokud nebyla kliknuta kotva, pokračuj normálně
            return super().get(request, *args, **kwargs)

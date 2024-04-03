from django.shortcuts import redirect
from django.views.generic import View
from homepage.forms.hero_section_form import HomePageHeroSectionForm
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
    Ukládá změny do databáze voláním metody save() na instanci modelu.
    Nakonec provede přesměrování na stránku home-page-edit.
    '''

    def post(self, request, *args, **kwargs):
        form = HomePageHeroSectionForm(request.POST, request.FILES)

        if form.is_valid():
            # Zde můžete provést další validaci, pokud je to potřeba
            # Získání nebo vytvoření instance modelu HomePageHeroSection
            hero_section, created = HomePageHeroSection.objects.get_or_create()

            # Nastavení hodnot z formuláře do instance modelu
            hero_section.hero_image = form.cleaned_data['hero_image']
            hero_section.hero_title = form.cleaned_data['hero_title']
            hero_section.hero_link_title = form.cleaned_data['hero_link_title']
            hero_section.hero_link = form.cleaned_data['hero_link']

            # Uložení změn do databáze
            hero_section.save()

            # Přesměrování na stránku home-page-edit
            return redirect('home-page-edit')
        else:
            # Pokud formulář není platný, přesměrujeme zpět na stránku úprav
            # a zobrazíme zprávu o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('home-page-edit')

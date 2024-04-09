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
        form = IntroSectionForm(request.POST)

        if form.is_valid():
            # Zde můžete provést další validaci, pokud je to potřeba
            # Získání nebo vytvoření instance modelu HomePageIntroSection
            intro_section = HomePageIntroSection.singleton()

            # Nastavení hodnot z formuláře do instance modelu
            intro_section.intro_title = form.cleaned_data['intro_title']
            intro_section.intro_description = form.cleaned_data['intro_description']
            intro_section.display_intro_section = form.cleaned_data['display_intro_section']

            # Uložení změn do databáze
            intro_section.save()

            # Přesměrování na stránku home-page-edit
            return redirect('home-page-edit')

        else:

            # Vrať se zpět na stránku úprav a zobraz zprávu o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('home-page-edit')
    def get(self, request, *args, **kwargs):


        # Zkontroluj, zda byla kliknuta kotva
        if 'show_intro_section' in request.GET:

            # Získání nebo vytvoření instance modelu HomePageIntroSection
            intro_section = HomePageIntroSection.singleton()

            # Nastavení pole display_intro_section na True
            intro_section.display_intro_section = True
            intro_section.save()

            # Přesměrování na stránku home-page-edit
            return redirect('home-page-edit')

        else:
            # Pokud nebyla kliknuta kotva, pokračuj normálně
            return super().get(request, *args, **kwargs)
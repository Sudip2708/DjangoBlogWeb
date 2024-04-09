from django.shortcuts import redirect
from django.views.generic import View
from homepage.forms.divider_section_form import DividerSectionForm
from homepage.models.divider_section import HomePageDividerSection
from django.contrib import messages


class EditDividerSection(View):
    '''
    Třída pro zpracování dat formuláře pro Divider sekci na Home Page

    Tato třída postupuje následovně:
    Po obdržení POST požadavku na zpracování dat z formuláře vytvoří instanci formuláře DividerSectionForm.
    Ověří, zda je formulář platný. Pokud ano, pokračuje.
    Získává nebo vytváří instanci modelu HomePageDividerSection.
    Nastavuje hodnoty z formuláře do příslušných polí instance modelu.
    Ukládá změny do databáze voláním metody save() na instanci modelu.
    Nakonec provede přesměrování na stránku home-page-edit.
    '''

    def post(self, request, *args, **kwargs):
        form = DividerSectionForm(request.POST, request.FILES)

        if form.is_valid():
            # Zde můžete provést další validaci, pokud je to potřeba
            # Získání nebo vytvoření instance modelu HomePageDividerSection
            divider_section = HomePageDividerSection.singleton()

            # Nastavení hodnot z formuláře do instance modelu
            divider_section.divider_image = form.cleaned_data['divider_image']
            divider_section.divider_text = form.cleaned_data['divider_text']
            divider_section.divider_link = form.cleaned_data['divider_link']
            divider_section.display_divider_section = form.cleaned_data['display_divider_section']

            # Uložení změn do databáze
            divider_section.save()

            # Přesměrování na stránku home-page-edit
            return redirect('home-page-edit')

        else:

            # Vrať se zpět na stránku úprav a zobraz zprávu o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('home-page-edit')

    def get(self, request, *args, **kwargs):

        # Zkontroluj, zda byla kliknuta kotva
        if 'show_divider_section' in request.GET:

            # Pokud ano - zapiš hodnotu do databáze a vrať se zpátky na stránku pro úpravi HomePage
            divider_section = HomePageDividerSection.singleton()
            divider_section.display_divider_section = True
            divider_section.save()
            return redirect('home-page-edit')

        else:
            # Pokud nebyla kliknuta kotva, pokračuj normálně
            return super().get(request, *args, **kwargs)
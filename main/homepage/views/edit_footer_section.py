from django.shortcuts import redirect
from django.views.generic import View
from homepage.forms.footer_section_form import FooterSettingsForm
from homepage.models.footer_section import FooterSettings
from django.contrib import messages


class EditFooterSection(View):
    '''
    Třída pro zpracování dat formuláře pro sekci patičky na Home Page

    Tato třída postupuje následovně:
    Po obdržení POST požadavku na zpracování dat z formuláře vytvoří instanci formuláře FooterSettingsForm.
    Ověří, zda je formulář platný. Pokud ano, pokračuje.
    Získává nebo vytváří instanci modelu FooterSettings.
    Nastavuje hodnoty z formuláře do příslušných polí instance modelu.
    Uložení změn do databáze voláním metody save() na instanci modelu.
    Nakonec provede přesměrování na stránku home-page-edit.
    '''

    def post(self, request, *args, **kwargs):
        form = FooterSettingsForm(request.POST)

        if form.is_valid():
            # Zde můžete provést další validaci, pokud je to potřeba

            # Získání nebo vytvoření instance modelu FooterSettings
            footer_settings = FooterSettings.singleton()

            # Nastavení hodnot z formuláře do instance modelu
            for field_name, field_value in form.cleaned_data.items():
                setattr(footer_settings, field_name, field_value)

            # Uložení změn do databáze
            footer_settings.save()

            # Přesměrování na stránku home-page-edit
            return redirect('home-page-edit')

        else:

            # Vrať se zpět na stránku úprav a zobraz zprávu o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('home-page-edit')

    def get(self, request, *args, **kwargs):

        # Zkontroluj, zda byla kliknuta kotva
        if 'show_footer_section' in request.GET:

            # Pokud ano - zapiš hodnotu do databáze a vrať se zpátky na stránku pro úpravi HomePage
            footer_settings = FooterSettings.singleton()
            footer_settings.display_footer_section = True
            footer_settings.save()
            return redirect('home-page-edit')

        else:
            # Pokud nebyla kliknuta kotva, pokračuj normálně
            return super().get(request, *args, **kwargs)
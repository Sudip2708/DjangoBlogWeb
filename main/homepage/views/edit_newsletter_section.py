from django.shortcuts import redirect
from django.views.generic import View
from homepage.forms.newsletter_section_form import NewsletterSectionForm
from homepage.models.newsletter_section import HomePageNewsletterSection
from django.contrib import messages


class EditNewsletterSection(View):
    '''
    Třída pro zpracování dat formuláře pro sekci newsletteru na Home Page

    Tato třída postupuje následovně:
    Po obdržení POST požadavku na zpracování dat z formuláře vytvoří instanci formuláře NewsletterSectionForm.
    Ověří, zda je formulář platný. Pokud ano, pokračuje.
    Získává nebo vytváří instanci modelu HomePageNewsletterSection.
    Nastavuje hodnoty z formuláře do příslušných polí instance modelu.
    Uložení změn do databáze voláním metody save() na instanci modelu.
    Nakonec provede přesměrování na stránku home-page-edit.
    '''

    def post(self, request, *args, **kwargs):
        form = NewsletterSectionForm(request.POST)

        if form.is_valid():
            # Zde můžete provést další validaci, pokud je to potřeba
            # Získání nebo vytvoření instance modelu HomePageNewsletterSection
            newsletter_section = HomePageNewsletterSection.singleton()

            # Nastavení hodnot z formuláře do instance modelu
            newsletter_section.newsletter_title = form.cleaned_data['newsletter_title']
            newsletter_section.newsletter_description = form.cleaned_data['newsletter_description']
            newsletter_section.newsletter_subscribers = form.cleaned_data['newsletter_subscribers']
            newsletter_section.display_newsletter_section = form.cleaned_data['display_newsletter_section']

            # Uložení změn do databáze
            newsletter_section.save()

            # Přesměrování na stránku home-page-edit
            return redirect('home-page-edit')

        else:

            # Vrať se zpět na stránku úprav a zobraz zprávu o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('home-page-edit')

    def get(self, request, *args, **kwargs):

        # Zkontroluj, zda byla kliknuta kotva
        if 'show_newsletter_section' in request.GET:

            # Pokud ano - zapiš hodnotu do databáze a vrať se zpátky na stránku pro úpravi HomePage
            newsletter_section = HomePageNewsletterSection.singleton()
            newsletter_section.display_newsletter_section = True
            newsletter_section.save()
            return redirect('home-page-edit')

        else:
            # Pokud nebyla kliknuta kotva, pokračuj normálně
            return super().get(request, *args, **kwargs)
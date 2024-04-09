from django.shortcuts import redirect
from django.views.generic import View
from homepage.forms.latest_section_form import LatestArticlesForm
from homepage.models.latest_section import HomePageLatestArticles
from django.contrib import messages


class EditLatestArticlesSection(View):
    '''
    Třída pro zpracování dat formuláře pro sekci nejnovějších článků na Home Page

    Tato třída postupuje následovně:
    Po obdržení POST požadavku na zpracování dat z formuláře vytvoří instanci formuláře LatestArticlesForm.
    Ověří, zda je formulář platný. Pokud ano, pokračuje.
    Získává nebo vytváří instanci modelu HomePageLatestArticles.
    Nastavuje hodnoty z formuláře do příslušných polí instance modelu.
    Uložení změn do databáze voláním metody save() na instanci modelu.
    Nakonec provede přesměrování na stránku home-page-edit.
    '''

    def post(self, request, *args, **kwargs):
        form = LatestArticlesForm(request.POST)

        if form.is_valid():
            # Zde můžete provést další validaci, pokud je to potřeba
            # Získání nebo vytvoření instance modelu HomePageLatestArticles
            latest_articles_section = HomePageLatestArticles.singleton()

            # Nastavení hodnot z formuláře do instance modelu
            latest_articles_section.latest_title = form.cleaned_data['latest_title']
            latest_articles_section.latest_description = form.cleaned_data['latest_description']
            latest_articles_section.latest_article_1 = form.cleaned_data['latest_article_1']
            latest_articles_section.latest_article_2 = form.cleaned_data['latest_article_2']
            latest_articles_section.latest_article_3 = form.cleaned_data['latest_article_3']
            latest_articles_section.display_latest_section = form.cleaned_data['display_latest_section']

            # Uložení změn do databáze
            latest_articles_section.save()

            # Přesměrování na stránku home-page-edit
            return redirect('home-page-edit')

        else:

            # Vrať se zpět na stránku úprav a zobraz zprávu o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('home-page-edit')

    def get(self, request, *args, **kwargs):

        # Zkontroluj, zda byla kliknuta kotva
        if 'show_latest_section' in request.GET:

            # Pokud ano - zapiš hodnotu do databáze a vrať se zpátky na stránku pro úpravi HomePage
            latest_articles_section = HomePageLatestArticles.singleton()
            latest_articles_section.display_latest_section = True
            latest_articles_section.save()
            return redirect('home-page-edit')

        else:
            # Pokud nebyla kliknuta kotva, pokračuj normálně
            return super().get(request, *args, **kwargs)
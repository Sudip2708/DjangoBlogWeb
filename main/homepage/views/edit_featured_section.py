from django.shortcuts import redirect
from django.views.generic import View
from homepage.forms.featured_section_form import FeaturedArticlesForm
from homepage.models.featured_section import HomePageFeaturedArticles
from django.contrib import messages


class EditFeaturedArticlesSection(View):
    '''
    Třída pro zpracování dat formuláře pro sekci označených článků na Home Page

    Tato třída postupuje následovně:
    Po obdržení POST požadavku na zpracování dat z formuláře vytvoří instanci formuláře FeaturedArticlesForm.
    Ověří, zda je formulář platný. Pokud ano, pokračuje.
    Získává nebo vytváří instanci modelu HomePageFeaturedArticles.
    Nastavuje hodnoty z formuláře do příslušných polí instance modelu.
    Uložení změn do databáze voláním metody save() na instanci modelu.
    Nakonec provede přesměrování na stránku home-page-edit.
    '''
    def post(self, request, *args, **kwargs):
        form = FeaturedArticlesForm(request.POST)

        if form.is_valid():
            # Zde můžete provést další validaci, pokud je to potřeba
            # Získání nebo vytvoření instance modelu HomePageFeaturedArticles
            featured_articles = HomePageFeaturedArticles.singleton()

            # Nastavení hodnot z formuláře do instance modelu
            featured_articles.featured_article_1 = form.cleaned_data['featured_article_1']
            featured_articles.featured_article_2 = form.cleaned_data['featured_article_2']
            featured_articles.featured_article_3 = form.cleaned_data['featured_article_3']
            featured_articles.display_featured_section = form.cleaned_data['display_featured_section']

            # Uložení změn do databáze
            featured_articles.save()

            # Přesměrování na stránku home-page-edit
            return redirect('home-page-edit')

        else:

            # Vrať se zpět na stránku úprav a zobraz zprávu o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('home-page-edit')

    def get(self, request, *args, **kwargs):

        # Zkontroluj, zda byla kliknuta kotva
        if 'show_featured_section' in request.GET:

            # Pokud ano - zapiš hodnotu do databáze a vrať se zpátky na stránku pro úpravi HomePage
            featured_articles = HomePageFeaturedArticles.singleton()
            featured_articles.display_featured_section = True
            featured_articles.save()
            return redirect('home-page-edit')

        else:
            # Pokud nebyla kliknuta kotva, pokračuj normálně
            return super().get(request, *args, **kwargs)
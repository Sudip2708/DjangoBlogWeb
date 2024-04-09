from django.shortcuts import redirect
from django.views.generic import View
from homepage.forms.gallery_section_form import GallerySectionForm
from homepage.models.gallery_section import HomePageGallerySection
from django.contrib import messages


class EditGallerySection(View):
    '''
    Třída pro zpracování dat formuláře pro sekci galerie článků na Home Page

    Tato třída postupuje následovně:
    Po obdržení POST požadavku na zpracování dat z formuláře vytvoří instanci formuláře GallerySectionForm.
    Ověří, zda je formulář platný. Pokud ano, pokračuje.
    Získává nebo vytváří instanci modelu HomePageGallerySection.
    Nastavuje hodnoty z formuláře do příslušných polí instance modelu.
    Uložení změn do databáze voláním metody save() na instanci modelu.
    Nakonec provede přesměrování na stránku home-page-edit.
    '''

    def post(self, request, *args, **kwargs):
        form = GallerySectionForm(request.POST)

        if form.is_valid():
            # Zde můžete provést další validaci, pokud je to potřeba
            # Získání nebo vytvoření instance modelu HomePageGallerySection
            gallery_section = HomePageGallerySection.singleton()

            # Nastavení hodnot z formuláře do instance modelu
            gallery_section.gallery_article_1 = form.cleaned_data['gallery_article_1']
            gallery_section.gallery_article_2 = form.cleaned_data['gallery_article_2']
            gallery_section.gallery_article_3 = form.cleaned_data['gallery_article_3']
            gallery_section.gallery_article_4 = form.cleaned_data['gallery_article_4']
            gallery_section.display_gallery_section = form.cleaned_data['display_gallery_section']

            # Uložení změn do databáze
            gallery_section.save()

            # Přesměrování na stránku home-page-edit
            return redirect('home-page-edit')

        else:

            # Vrať se zpět na stránku úprav a zobraz zprávu o neúspěchu
            messages.error(request, "Provedené úpravy nebyly uloženy.")
            return redirect('home-page-edit')

    def get(self, request, *args, **kwargs):

        # Zkontroluj, zda byla kliknuta kotva
        if 'show_gallery_section' in request.GET:

            # Pokud ano - zapiš hodnotu do databáze a vrať se zpátky na stránku pro úpravi HomePage
            gallery_section = HomePageGallerySection.singleton()
            gallery_section.display_gallery_section = True
            gallery_section.save()
            return redirect('home-page-edit')

        else:
            # Pokud nebyla kliknuta kotva, pokračuj normálně
            return super().get(request, *args, **kwargs)
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages

from homepage.forms.gallery_section_form import GallerySectionForm
from homepage.models.gallery_section import HomePageGallerySection
from articles.models.article import Article



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
        '''
        Zpracování HTTP POST požadavku.

        Tato metoda zpracovává odeslaný formulář pro úpravu HomePageGallerySection na domovské stránce.
        Pokud je formulář validní, aktualizuje hodnoty v databázi
        a přesměruje uživatele na stránku pro úpravu domovské stránky.
        Pokud formulář není validní, zobrazí chybovou zprávu
        a přesměruje uživatele zpět na stránku pro úpravu s neuloženými změnami.

        :param request: Objekt HttpRequest obsahující data zaslaná klientem.
        :param args: Další pozicinální argumenty.
        :param kwargs: Další klíčové argumenty.
        :return: HttpResponse objekt reprezentující odpověď serveru na požadavek.
        '''

        # Načtení formuláře
        form = GallerySectionForm(request.POST)

        # Kontrola, zda je formulář validní
        if form.is_valid():

            # Získání nebo vytvoření instance modelu HomePageGallerySection
            gallery_instance = HomePageGallerySection.singleton()

            # Uložení hodnot do slovníku pro vybrané články
            for n in range(1, 5):

                # Načtení ID článku
                article_field = f"gallery_article_{n}"
                article_id = form.cleaned_data.get(article_field)

                # Pokud ID článku nerovná se 0 (nejedná se o defaultní článek)
                if article_id != "0":

                    # Načtení dat z modelu článku
                    article = Article.objects.get(pk=article_id)

                    # Získání aktuálního slovníku pro článek
                    gallery_article_dict = getattr(gallery_instance, article_field)

                    # Aktualizace hodnot ve slovníku
                    gallery_article_dict["picture_preview_path"] = article.main_picture_for_article.url
                    gallery_article_dict["picture_max_size_path"] = article.main_picture_max_size.url
                    gallery_article_dict["title"] = article.title
                    gallery_article_dict["article_id"] = article.id

                    # Aktualizace slovníku v instanci modelu
                    setattr(gallery_instance, article_field, gallery_article_dict)

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

        :param request: Objekt HttpRequest obsahující data zaslaná klientem.
        :param args: Další pozicinální argumenty.
        :param kwargs: Další klíčové argumenty.
        :return: HttpResponse objekt reprezentující odpověď serveru na požadavek.
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
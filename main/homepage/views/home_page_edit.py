from django.shortcuts import render

from .home_page import BaseHomePageView

from homepage.models.hero_section import HomePageHeroSection
from homepage.models.intro_section import HomePageIntroSection
from homepage.models.featured_section import HomePageFeaturedArticles
from homepage.models.divider_section import HomePageDividerSection
from homepage.models.latest_section import HomePageLatestArticles
from homepage.models.newsletter_section import HomePageNewsletterSection
from homepage.models.gallery_section import HomePageGallerySection
from homepage.models.footer_section import FooterSettings

from homepage.forms.hero_section_form import HeroSectionForm
from homepage.forms.intro_section_form import IntroSectionForm
from homepage.forms.featured_section_form import FeaturedArticlesForm
from homepage.forms.divider_section_form import DividerSectionForm
from homepage.forms.latest_section_form import LatestArticlesForm
from homepage.forms.newsletter_section_form import NewsletterSectionForm
from homepage.forms.gallery_section_form import GallerySectionForm
from homepage.forms.footer_section_form import FooterSettingsForm


class HomePageEditView(BaseHomePageView):
    '''
    Třída pro úpravu obsahu domovské stránky.

    Tato třída dědí z BaseHomePageView a používá metodu `get_home_page_data` pro získání dat
    pro zobrazení domovské stránky a následně přidává formuláře pro úpravu obsahu různých sekcí.
    '''

    def get(self, request, *args, **kwargs):
        '''
        Metoda pro získání dat a zobrazení stránky pro úpravu obsahu domovské stránky.

        :param request: HttpRequest
        :param args: Pozicinální argumenty
        :param kwargs: Klíčové argumenty
        :return: HttpResponse
        '''

        # Načtení kontextu z BaseHomePageView
        context = self.get_home_page_data()

        # Přidání formulářů pro editaci stránky
        hero_edit_form = HeroSectionForm(instance=HomePageHeroSection.singleton())
        intro_edit_form = IntroSectionForm(instance=HomePageIntroSection.singleton())
        featured_edit_form = FeaturedArticlesForm(instance=HomePageFeaturedArticles.singleton())
        divider_edit_form = DividerSectionForm(instance=HomePageDividerSection.singleton())
        latest_edit_form = LatestArticlesForm(instance=HomePageLatestArticles.singleton())
        newsletter_edit_form = NewsletterSectionForm(instance=HomePageNewsletterSection.singleton())
        gallery_edit_form = GallerySectionForm(instance=HomePageGallerySection.singleton())
        footer_edit_form = FooterSettingsForm(instance=FooterSettings.singleton())

        # Přidání formulářů do kontextu
        context.update({
            'hero_edit_form': hero_edit_form,
            'intro_edit_form': intro_edit_form,
            'featured_edit_form': featured_edit_form,
            'divider_edit_form': divider_edit_form,
            'latest_edit_form': latest_edit_form,
            'newsletter_edit_form': newsletter_edit_form,
            'gallery_edit_form': gallery_edit_form,
            'footer_edit_form': footer_edit_form,
        })

        # Navrácení stránky
        return render(request, '1_home/10__base__.html', context)

from django.shortcuts import render
from django.views.generic import View

from homepage.models.hero_section import HomePageHeroSection
from homepage.models.intro_section import HomePageIntroSection
from homepage.models.featured_section import HomePageFeaturedArticles
from homepage.models.divider_section import HomePageDividerSection
from homepage.models.latest_section import HomePageLatestArticles
from homepage.models.newsletter_section import HomePageNewsletterSection
from homepage.models.gallery_section import HomePageGallerySection
from homepage.models.footer_section import FooterSettings


class BaseHomePageView(View):
    '''
    Základní třída pro zobrazení dat domovské stránky.

    Tato třída definuje metodu `get_home_page_data`, která získává data pro zobrazení domovské stránky
    z různých sekcí, jako je hrdinská sekce, úvodní sekce, sekce s významnými články atd.
    '''

    def get_home_page_data(self):
        '''
        Metoda pro získání dat domovské stránky.

        :return: Slovník obsahující data pro zobrazení domovské stránky.
        '''

        # Načtení dat pro vytvoření základního kontextu pro HomePage
        hero_data = HomePageHeroSection.singleton().get_hero_settings
        intro_data = HomePageIntroSection.singleton().get_intro_settings
        featured_data = HomePageFeaturedArticles.singleton().get_featured_settings
        divider_data = HomePageDividerSection.singleton().get_divider_settings
        latest_data = HomePageLatestArticles.singleton().get_latest_settings
        newsletter_data = HomePageNewsletterSection.singleton().get_newsletter_settings
        gallery_data = HomePageGallerySection.singleton().get_gallery_settings
        footer_data = FooterSettings.singleton().get_footer_settings
        print("############# featured_data", featured_data)

        # Přidání dat do kontextu
        return {
            'hero_data': hero_data,
            'intro_data': intro_data,
            'featured_data': featured_data,
            'divider_data': divider_data,
            'latest_data': latest_data,
            'newsletter_data': newsletter_data,
            'gallery_data': gallery_data,
            'footer_data': footer_data,
        }


class HomePageView(BaseHomePageView):
    '''
    Třída pro zobrazení domovské stránky.

    Tato třída dědí z BaseHomePageView a používá metodu `get_home_page_data` pro získání dat
    pro zobrazení domovské stránky. Poté renderuje šablonu domovské stránky s těmito daty.
    '''

    def get(self, request, *args, **kwargs):
        '''
        Metoda pro získání dat a zobrazení domovské stránky.

        :param request: HttpRequest
        :param args: Pozicinální argumenty
        :param kwargs: Klíčové argumenty
        :return: HttpResponse
        '''

        # Načtení kontextu z BaseHomePageView
        context = self.get_home_page_data()

        # Navrácení stránky
        return render(request, '1_home/10__base__.html', context)

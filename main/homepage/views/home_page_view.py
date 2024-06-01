from django.shortcuts import render
from django.views.generic import TemplateView

from common_data.base_view import BaseView

from ..models.hero_section import HomePageHeroSection
from ..models.intro_section import HomePageIntroSection
from ..models.featured_section import HomePageFeaturedArticles
from ..models.divider_section import HomePageDividerSection
from ..models.latest_section import HomePageLatestArticles
from ..models.newsletter_section import HomePageNewsletterSection
from ..models.gallery_section import HomePageGallerySection
from ..models.footer_section import FooterSettings


class HomePageView(BaseView, TemplateView):
    '''
    Pohled pro zobrazení obsahu domovské stránky.

    Pohled načítá jednotlivé data pro sekce stránky z jejich modelů
    a navrací šablonu s daty pro zobrazení domácí stránky.
    '''

    template_name = '1_home/10__base__.html'

    def __init__(self):
        '''
        Metoda pro základní inicializaci třídy.

        Metoda načítá instance modelů jednotlivých sekcí a vytváří pro ně atributy.
        Atributy jsou použity jakv tomto kodu, tak i v pohledu HomePageEditView,
        který dědí z tohoto pohledu.
        '''
        self.hero_instance = HomePageHeroSection.singleton()
        self.intro_instance = HomePageIntroSection.singleton()
        self.featured_instance = HomePageFeaturedArticles.singleton()
        self.divider_instance = HomePageDividerSection.singleton()
        self.latest_instance = HomePageLatestArticles.singleton()
        self.newsletter_instance = HomePageNewsletterSection.singleton()
        self.gallery_instance = HomePageGallerySection.singleton()
        self.footer_instance = FooterSettings.singleton()

    def get_context_data(self, **kwargs):
        '''
        Metoda pro vytvoření kontextových dat pro zobrazení domovské stránky.

        Metoda nejprve načítá kontext z nadřazené třídy,
        a následně přidává vlastní obsah pro vykreslení jednotlivých sekcí,
        voláním metody 'get_data' na každém modelu sekce.
        Metoda vrací upravený kontext.
        '''

        context = super().get_context_data(**kwargs)
        context.update({
            'hero_data': self.hero_instance.get_data(),
            'intro_data': self.intro_instance.get_data(),
            'featured_data': self.featured_instance.get_data(),
            'divider_data': self.divider_instance.get_data(),
            'latest_data': self.latest_instance.get_data(),
            'newsletter_data': self.newsletter_instance.get_data(),
            'gallery_data': self.gallery_instance.get_data(),
        })

        return context

    def get(self, request, *args, **kwargs):
        '''
        Metoda pro zobrazení domovské stránky.

        Metoda načte kontext a navrátí šablonu s daty pro domácí stránku.
        '''

        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

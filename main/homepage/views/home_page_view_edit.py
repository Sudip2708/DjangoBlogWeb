from django.shortcuts import render
from .home_page_view import HomePageView

from ..forms.hero_section_form import HeroSectionForm
from ..forms.intro_section_form import IntroSectionForm
from ..forms.featured_section_form import FeaturedArticlesForm
from ..forms.divider_section_form import DividerSectionForm
from ..forms.latest_section_form import LatestArticlesForm
from ..forms.newsletter_section_form import NewsletterSectionForm
from ..forms.gallery_section_form import GallerySectionForm
from ..forms.footer_section_form import FooterSettingsForm


class HomePageEditView(HomePageView):
    '''
    Pohled pro úpravu obsahu domovské stránky.

    Pohled dědí veškerá data z  HomePageView
    a přidává data pro úpravu obsahu prostřednictvím příslušných formulářů.
    '''

    template_name = '1_home/10__base__.html'

    def get_context_data(self, **kwargs):
        '''
        Metoda pro vytvoření kontextových dat pro zobrazení domovské stránky.

        Metoda nejprve načítá kontext z nadřazené třídy,
        a následně přidává vlastní obsah pro editaci jednotlivých sekcí,
        načtením formulářů pro jednotlivé sekce.
        Metoda vrací upravený kontext.
        '''

        # Zavolání metody rodičovské třídy pro získání kontextových dat
        context = super().get_context_data(**kwargs)

        # Vytvoření formulářů pro editaci obsahu
        hero_edit_form = HeroSectionForm(instance=self.hero_instance)
        intro_edit_form = IntroSectionForm(instance=self.intro_instance)
        featured_edit_form = FeaturedArticlesForm(instance=self.featured_instance)
        divider_edit_form = DividerSectionForm(instance=self.divider_instance)
        latest_edit_form = LatestArticlesForm(instance=self.latest_instance)
        newsletter_edit_form = NewsletterSectionForm(instance=self.newsletter_instance)
        gallery_edit_form = GallerySectionForm(instance=self.gallery_instance)
        footer_edit_form = FooterSettingsForm(instance=self.footer_instance)

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

        return context

    def get(self, request, *args, **kwargs):
        '''
        Metoda pro zobrazení domovské stránky.

        Metoda načte kontext a navrátí šablonu s daty pro domácí stránku.
        '''

        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)
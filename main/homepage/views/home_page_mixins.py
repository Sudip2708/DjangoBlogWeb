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

class HomePageViewMixin:
    '''
    Mixin pro získání dat domovské stránky.
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


class HomePageEditViewMixin:
    '''
    Mixin pro přidání formulářů pro úpravu obsahu domovské stránky do kontextu.
    '''

    def add_edit_forms_to_context(self, context):
        '''
        Metoda pro přidání formulářů pro úpravu obsahu domovské stránky do kontextu.

        :param context: Kontext pro zobrazení šablony.
        '''

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
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
    View for displaying the content of the home page.

    This view loads the data for individual sections of the page from their models
    and returns a template with the data for displaying the home page.
    '''

    template_name = '1_home/10__base__.html'

    def __init__(self):
        '''
        Method for basic class initialization.

        The method loads instances of the models of individual sections and creates attributes for them.
        Attributes are used both in this code and in the HomePageEditView view,
        which inherits from this view.
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
        Method for creating context data for displaying the home page.

        The method first loads the context from the parent class,
        and then adds custom content for rendering individual sections,
        by calling the 'get_data' method on each section model.
        The method returns the modified context.
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
        Method for displaying the home page.

        The method loads the context and returns a template with the data for the home page.
        '''

        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

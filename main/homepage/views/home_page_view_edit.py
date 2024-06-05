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
    View for editing the content of the home page.

    This view inherits all data from HomePageView
    and adds data for editing the content via the respective forms.
    '''

    template_name = '1_home/10__base__.html'

    def get_context_data(self, **kwargs):
        '''
        Method for creating context data for displaying the home page.

        The method first loads the context from the parent class,
        and then adds custom content for editing individual sections,
        by loading the forms for each section.
        The method returns the modified context.
        '''

        # Calling the method of the parent class to get context data
        context = super().get_context_data(**kwargs)

        # Creating forms for editing content
        hero_edit_form = HeroSectionForm(instance=self.hero_instance)
        intro_edit_form = IntroSectionForm(instance=self.intro_instance)
        featured_edit_form = FeaturedArticlesForm(instance=self.featured_instance)
        divider_edit_form = DividerSectionForm(instance=self.divider_instance)
        latest_edit_form = LatestArticlesForm(instance=self.latest_instance)
        newsletter_edit_form = NewsletterSectionForm(instance=self.newsletter_instance)
        gallery_edit_form = GallerySectionForm(instance=self.gallery_instance)
        footer_edit_form = FooterSettingsForm(instance=self.footer_instance)

        # Adding forms to the context
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
        Method for displaying the home page.

        The method loads the context and returns a template with the data for the home page.
        '''

        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

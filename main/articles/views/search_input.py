from django.views.generic import TemplateView

from common_data.base_view import BaseView

from ..forms.search_form import ArticleSearchForm


class SearchInputView(BaseView, TemplateView):
    '''
    View for displaying the search page (and for announcing search errors).

    This view handles the following URLs:
    - article-search-input: Page for entering search.
    - article-search-error: Page for announcing search errors.

    Attributes overridden from TemplateView:
    - template_name: Specifies the path to the template used for rendering the results.

    The view inherits from the base class TemplateView and its custom class BaseView
    and then creates content for rendering the search page
    and for rendering the page announcing an error in entering the search.
    '''

    template_name = '2_main/22__search__.html'

    def get_context_data(self, **kwargs):
        '''
        Method for passing the context needed to render the page.

        This method inherits the content from the BaseView class:
        - context['user']: User instance.
        - context['url_name']: URL name of the address from which the request came.
        - context['sidebar_search_form']: Search form (for the sidebar).
        - context['published_categories']: Published categories (for dropdown menu and sidebar).
        - context['footer']: Data for rendering the footer (already included on the homepage)
        - context['user_thumbnail']: Profile thumbnail (for logged-in and logged-out users).

        This method overrides this content (only in case of error):
        - context['sidebar_search_form']: Search form (for the sidebar).

        This method adds this content:
        - context['page_title']: Page title.
        - context['search_form']: Search form on the page.

        The method first loads the context of the parent class,
        and then checks if the request came from the search page,
        if so, it creates a title and an empty form for it.

        Then the method checks if the request came from the error announcement page,
        if so, it retrieves the forwarded data and then extracts
        the form with the error message and pre-filled data from it.
        It then passes it as context for rendering its own form
        and also overwrites the form received from BaseView,
        intended for searching from the sidebar.
        And then it creates and adds a title.

        The method returns the content needed to render the page.
        '''
        context = super().get_context_data(**kwargs)

        # Context for the search page
        if self.url_name == 'article-search-input':
            context['page_title'] = 'Search in Articles'
            context['search_form'] = ArticleSearchForm()

        # Context for the page with error display
        elif self.url_name == 'article-search-error':
            error_data = self.request.session.pop('search_error_data', None)
            if error_data:
                form_data = error_data['form_data']
                form = ArticleSearchForm(form_data)
                context['sidebar_search_form'] = form
                context['search_form'] = form
            context['page_title'] = 'Search in Articles - Error'

        return context

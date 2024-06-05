from django.views.generic import ListView
from django.shortcuts import redirect
from django.urls import reverse

from common_data.base_view import BaseView

from ..forms.search_form import ArticleSearchForm
from .common_data.get_paginate_by import get_paginate_by
from .search_data.get_search_parameters import get_search_parameters
from .search_data.get_queryset import get_queryset
from .search_data.get_context_data import get_context_data


class SearchView(BaseView, ListView):
    '''
    View for processing article searches.

    This view handles the following URLs:
    - article-search: Base address for entering and evaluating search parameters.
    - article-search-results: Page for displaying search results.
    - article-search-similar: Page for displaying similar articles for articles from the search results.
    - article-search-results-category: Page for displaying categories for the search result.
    - article-search-similar-category: Page for displaying categories for similar articles.

    The view inherits from the base class ListView and its custom class BaseView.

    Attributes overridden from ListView:
    - template_name: Specifies the path to the template used for rendering the results.
    - context_object_name: Name of the variable in the template context that will contain the resulting list of objects.

    Attributes inherited from BaseView:
    - self.user: User instance (either CustomUser or AnonymousUserWithSettings).
    - self.url_name: URL name of the address from which the request came.

    Attributes defined by this view:
    - self.search_parameters: Attribute containing a dictionary with query parameters.
    - self.article_ids: Attribute for article IDs based on the searched data.
    - self.page_title: Attribute for the page title.
    - self.page_title_mobile: Attribute for the page title for mobile devices.
    - self.display_text: Attribute for descriptive text informing about what was searched for.
    - self.info_text: Information text (displayed when no similar article is found).
    - self.category_items: Attribute for listing categories for search results.
    - self.current_category_tab: Attribute for the currently selected category tab.

    Methods defined in this view:
    - get: Method for retrieving form data to render the page.
    - get_queryset: Method for retrieving instances of articles and data needed to render the page.
    - get_paginate_by: Method for determining the number of articles per page when paginating search results.
    - get_context_data: Method for passing the context needed to render the page.
    '''

    template_name = '3_articles/30__base__.html'
    context_object_name = 'articles_results'

    def get(self, request, *args, **kwargs):
        '''
        Method for processing incoming requests.

        The method first checks by URL name whether it is a request from the article-search page,
        used for entering and evaluating search parameters.

        If so, it loads an instance of the form and performs a check of the entered data.
        If the data is correct, it calls a function to create a dictionary with search parameters,
        and redirects this dictionary to the article-search-results address,
        to obtain data needed to display search results.

        If the data is not valid, it redirects to the page for displaying errors in entry.

        If the get method receives pre-prepared data, it calls the get method of the parent class
        and passes the data for further processing.
        '''

        # Capturing user query
        if self.url_name == 'article-search':

            form = ArticleSearchForm(request.GET)
            if form.is_valid():

                # Creating dictionaries with search parameters and forwarding processed data
                search_parameters = get_search_parameters(form.cleaned_data)
                return redirect(reverse('article-search-results', kwargs={'query': search_parameters}))

            else:

                # Forwarding the form to the page for displaying entry errors
                request.session['search_error_data'] = {'form_data': form.data}
                return redirect(reverse('article-search-error'))

        else:

            # If it is a forwarding of processed data, the get method of the parent class is called
            return super().get(request, *args, **kwargs)

    def get_queryset(self):
        '''
        Method for retrieving instances of articles and data needed to render the page.

        This method calls the method with the same name stored in a separate file
        and returns its result.
        '''
        return get_queryset(self)

    def get_paginate_by(self, queryset):
        '''
        Method for determining the number of articles per page when paginating search results.

        This method calls the method with the same name stored in a separate file
        and returns its result.
        '''
        return get_paginate_by(self, queryset)

    def get_context_data(self, **kwargs):
        '''
        Method for passing the context needed to render the page.

        This method first loads the context of the parent class,
        and then calls the method with the same name stored in a separate file,
        passing it the context, and then returns its result.
        '''
        context = super().get_context_data(**kwargs)
        return get_context_data(self, context, **kwargs)

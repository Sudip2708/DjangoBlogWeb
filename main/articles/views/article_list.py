from django.views.generic import ListView

from common_data.base_view import BaseView

from .common_data.get_paginate_by import get_paginate_by
from .article_list_data.get_queryset import get_queryset
from .article_list_data.get_context_data import get_context_data


class ArticleListView(BaseView, ListView):
    '''
    View for displaying a list of articles.

    This view processes the following URLs:
    - article-list: Page displaying all published articles.
    - article-category-list: Page displaying all published articles categorized.
    - article-tag-list: Page displaying articles for a given tag.
    - article-tag-list-similar: Page displaying similar articles for a given tag.
    - article-tag-list-category: Page displaying categories for articles for a given tag.
    - article-tag-list-similar-category: Page displaying categories for similar articles for a given tag.

    The view inherits from the base class ListView and its custom class BaseView.

    Overridden attributes from ListView:
    - self.template_name: Specifies the path to the template used for rendering the results.
    - self.context_object_name: The name of the variable in the template context that will contain the resulting object list.

    Inherited attributes from BaseView:
    - self.user: User instance (either CustomUser or AnonymousUserWithSettings).
    - self.url_name: URL name of the address from which the request came.

    Attributes defined by this view:
    - self.page_title: Page title.
    - self.page_title_mobile: Attribute for page title for mobile devices.
    - self.page_subtitle: Page subtitle (displayed when navigation for categories is hidden).
    - self.info_text: Informational text (displayed when no similar article is found).
    - self.current_category: Instance of the currently selected category (only for categories).
    - self.category_tabs = List of categories for content self.article_ids (only for categories).

    Methods defined in this view:
    - get_queryset: Method for retrieving article instances and data needed for rendering the page.
    - get_paginate_by: Method for determining the number of articles per page when paginating search results.
    - get_context_data: Method for passing the context required for rendering the page.
    '''

    template_name = '3_articles/30__base__.html'
    context_object_name = 'articles_results'

    def get_queryset(self, *args, **kwargs):
        '''
        Method for retrieving article instances and data needed for rendering the page.

        This method calls the same-named method stored in a separate file
        and returns its result.
        '''
        return get_queryset(self, *args, **kwargs)

    def get_paginate_by(self, queryset):
        '''
        Method for determining the number of articles per page when paginating search results.

        This method calls the same-named method stored in a separate file
        and returns its result.
        '''
        return get_paginate_by(self, queryset)

    def get_context_data(self, **kwargs):
        '''
        Method for passing the context required for rendering the page.

        This method first loads the context of the parent class,
        and then calls the same-named method stored in a separate file,
        passing the context, and returns its result.
        '''
        context = super().get_context_data(**kwargs)
        return get_context_data(self, context, **kwargs)

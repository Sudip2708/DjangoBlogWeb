from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from common_data.base_view import BaseView

from .common_data.get_paginate_by import get_paginate_by
from .my_articles_data.get_queryset import get_queryset
from .my_articles_data.get_context_data import get_context_data


@method_decorator(login_required, name='dispatch')
class MyArticlesView(BaseView, ListView):
    '''
    View for the page displaying the user's own articles (only for logged-in users).

    This view processes the following URL:
    - my-articles: Page for articles authored by the user associated with the logged-in user.

    The page has the following tabs:
    - all: All articles sorted by creation date in descending order.
    - drafted: Drafted articles.
    - publish: Published articles (articles for the public).
    - archive: Archived articles.

    The view inherits from the base class ListView and its custom class BaseView.

    Attributes overridden from ListView:
    - self.template_name: Specifies the path to the template used for rendering the results.
    - self.context_object_name: Name of the variable in the template context that will contain the resulting list of objects.

    Attributes inherited from BaseView:
    - self.user: User instance (either CustomUser or AnonymousUserWithSettings).
    - self.url_name: URL name of the address from which the request came.

    Attributes defined by this view:
    - self.page_title: Page title.
    - self.page_title_mobile: Attribute for the page title for mobile devices.
    - self.current_tab: Attribute for the name of the currently displayed tab.

    Methods defined in this view:
    - get_queryset: Method for retrieving instances of articles and data needed to render the page.
    - get_paginate_by: Method for determining the number of articles per page when paginating search results.
    - get_context_data: Method for passing the context needed to render the page.
    '''

    template_name = '3_articles/30__base__.html'
    context_object_name = 'articles_results'

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

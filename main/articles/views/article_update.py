from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.urls import reverse

from .article_create import ArticleCreateView


@method_decorator(login_required, name='dispatch')
class ArticleUpdateView(ArticleCreateView, UpdateView):
    '''
    View for updating a created article (only for logged-in users).

    This view processes the following URL:
    - article-update: Page for updating a created article.

    The view inherits from the base class UpdateView and its custom class for creating articles ArticleCreateView.

    Attributes inherited from ArticleCreateView:
    - self.model: Specifies the model this view works with.
    - self.template_name: Specifies the path to the template used for rendering the results.
    - self.user: User instance (either CustomUser or AnonymousUserWithSettings).
    - self.url_name: URL name of the address from which the request came.

    Methods inherited from ArticleCreateView:
    - get_form_class: Method for returning the form based on the selected tab of the page.
    - form_valid: Method for adding author information (author instance) to the form.
    - get_success_url: Method for creating the redirect URL after successfully creating the article.

    Overridden methods from ArticleCreateView:
    - get_context_data: Method for creating the context.

    '''

    def get_context_data(self, **kwargs):
        '''
        Method for creating the context.

        Context inherited from ArticleCreateView:
        - context['user']: User instance.
        - context['url_name']: URL name of the address from which the request came.
        - context['sidebar_search_form']: Search form (for the sidebar).
        - context['published_categories']: Published categories (for the dropdown menu and sidebar).
        - context['footer']: Data for rendering the footer (already included on the home page)
        - context['user_thumbnail']: Profile thumbnail (for logged-in and logged-out users).

        Context created by this view:
        - context['tab_urls']: Reverse paths to individual tabs.
        - context['current_tab']: Current page tab.
        - context['title']: Page title.
        '''

        # Creating URLs for individual page tabs
        tab_urls = {
            'for_overview': reverse('article-update', kwargs={'slug': self.object.slug, 'current_tab': 'overview'}),
            'for_content': reverse('article-update', kwargs={'slug': self.object.slug, 'current_tab': 'content'}),
            'for_settings': reverse('article-update', kwargs={'slug': self.object.slug, 'current_tab': 'settings'}),
        }

        context = super().get_context_data(**kwargs)
        context['tab_urls'] = tab_urls
        context['title'] = 'Update Your Article'

        return context

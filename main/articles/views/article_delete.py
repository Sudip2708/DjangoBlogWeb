from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from common_data.base_view import BaseView

from ..models.article import Article


@method_decorator(login_required, name='dispatch')
class ArticleDeleteView(BaseView, DeleteView):
    '''
    View for deleting an article (only for authenticated users).

    The view processes the following URL:
    - article-delete: Page for confirming the deletion of an article.

    The view inherits from the base class DeleteView and its custom class BaseView.

    Overridden attributes from DeleteView:
    - self.model: Specifies the model this view works with.
    - self.template_name: Specifies the path to the template used for rendering the results.
    - self.success_url: Defines the URL to redirect to after successfully performing the operation.

    Inherited attributes from BaseView:
    - self.user: User instance (either CustomUser or AnonymousUserWithSettings).
    - self.url_name: URL name of the address from which the request came.

    Methods defined in this view:
    - get_context_data: Method that creates content for rendering the template.
    '''

    model = Article
    template_name = '5_create_article/55__confirm_delete__.html'
    success_url = reverse_lazy('my-articles', kwargs={'current_tab': 'all'})

    def get_context_data(self, **kwargs):
        '''
        Method to pass the context required for rendering the page.

        Context inherited from BaseView:
        - context['user']: User instance.
        - context['url_name']: URL name of the address from which the request came.
        - context['sidebar_search_form']: Search form (for the sidebar).
        - context['published_categories']: Published categories (for dropdown menu and sidebar).
        - context['footer']: Data for rendering the footer (included on the homepage)
        - context['user_thumbnail']: Profile thumbnail (for logged-in and logged-out users).

        Context created by this view:
        - context['article']: Article instance.
        '''
        context = super().get_context_data(**kwargs)
        context['article'] = self.get_object()
        return context

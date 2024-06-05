from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from common_data.base_view import BaseView

from ..models.article import Article
from .article_create_data.get_form_class import get_form_class
from .article_create_data.get_or_create_author import get_or_create_author
from .article_create_data.get_success_url import get_success_url
from .article_create_data.get_context_data import get_context_data


@method_decorator(login_required, name='dispatch')
class ArticleCreateView(BaseView, CreateView):
    '''
    View for creating an article (only for authenticated users).

    The view processes the following URL:
    - article-create: Page for creating a new article.

    The view inherits from the base class CreateView and its custom class BaseView.

    Overridden attributes from CreateView:
    - self.model: Specifies the model this view works with.
    - self.template_name: Specifies the path to the template used for rendering the results.

    Inherited attributes from BaseView:
    - self.user: User instance (either CustomUser or AnonymousUserWithSettings).
    - self.url_name: URL address from which the request came.

    Methods defined in this view:
    - get_form_class: Method that returns the form based on the selected tab of the page.
    - form_valid: Method that validates the form (+ adds the author instance).
    - get_success_url: Method that returns the redirect URL after successfully creating the article.
    - get_context_data: Method that returns the content for rendering the template.
    '''

    model = Article
    template_name = '5_create_article/50__base__.html'

    def get_form_class(self):
        '''
        Method to return the appropriate form (based on the page tab).

        The method calls the similarly named method stored in a separate file
        and returns its result.
        '''
        return get_form_class(self)

    def form_valid(self, form):
        '''
        Method for form validation (+ adds the author).

        The method calls the function to get or create and get the author instance.
        Then the method calls the validation method of the parent class.
        '''
        form.instance.author = get_or_create_author(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        '''
        Method to create the return address (after successfully saving the form).

        The method calls the similarly named method stored in a separate file
        and returns its result.
        '''
        return get_success_url(self)

    def get_context_data(self, **kwargs):
        '''
        Method to pass the context required for rendering the page.

        The method first loads the context of the parent class,
        and then calls the similarly named method stored in a separate file,
        passes the context to it, and returns its result.
        '''
        context = super().get_context_data(**kwargs)
        return get_context_data(self, context, **kwargs)

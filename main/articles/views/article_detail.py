from django.views.generic import DetailView
from django.shortcuts import redirect, reverse

from common_data.base_view import BaseView

from ..models.article import Article
from ..models.article_view import ArticleView
from ..forms.comment_form import ArticleCommentForm


class ArticleDetailView(BaseView, DetailView):
    '''
    View for displaying a single article page.

    This view processes the following URL:
    - article-detail: Page displaying a selected article.

    The view inherits from the base class DetailView and its custom class BaseView.

    Overridden attributes from DetailView:
    - self.template_name: Specifies the path to the template used for rendering the results.
    - self.context_object_name: The name of the variable in the template context that will contain the resulting object.

    Inherited attributes from BaseView:
    - self.user: User instance (either CustomUser or AnonymousUserWithSettings).
    - self.url_name: URL name of the address from which the request came.

    Methods defined in this view:
    - get_object: Method for retrieving the object (article instance) and recording its view.
    - handle_comment_form: Method for processing the form for commenting on the article.
    - get_context_data: Method that returns content for rendering the template.
    '''
    model = Article
    template_name = '4_article/40__base__.html'
    context_object_name = 'article'

    def get_object(self):
        '''
        Method for retrieving the object (article instance) and recording its view.

        First, it retrieves the article instance from the parent class.
        Then, it calls the record_view method of the ArticleView class to record the view.
        In addition to the article instance and the author, it also passes the IP address obtained from the 'META' dictionary.
        The method returns the article instance.
        '''
        obj = super().get_object()
        ArticleView.record_view(obj, self.request.user, self.request.META.get('REMOTE_ADDR'))
        return obj

    def post(self, request, *args, **kwargs):
        '''
        Method for processing the form for commenting on the article.

        First, it loads the form for commenting on the article, and if the data is valid,
        it adds the user instance and the article instance to the form and saves the data to the database.
        After successfully saving the comment, it redirects the user to the article page.
        '''
        form = ArticleCommentForm(request.POST)

        if form.is_valid():
            article = self.get_object()
            form.instance.user = request.user
            form.instance.article = article
            form.save()

            return redirect(reverse("article-detail", kwargs={'slug': article.slug}))

        else:
            return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        '''
        Method for passing the context required for rendering the page.

        Context inherited from BaseView:
        - context['user']: User instance.
        - context['url_name']: URL name of the address from which the request came.
        - context['sidebar_search_form']: Search form (for the sidebar).
        - context['published_categories']: Published categories (for dropdown menu and sidebar).
        - context['footer']: Data for rendering the footer (included on the homepage)
        - context['user_thumbnail']: Profile thumbnail (for logged-in and logged-out users).

        Context created by this view:
        - context['form']: Form for leaving a comment on the article.
        '''
        context = super().get_context_data(**kwargs)

        context['form'] = ArticleCommentForm()
        return context

from django.views.generic import View
from django.urls import resolve

from articles.forms.search_form import ArticleSearchForm
from articles.models.article_category import ArticleCategory
from homepage.models.footer_section import FooterSettings


class BaseView(View):
    '''
    Definition of the base view class from which all other view classes inherit.

    This class first creates attributes in the dispatch method upon receiving a request:
    - self.user: User instance.
    - self.url_name: URL name of the address from which the request came.

    It then adds context in the get_context_data method:
    - context['user']: User instance.
    - context['url_name']: URL name of the address from which the request came.
    - context['sidebar_search_form']: Search form (for the sidebar).
    - context['published_categories']: Published categories (for dropdown menu and sidebar).
    - context['footer']: Data for rendering the footer (already included on the home page).
    - context['user_thumbnail']: Profile picture thumbnail (for logged-in and logged-out users).
    '''

    def dispatch(self, request, *args, **kwargs):
        '''
        This method defines basic attributes shared by all other classes that inherit from this class.

        Attributes defined by this method:
        - self.user: User instance (either CustomUser or AnonymousUserWithSettings).
        - self.url_name: URL name of the address from which the request came.
        - self.default_profile_picture: URL path to the default image for logged-out users.

        The method then calls the dispatch() of the parent class.
        '''

        self.user = request.user
        self.url_name = resolve(self.request.path_info).url_name
        self.default_profile_picture = request.build_absolute_uri('/media/images/profile_pictures/default.jpg')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        '''
        This method defines basic context shared by all other classes that inherit from this class.

        Context defined by this method:
        - context['user']: User instance.
        - context['url_name']: URL name of the address from which the request came.
        - context['sidebar_search_form']: Search form (for the sidebar).
        - context['published_categories']: Published categories (for dropdown menu and sidebar).
        - context['footer']: Data for rendering the footer (already included on the home page).
        - context['user_thumbnail']: Profile picture thumbnail (for logged-in and logged-out users).

        The method first loads the context from the parent class
        and then returns it, along with adding its own values.
        '''

        context = super().get_context_data(**kwargs)

        context['user'] = self.user
        context['url_name'] = self.url_name
        context['sidebar_search_form'] = ArticleSearchForm()
        context['published_categories'] = ArticleCategory.objects.exclude(id=1)
        context['footer'] = FooterSettings.singleton().get_data()
        if self.user.is_authenticated:
            context['user_thumbnail'] = self.user.profile_picture_thumbnail.url
        else:
            context['user_thumbnail'] = self.default_profile_picture

        return context

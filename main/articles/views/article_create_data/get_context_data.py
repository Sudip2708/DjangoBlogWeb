from django.urls import reverse

from taggit.models import Tag


def get_context_data(self, context, **kwargs):
    '''
    Method for creating context.

    Context inherited from BaseView:
    - context['user']: User instance.
    - context['url_name']: URL name of the address from which the request came.
    - context['sidebar_search_form']: Search form (for the sidebar).
    - context['published_categories']: Published categories (for dropdown menu and sidebar).
    - context['footer']: Data for footer rendering (already included on the home page)
    - context['user_thumbnail']: Profile thumbnail (for logged-in and non-logged-in users).

    Context created by this view:
    - context['tab_urls']: Reverse paths to individual tabs.
    - context['current_tab']: Current page tab.
    - context['title']: Page title.
    - context['tags_name_str']: String of tags for automatic tag completion
        (used in Tagify script and created only for the settings section).
    '''

    # Creating URL addresses for individual page tabs
    tab_urls = {
        'for_overview': reverse('article-create', kwargs={'current_tab': 'overview'}),
        'for_content': reverse('article-create', kwargs={'current_tab': 'content'}),
        'for_settings': reverse('article-create', kwargs={'current_tab': 'settings'}),
    }

    # Creating a list of existing tags and converting it to a string.
    all_tags = list(Tag.objects.values_list('name', flat=True))
    tags_name_str = ','.join(all_tags)

    # Creating a variable for the current tab
    current_tab = self.kwargs.get('current_tab')

    context['tab_urls'] = tab_urls
    context['current_tab'] = current_tab
    context['title'] = 'Create Your Article'
    if current_tab == 'settings':
        context['tags_name_str'] = tags_name_str

    return context

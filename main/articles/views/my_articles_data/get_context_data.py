def get_context_data(self, context, **kwargs):
    '''
    Method for adding necessary content to render the page.

    This method is intended for the following URL:
    - my-articles: Page for articles by the author associated with the user.

    The method inherits the following content from the BaseView class:
    - context['user']: User instance.
    - context['url_name']: URL name of the address from which the request came.
    - context['sidebar_search_form']: Search form (for the sidebar).
    - context['published_categories']: Published categories (for the dropdown menu and sidebar).
    - context['footer']: Data for rendering the footer (already included on the home page).
    - context['user_thumbnail']: Thumbnail of the profile picture (for logged-in and logged-out users).

    The method creates and adds the following content:
    - context['page_title']: Page title.
    - context['mobile_page_title']: Page title for mobile devices.
    - context['current_tab']: Name of the currently selected tab.
    '''

    context['page_title'] = 'My Articles'
    context['page_title_mobile'] = 'My Articles'
    context['current_tab'] = self.current_tab

    return context

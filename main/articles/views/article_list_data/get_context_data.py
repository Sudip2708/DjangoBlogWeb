def get_context_data(self, context, **kwargs):
    '''
    Method for adding content necessary for rendering the page.

    This method is intended for the following URLs:
    - article-list: Page displaying all published articles.
    - article-category-list: Page displaying all published articles sorted into categories.
    - article-tag-list: Page for displaying articles for a specific tag.
    - article-tag-list-similar: Page for displaying similar articles for a specific tag.
    - article-tag-list-category: Page for displaying categories for articles for a specific tag.
    - article-tag-list-similar-category: Page for displaying categories for similar articles for a specific tag.

    The method inherits the following content from the BaseView class:
    - context['user']: User instance.
    - context['url_name']: URL name of the address from which the request came.
    - context['sidebar_search_form']: Search form (for the sidebar).
    - context['published_categories']: Published categories (for dropdown menu and sidebar).
    - context['footer']: Data for rendering the footer (included on the home page)
    - context['user_thumbnail']: Profile picture thumbnail (for logged-in and logged-out users).

    The method adds combinations of these contents:
    - context['page_title']: Page title.
    - context['mobile_page_title']: Page title for mobile devices (only for all articles and categories).
    - context['page_subtitle']: Subtitle (if categories are not displayed).
    - context['info_text']: Informational text about a possible lack of any results (for similar articles).
    - context['current_category']: Instance of the currently selected category.
    - context['category_tabs']: Category instances for the given content.
    - context['current_tag']: Instance of the currently selected tag.
    '''

    # Context for all pages
    context['page_title'] = self.page_title

    # Context for the page with all articles
    if self.url_name == 'article-list':
        context['page_title_mobile'] = self.page_title_mobile
        if self.user.settings.get('show_category_navigation'):
            context['current_category'] = self.current_category
            context['category_tabs'] = self.category_tabs
        else:
            context['page_subtitle'] = self.page_subtitle

    # Context for the page with categories
    elif self.url_name == 'article-category-list':
        context['page_title_mobile'] = self.page_title_mobile
        context['current_category'] = self.current_category
        if self.user.settings.get('show_category_navigation'):
            context['category_tabs'] = self.category_tabs
        else:
            context['page_subtitle'] = self.page_subtitle

    # If we are on the page with similar articles based on a tag
    elif self.url_name.startswith('article-tag'):
        context['current_tag'] = self.current_tag
        if not self.article_ids:
            context['info_text'] = self.info_text
        if not self.user.settings.get('show_tab_for_similar'):
            context['page_subtitle'] = self.page_subtitle
        if self.url_name.endswith('category'):
            context['current_category'] = self.current_category
            context['category_tabs'] = self.category_tabs

    return context

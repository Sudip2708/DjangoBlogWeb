def get_context_data(self, context, **kwargs):
    '''
    Method for adding content necessary for rendering the page.

    The method is intended for the following URLs:
    - article-search: Base address used for entering and evaluating search parameters.
    - article-search-results: Page for displaying search results.
    - article-search-similar: Page for displaying similar articles for articles from the search results.
    - article-search-results-category: Page for displaying categories for the search result.
    - article-search-similar-category: Page for displaying categories for similar articles.

    The method inherits the following content from the BaseView class:
    - context['user']: User instance.
    - context['url_name']: URL name of the address from which the request came.
    - context['sidebar_search_form']: Search form (for the sidebar).
    - context['published_categories']: Published categories (for dropdown menu and sidebar).
    - context['footer']: Data for rendering the footer (already included on the homepage)
    - context['user_thumbnail']: Profile picture thumbnail (for logged-in and logged-out users).

    The method adds the following combinations of this content:
    - context['query']: Dictionary with search parameters.
    - context['page_title']: Page title.
    - context['page_title_mobile']: Page title for mobile devices.
    - context['display_text']: Description of the search.
    - context['info_text']: Informational text about a possible failure to find any results (for similar articles).
    - context['current_category']: Currently selected category instance.
    - context['category_tabs']: Category instances for the given content.
    '''

    if self.url_name == 'article-search-error':
        return context

    # Context for all pages
    context['query'] = self.search_parameters
    context['page_title'] = self.page_title
    context['page_title_mobile'] = self.page_title_mobile
    context['display_text'] = self.display_text

    # Context for the page with similar articles
    if not self.article_ids:
        context['info_text'] = self.info_text

    # Context for the page with categories
    if self.url_name.endswith('category'):
        context['category_tabs'] = self.category_tabs
        context['current_category'] = self.current_category

    # Returning context
    return context

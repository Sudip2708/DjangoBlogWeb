from .get_queryset_data.get_queryset_for_articles import get_queryset_for_articles
from .get_queryset_data.get_queryset_for_categories import get_queryset_for_categories
from .get_queryset_data.get_queryset_for_tags import get_queryset_for_tags


def get_queryset(self, *args, **kwargs):
    '''
    Method for obtaining the articles displayed on the page.

    This method is intended for the following URLs:
    - article-list: Page displaying all published articles.
    - article-category-list: Page displaying all published articles sorted into categories.
    - article-tag-list: Page for displaying articles for a specific tag.
    - article-tag-list-similar: Page for displaying similar articles for a specific tag.
    - article-tag-list-category: Page for displaying categories for articles for a specific tag.
    - article-tag-list-similar-category: Page for displaying categories for similar articles for a specific tag.

    Attributes added or modified by this method:
    - self.page_title: Page title.
    - self.page_title_mobile: Page title for mobile devices.
    - self.page_subtitle: Subtitle (displayed when category navigation is hidden).
    - self.info_text: Informational text (displayed when no similar articles are found).
    - self.current_category: Instance of the currently selected category (only for categories).
    - self.category_tabs: List of categories for the content in self.article_ids (only for categories).

    In this code, the method determines from which address the request came
    and then calls the appropriate method to process the request.

    The method returns instances of articles intended to be displayed on the page.
    '''

    # Configuration for the page displaying all articles
    if self.url_name == 'article-list':
        queryset = get_queryset_for_articles(self)

    # Configuration for pages displaying content for a specific category
    elif self.url_name == 'article-category-list':
        queryset = get_queryset_for_categories(self)

    # Configuration for pages displaying content for a specific tag
    elif self.url_name.startswith('article-tag'):
        queryset = get_queryset_for_tags(self)

    return queryset

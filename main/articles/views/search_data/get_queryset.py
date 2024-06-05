import ast

from ...models.article import Article
from ..common_data.get_similar_data import get_similar_data
from ..common_data.get_category_data import get_category_data
from .get_article_ids import get_article_ids


def get_queryset(self):
    '''
    Method for obtaining content based on the specified search.

    The method is intended for the following URLs:
    - article-search-results: Page for displaying search results.
    - article-search-similar: Page for displaying similar articles for articles from the search results.
    - article-search-results-category: Page for displaying categories for the search result.
    - article-search-similar-category: Page for displaying categories for similar articles.

    Attributes added or modified by this method:
    - self.search_parameters: Attribute containing a dictionary with query parameters.
    - self.article_ids: Attribute for article IDs based on the searched data.
    - self.page_title: Attribute for page title.
    - self.page_title_mobile: Page title for mobile devices.
    - self.display_text: Attribute for descriptive text, informing about what was searched.
    - self.info_text: Informational text (displayed when no similar article is found).
    - self.category_items: Attribute for listing categories for the search result.
    - self.current_category_tab: Attribute for the currently selected category tab.

    The method first loads the search parameters and creates the self.search_parameters attribute for them.

    Then it calls a function to search for content based on the search parameters,
    which returns content for the self.article_ids and self.display_text attributes.

    After that, it creates a title for mobile devices.

    The method then verifies if the request came from the address for displaying search results for search parameters
    (url name starts with the string 'article-search-results')
    and if yes, it creates content for the self.page_title attribute.

    Next, the method checks if the request came from the address for displaying similar articles
    (url name starts with the string 'article-search-similar')
    and if yes, a method is called to search for articles based on the self.article_ids attribute,
    which have at least one matching tag and are not included in self.article_ids.
    And then it overrides this attribute with the new values.

    Furthermore, the method checks if the request came from the address for displaying categories
    (the end part of the address name contains the string 'category').
    If yes, it calls a method to get a list of categories
    and content for the currently displayed category: self.article_ids, self.category_items, and self.current_category_tab.

    Finally, the method checks if the newly obtained content for self.article_ids
    contains at least one record, and if not, it creates the self.info_text attribute.

    Finally, the method searches for and returns instances of articles according to the content of the self.article_ids attribute.
    (Articles are sorted from newest to oldest.)
    '''

    # Setup for error display page
    if self.url_name == 'article-search-error':
        return Article.objects.none()

    # Getting search parameters
    self.search_parameters = ast.literal_eval(self.kwargs.get('query'))

    # Getting article IDs and descriptive text based on the provided parameters
    self.article_ids, self.display_text = get_article_ids(self.search_parameters)

    # Setting the title displayed on mobile devices
    self.page_title_mobile = 'Search results'

    # Creating the page title
    if self.url_name.startswith('article-search-results'):
        self.page_title = 'Search results for Articles'

    # Getting article IDs and title for the page with similar articles based on tags
    if self.url_name.startswith('article-search-similar'):
        get_similar_data(self)
        self.page_title = 'Similar Articles for Search Result'

    # Getting article IDs for pages displaying categories
    if self.url_name.endswith('category'):
        get_category_data(self)

    # Creating a notice if no article is found
    if not self.article_ids:
        self.info_text = 'There are no articles for this request.'

    # Creating and returning a queryset of selected articles
    queryset = Article.objects.filter(id__in=self.article_ids)
    return queryset

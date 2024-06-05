from ....models.article import Article
from ....models.article_category import ArticleCategory


def get_queryset_for_articles(self):
    '''
    Method to create a list of articles for the page displaying all articles.

    This method is intended for the following URLs:
    - article-list: Page showing all published articles.

    Attributes added or modified by this method:
    - self.category_tabs: List of all published categories.
    - self.current_category: Data for the current tab.
    - self.page_title: Page title.
    - self.page_title_mobile: Page title for mobile devices.
    - self.page_subtitle: Subtitle for the page (shown when category navigation is hidden).

    The method first checks whether the user has enabled category navigation.
    If yes, it creates attributes self.category_tabs, self.current_category, self.page_title, and self.page_title_mobile.
    If not, it creates attributes self.page_title, self.page_title_mobile, self.page_subtitle.

    The method retrieves and returns all published articles.
    (Articles are sorted from newest to oldest.)
    '''

    # Creating values for the page with category navigation enabled
    if self.user.settings.get('show_category_navigation'):
        self.category_tabs = ArticleCategory.objects.exclude(id=1)
        self.current_category = {'id': 0, 'slug': 'all', 'title': 'All'}
        self.page_title = 'Article Categories'
        self.page_title_mobile = 'All Articles'

    # Creating values for the page without category navigation enabled
    else:
        self.page_title = self.page_title_mobile = 'All Articles'
        self.page_subtitle = 'To see tab for categories click on Show Category in navbar.'

    # Creating and returning instances of articles
    queryset = Article.objects.filter(status='publish') \
                              .order_by('-created')
    return queryset

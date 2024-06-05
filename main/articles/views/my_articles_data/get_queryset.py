from ...models.article import Article
from ...models.article_author import ArticleAuthor


def get_queryset(self):
    '''
    Method for retrieving articles displayed on the page.

    This method is intended for the following URL:
    - my-articles: Page for articles by the author associated with the user.

    The page has the following tabs:
    - all: All articles sorted by creation date in descending order.
    - drafted: Drafted articles.
    - publish: Published articles (articles for the public).
    - archive: Archived articles.

    Attributes added or modified by this method:
    - self.page_title: Page title.
    - self.page_title_mobile: Attribute for the page title for mobile devices.
    - self.current_tab: Attribute for the name of the currently displayed tab.

    This method determines the originating tab from the request's address
    and then creates content for displaying articles of the corresponding tab.

    The method returns instances of articles intended for display on the page.
    '''

    # Retrieving the current tab from the page address
    self.current_tab = self.kwargs.get('current_tab')

    # Retrieving the author
    author = ArticleAuthor.objects.get(id=self.user.linked_author.id)

    # Retrieving articles for the Drafted tab
    if self.current_tab == 'drafted':
        queryset = Article.objects.filter(author=author, status='drafted') \
                                  .order_by('-created')

    # Retrieving articles for the Publish tab
    elif self.current_tab == 'publish':
        queryset = Article.objects.filter(author=author, status='publish') \
                                  .order_by('-created')

    # Retrieving articles for the Archive tab
    elif self.current_tab == 'archive':
        queryset = Article.objects.filter(author=author, status='archive') \
                                  .order_by('-created')

    # Retrieving articles for the All tab
    else:
        queryset = Article.objects.filter(author=author) \
                                  .order_by('-created')

    return queryset

from ...models.article import Article
from ...models.article_category import ArticleCategory


def get_category_data(self):
    '''
    Method for creating a list of articles for a specific category.

    This method is used in the following files:
    - articles/views/article_list_data/get_queryset_data/get_queryset_for_tags.py
    - articles/views/search_data/get_queryset.py

    Attributes added or modified by this method:
    - self.article_ids: IDs of articles containing the selected tag.
    - self.current_category: Instance of the currently selected category.
    - self.category_tabs: Instances of categories for self.article_ids.
    - self.page_title: Page title.

    The method first retrieves the slug of the currently selected category from the URL.

    Then it retrieves a set of category IDs based on the article IDs,
    and then retrieves instances of categories based on their IDs,
    and adds them to the self.category_tabs attribute.

    Next, based on the value for current_category, it checks if any of the categories contain the same slug
    as the one specified in this variable. If there is a match, it loads this category into the self.current_category attribute.
    In case of no match (current_category value may also contain the string 'first'
    used in the case of the first display of category navigation,
    when we want to get a list for the first tab, but we don't know which one it will be yet),
    it sets the first category in the list as the selected one.

    Finally, it filters from the self.article_ids attribute those articles that belong to the selected category
    and updates the content of the attribute with them.

    Finally, the method creates the self.page_title attribute for the page title.
    '''

    # Retrieving the current category
    current_category = self.kwargs['category_slug']

    # Getting a set of category IDs based on article IDs
    article_category_ids = Article.objects \
        .filter(id__in=self.article_ids) \
        .values_list('category_id', flat=True) \
        .distinct()

    # Getting a set of category instances based on category IDs
    self.category_tabs = ArticleCategory.objects \
        .filter(id__in=article_category_ids) \
        .distinct()

    # Getting the category to be displayed after loading the page
    self.current_category = next(
        (category for category in self.category_tabs if category.slug == current_category),
        self.category_tabs.first()
    )

    # Getting the list of article IDs with status "publish" and linked to the selected category
    self.article_ids = Article.objects \
        .filter(id__in=self.article_ids, category=self.current_category) \
        .values_list('id', flat=True)

    # Creating the page title
    self.page_title = f'Category for {self.page_title}'

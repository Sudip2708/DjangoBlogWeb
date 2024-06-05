from django.shortcuts import get_object_or_404

from ....models.article import Article
from ....models.article_category import ArticleCategory


def get_queryset_for_categories(self):
    '''
    Method to create a list of articles for the selected category.

    This method is intended for the following URL:
    - article-category-list: Page showing all published articles sorted into categories.

    Attributes added or modified by this method:
    - self.current_category: Currently selected category.
    - self.category_tabs: List of all published categories.
    - self.page_title: Page title.
    - self.page_title_mobile: Page title for mobile devices.
    - self.page_subtitle: Subtitle for the page (shown when category navigation is hidden).

    The method first retrieves the currently selected category slug from the URL,
    then gets its instance and saves it as the attribute self.current_category.
    (If no category is found for the given slug, a 404 exception is raised.)

    The method then checks whether the user has enabled category navigation.
    If yes, it creates attributes self.category_tabs, self.page_title, and self.page_title_mobile.
    If not, it creates attributes self.page_title, self.page_title_mobile, and self.page_subtitle.

    The method retrieves and returns all published articles for the specified category.
    (Articles are sorted from newest to oldest.)
    '''

    # Retrieving the current category
    current_category_slug = self.kwargs['category_slug']
    self.current_category = get_object_or_404(ArticleCategory, slug=current_category_slug)

    # Creating values for the page with category navigation enabled
    if self.user.settings.get('show_category_navigation'):
        self.category_tabs = ArticleCategory.objects.exclude(id=1)
        self.page_title = 'Article Categories'
        self.page_title_mobile = f'Category: {self.current_category.name}'

    # Creating values for the page without category navigation enabled
    else:
        self.page_title = f'Articles for Category: {self.current_category.name}'
        self.page_title_mobile = f'Category: {self.current_category.name}'
        self.page_subtitle = 'To see tab for categories click on Show Category in navbar.'

    # Creating and returning instances of articles
    queryset = Article.objects.filter(category=self.current_category, status='publish') \
                              .order_by('-created')
    return queryset

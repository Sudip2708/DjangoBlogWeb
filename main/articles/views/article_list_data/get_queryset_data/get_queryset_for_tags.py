from ....models.article import Article
from ...common_data.get_similar_data import get_similar_data
from ...common_data.get_category_data import get_category_data
from .get_tag_data import get_tag_data


def get_queryset_for_tags(self):
    '''
    Method to create a list of articles for a specific tag and for similar articles.

    This method is intended for the following URLs:
    - article-tag-list: Page for displaying articles for a given tag.
    - article-tag-list-similar: Page for displaying similar articles for a given tag.
    - article-tag-list-category: Page for displaying categories for articles for a given tag.
    - article-tag-list-similar-category: Page for displaying categories for similar articles for a given tag.

    Attributes added or modified by this method:
    - self.page_title: Page title.
    - self.page_subtitle: Subtitle for the page (shown when category navigation is hidden).
    - self.info_text: Informational text (displayed when no similar articles are found).
    - self.current_category: Instance of the currently selected category (only for categories).
    - self.category_tabs = List of categories for the content in self.article_ids (only for categories).

    The method first calls the get_tag_data(self) method, which retrieves the tag slug from the URL,
    and then creates values for the attributes:
    self.current_tag, self.article_ids, self.page_title, and self.page_subtitle.

    Then, the method checks whether the request came from the page for displaying similar articles.
    If yes, it calls the get_similar_data(self) method, which retrieves a list of similar articles
    that have at least one tag in common and are not included in the original list,
    and then creates values for the attributes self.article_ids and self.page_title.
    Finally, the method checks whether the newly created content for self.article_ids
    contains at least one record, and if not, it creates content for the self.info_text attribute.

    After that, the method checks whether the request came from a page displaying category navigation.
    If yes, it calls the get_category_data(self) method, which, based on the currently selected category,
    creates values for the attributes:
    self.article_ids, self.current_category, self.category_tabs, and self.page_title.

    Finally, the method retrieves instances for the selected articles and returns them as a queryset.
    '''

    # Settings for the page with tags (article-tag-list)
    get_tag_data(self)

    # Settings for the page with similar articles (article-tag-list-similar)
    if self.url_name.startswith('article-tag-list-similar'):
        get_similar_data(self)
        self.page_title = f'Similar Articles for Tag: {self.current_tag.name}'
        if not self.article_ids:
            self.info_text = 'There are no other articles with tags that have articles in the result.'

    # Settings for displaying categories (article-tag-list-category, article-tag-list-similar-category)
    if self.url_name.endswith('category'):
        get_category_data(self)

    # Creating and returning a list of article instances
    queryset = Article.objects.filter(id__in=self.article_ids)
    return queryset

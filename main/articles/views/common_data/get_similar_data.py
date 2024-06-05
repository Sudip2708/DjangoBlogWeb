from taggit.models import Tag

from ...models.article import Article


def get_similar_data(self):
    '''
    Method to create attributes for displaying similar articles.

    This method is used in the following files:
    - articles/views/article_list_data/get_queryset_data/get_queryset_for_tags.py
    - articles/views/search_data/get_queryset.py

    Attributes added or modified by this method:
    - self.article_ids: IDs of articles containing the selected tag.
    - self.info_text: Informational text (displayed when no similar article is found).

    The method first retrieves a set of tag IDs for articles contained in self.article_ids.

    Then, for this set of tag IDs, it retrieves a set of article IDs that contain at least one tag from the tag set,
    are not part of self.article_ids, and have a status of 'publish'.
    It then overwrites the original content of self.article_ids with these new data.
    '''
    # Retrieving tag IDs for articles from the query
    unique_tag_ids = Tag.objects \
                        .filter(article__id__in=self.article_ids) \
                        .values_list('id', flat=True) \
                        .distinct()

    # Retrieving IDs of articles containing at least one tag, not part of the original list, and with a status of publish
    self.article_ids = Article.objects \
                            .filter(status='publish', tags__id__in=unique_tag_ids) \
                            .exclude(id__in=self.article_ids) \
                            .values_list('id', flat=True) \
                            .distinct()

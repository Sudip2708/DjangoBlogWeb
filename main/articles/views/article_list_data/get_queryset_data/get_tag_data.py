from django.shortcuts import get_object_or_404
from taggit.models import Tag

from ....models.article import Article


def get_tag_data(self):
    '''
    Method for creating a list of articles for a specific tag.

    Attributes added or modified by this method:
    - self.current_tag: Currently selected tag.
    - self.article_ids: IDs of articles containing the selected tag.
    - self.page_title: Page title.
    - self.page_subtitle: Subtitle for the page (shown when navigation for similar articles is hidden).

    The method first retrieves the currently selected tag slug from the URL,
    and then obtains its instance and saves it as the self.current_tag attribute.
    (If no category is found for the given slug, a 404 exception is raised.)

    Then the method retrieves a set of article IDs containing the given tag,
    and saves it as the self.article_ids attribute.

    Next, it creates the self.page_title attribute for the page title,
    and if the navigation for similar articles is not enabled,
    it also creates the self.page_subtitle attribute for the descriptive text.
    '''

    # Retrieving the currently selected tag
    current_tag_slug = self.kwargs.get('tag_slug')
    self.current_tag = get_object_or_404(Tag, slug=current_tag_slug)

    # Retrieving article IDs for the given tag
    self.article_ids = Article.objects \
                              .filter(tags=self.current_tag, status='publish') \
                              .values_list('id', flat=True)

    # Creating the page title
    self.page_title = f'Articles with Tag: {self.current_tag.name}'

    # Creating the page subtitle if the navigation for similar articles is not enabled
    if not self.user.settings.get('show_tab_for_similar'):
        self.page_subtitle = 'To see tab for similar articles click on Show Similar in navbar.'

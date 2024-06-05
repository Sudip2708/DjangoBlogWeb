from ...forms.article_overview_form import ArticleOverviewForm
from ...forms.article_content_form import ArticleContentForm
from ...forms.article_settings_form import ArticleSettingsForm


def get_form_class(self):
    '''
    Method to return the appropriate form class (based on the page tab).

    The method creates the current_tab attribute for the currently selected tab
    and then returns the corresponding class for creating the form for this tab.
    '''

    self.current_tab = self.kwargs.get('current_tab')

    if self.current_tab == 'overview':
        form_class = ArticleOverviewForm

    elif self.current_tab == 'content':
        form_class = ArticleContentForm

    elif self.current_tab == 'settings':
        form_class = ArticleSettingsForm

    return form_class

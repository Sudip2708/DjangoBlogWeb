from ...forms.article_overview_form import ArticleOverviewForm
from ...forms.article_content_form import ArticleContentForm
from ...forms.article_settings_form import ArticleSettingsForm

def get_form_class(self):
    '''
    Metoda pro navrácení příslušného formuláře (dle záložky stránky).

    Metoda vytváří atribut current_tab pro aktuálně vybranou záložku
    a následně pro tuto záložku vrací příslušnou třídu pro vytvoření formuláře.
    '''

    self.current_tab = self.kwargs.get('current_tab')

    if self.current_tab == 'overview':
        form_class = ArticleOverviewForm

    elif self.current_tab == 'content':
        form_class = ArticleContentForm

    elif self.current_tab == 'settings':
        form_class = ArticleSettingsForm

    return form_class

from django import forms
from tinymce.widgets import TinyMCE

from articles.models.article import Article

from ..models.latest_section import HomePageLatestArticles


class LatestArticlesForm(forms.ModelForm):
    '''
    Form for setting up the Latest Articles section on the homepage.

    This form class is associated with the EditLatestArticlesSection view.

    The form defines the following fields:
    - display_latest_section: Visibility of the section.
    - latest_title: Section title.
    - latest_description: Descriptive text for the section.
    - latest_article_1: First selected article.
    - latest_article_2: Second selected article.
    - latest_article_3: Third selected article.
    '''

    class Meta:
        '''
        The Meta class is a special inner class for configuring the form.

        The Meta class provides metadata and configuration for the main class,
        and here it defines the following attributes:
        - model: Specifies the model on which the form is based.
        - fields: Defines the fields to be included in the form.
        - widgets: Allows specifying custom widgets for individual form fields.

        Widgets used in this code:
        - forms.CheckboxInput: Field for boolean checkbox values.
        - TinyMCE: Field for entering text using the TinyMCE module.
        - forms.Select: Field for selecting from preset values.
        '''

        model = HomePageLatestArticles
        fields = ['display_latest_section', 'latest_title', 'latest_description',
                  'latest_article_1', 'latest_article_2', 'latest_article_3']
        widgets = {
            'display_latest_section': forms.CheckboxInput(),
            'latest_title': TinyMCE(),
            'latest_description': TinyMCE(),
            'latest_article_1': forms.Select(),
            'latest_article_2': forms.Select(),
            'latest_article_3': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        '''
        Initialization method of the form.

        The method first calls the initialization of the superclass and then creates the content
        for the selection menu for selecting previous and next articles.

        The method filters all published articles and sorts them from newest to oldest,
        and adds this list as a queryset to create the value selection menu
        for the 'featured_article' fields 1 - 3.
        '''

        super().__init__(*args, **kwargs)

        published_articles = Article.objects.filter(status='publish').order_by('-published')
        self.fields['latest_article_1'].queryset = published_articles
        self.fields['latest_article_2'].queryset = published_articles
        self.fields['latest_article_3'].queryset = published_articles

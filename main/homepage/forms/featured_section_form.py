from django import forms

from articles.models.article import Article

from ..models.featured_section import HomePageFeaturedArticles


class FeaturedArticlesForm(forms.ModelForm):
    '''
    Form for setting up the Featured Articles section of the home page.

    The form is linked to the EditFeaturedArticlesSection view.

    The form defines the following fields:
    - display_featured_section: Visibility of the section.
    - featured_article_1: First selected article.
    - featured_article_2: Second selected article.
    - featured_article_3: Third selected article.
    '''

    class Meta:
        '''
        The Meta class is a special inner class for configuring the form.

        The Meta class provides metadata and configuration for the main class,
        and here it defines the following attributes:
        - model: Specifies the model on which the form is based.
        - fields: Defines the fields that will be included in the form.
        - widgets: Allows specifying custom widgets for individual form fields.

        Widgets used in this code:
        - forms.CheckboxInput: Field for checkbox boolean value.
        - forms.Select: Field for selection from predefined values.
        '''

        model = HomePageFeaturedArticles
        fields = ['display_featured_section', 'featured_article_1', 'featured_article_2', 'featured_article_3']
        widgets = {
            'display_featured_section': forms.CheckboxInput(),
            'featured_article_1': forms.Select(),
            'featured_article_2': forms.Select(),
            'featured_article_3': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        '''
        Initialization method of the form.

        The method first calls the initialization of the parent class and then creates content
        for the selection menu for choosing previous and next articles.

        The method filters all published articles and sorts them from newest to oldest,
        and adds this list as a queryset to create the menu options
        for the 'featured_article_1' - 'featured_article_3' fields.
        '''

        super().__init__(*args, **kwargs)

        published_articles = Article.objects.filter(status='publish').order_by('-published')
        self.fields['featured_article_1'].queryset = published_articles
        self.fields['featured_article_2'].queryset = published_articles
        self.fields['featured_article_3'].queryset = published_articles

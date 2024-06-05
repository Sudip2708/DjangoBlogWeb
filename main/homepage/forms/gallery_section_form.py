from django import forms

from articles.models.article import Article

from ..models.gallery_section import HomePageGallerySection


class GallerySectionForm(forms.ModelForm):
    '''
    Form for editing Gallery section settings on the homepage.

    This form class is associated with the EditGalleryArticlesSection view.

    The form defines the following fields:
    - display_gallery_section: Visibility of the section.
    - gallery_article_1: First selected article.
    - gallery_article_2: Second selected article.
    - gallery_article_3: Third selected article.
    - gallery_article_4: Fourth selected article.
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
        - forms.Select: Field for selecting from predefined values.
        '''

        # Setting the model and an empty list for the section fields
        model = HomePageGallerySection
        fields = ['display_gallery_section', 'gallery_article_1', 'gallery_article_2', 'gallery_article_3', 'gallery_article_4']
        widgets = {
            'display_gallery_section': forms.CheckboxInput(),
            'gallery_article_1': forms.Select(),
            'gallery_article_2': forms.Select(),
            'gallery_article_3': forms.Select(),
            'gallery_article_4': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        '''
        Form initialization method.

        This method first calls the initialization of the parent class and then creates content
        for the selection menu for the previous and next articles.

        The method filters all published articles and sorts them from newest to oldest,
        and adds this list as a queryset to create a selection of values
        for the 'featured_article_1' - 'featured_article_3' fields.
        '''

        super().__init__(*args, **kwargs)

        all_articles = Article.objects.all().order_by('title')
        self.fields['gallery_article_1'].queryset = all_articles
        self.fields['gallery_article_2'].queryset = all_articles
        self.fields['gallery_article_3'].queryset = all_articles
        self.fields['gallery_article_4'].queryset = all_articles

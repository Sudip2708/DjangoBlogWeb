from django import forms
from taggit.forms import TagWidget

from ..models.article import Article


class ArticleSettingsForm(forms.ModelForm):
    '''
    Form for defining and managing selected fields of the Article model.

    This form is used in views:
    - ArticleCreateView: To create a new article.
    - ArticleUpdateView: To edit an existing article.

    This form is connected to the 'status', 'category', 'tags', 'previous_article', and 'next_article' fields
    and the corresponding tab of the page for their editing.
    '''

    class Meta:
        '''
        Meta class is a special inner class for form configuration.

        The Meta class provides metadata and configuration for the main class,
        and here it defines the following attributes:
        - model: Specifies the model on which the form is based.
        - fields: Defines the fields to be included in the form.
        - widgets: Allows specifying custom widgets for individual form fields.

        Widgets used in this code:
        - forms.Select: Field for selecting from pre-defined values.
        - TagWidget: Field from the Taggit module for managing tags.
        '''

        model = Article
        fields = ('status', 'category', 'tags', 'previous_article', 'next_article')
        widgets = {
            'status': forms.Select(),
            'category': forms.Select(),
            'tags': TagWidget(),
            'previous_article': forms.Select(),
            'next_article': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        '''
        Initialization method of the form.

        The method first calls the initialization of the parent class and then creates content
        for the selection menu for choosing the previous and next article.

        The method filters all published articles and sorts them from newest to oldest,
        and adds this list as a queryset to create a choice set for the 'previous_article' and 'next_article' fields.
        '''
        super().__init__(*args, **kwargs)

        published_articles = Article.objects.filter(status='publish').order_by('-published')
        self.fields['previous_article'].queryset = published_articles
        self.fields['next_article'].queryset = published_articles

    def clean(self):
        '''
        Method for cleaning and validating form data.

        This method is used to perform additional checks and modifications on cleaned data
        (cleaned_data) after it has been validated in the standard way.

        The method first checks whether the tags field has been changed
        and whether it contains any of the expressions from the 'invalid_tags' list.
        If so, it removes these expressions from the list.
        Then the method retrieves the list of tags from the previous relation and compares it with the current relation.
        If a tag has been deleted, these tags are overwritten to the instance attribute 'tags_to_delete'.
        (Followed by verification and possible deletion of the tag in the post_save signal 'handle_delete_unused_tags_post_save'.)

        Furthermore, the method checks whether the 'status' field has been changed and whether the new value is 'publish'
        (the article is ready for publishing), and then checks whether all fields necessary for publishing the article are filled in:
        - title: The title must be defined and must not be the automatically generated name.
        - overview: The article overview must be defined as it is used for the article preview.
        - content: The article content must be defined.
        - main_picture_max_size: The main picture must be defined (and must not be the default picture).
        - category_id: The field referring to the category must not contain the category with ID 1 (Uncategorized).
        - tags: The tags field must contain at least one tag.

        If any deficiency is detected, the method returns the form with the corresponding exception.

        If everything goes well, the method returns cleaned data to the view for further processing.
        '''
        cleaned_data = super().clean()

        # Processing tag change
        if 'tags' in self.changed_data:
            tags = cleaned_data.get('tags', [])

            # Filtering unwanted items
            invalid_tags = [':', '[{', 'value', '{', '}', '}]']
            cleaned_data['tags'] = [tag for tag in tags if tag not in invalid_tags]

            # Checking if a tag has been deleted (fills the tags_to_delete attribute list).
            original_tags = list(self.instance.tags.names() if self.instance.pk else [])
            self.instance.tags_to_delete = list(set(original_tags) - set(cleaned_data['tags']))

        # Article check before publication
        if 'status' in self.changed_data and cleaned_data.get('status') == 'publish':
            article = self.instance

            if article.title.startswith('#Article'):
                raise forms.ValidationError("To be published, the article must not start with the text 'Untitled Article'.")

            elif not article.overview:
                raise forms.ValidationError("To be published, the article must contain an overview.")

            elif not article.content:
                raise forms.ValidationError("To be published, the article must contain content.")

            elif article.main_picture_max_size.name == article.default_picture:
                raise forms.ValidationError("To be published, the article must contain a main picture.")

            elif article.category_id == 1:
                raise forms.ValidationError("To be published, the article must not be in the Uncategorized category.")

            elif not article.tags:
                raise forms.ValidationError("To be published, the article must contain at least one tag.")

        return cleaned_data

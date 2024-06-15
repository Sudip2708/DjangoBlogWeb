from django import forms
from tinymce.widgets import TinyMCE
from bs4 import BeautifulSoup

from ..models.article import Article
from ..schema.article_schema import ArticleSchema


class ArticleContentForm(forms.ModelForm):
    '''
    Form for defining and managing the 'content' field of the Article model.

    This form is used in views:
    - ArticleCreateView: To create a new article.
    - ArticleUpdateView: To edit an existing article.

    This form is connected only to the 'content' field
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
        - TinyMCE: The field is rendered using the TinyMCE extension for
                   creating and editing article content as HTML content.
        '''

        model = Article
        fields = ('content',)
        widgets = {
            'content': TinyMCE(attrs={
                'placeholder': "Here, you can create the content of the article." +
                               " After you're done here, don't forget to set the items" +
                               " in the Settings tab to complete and publish your article."
            }),
        }

    def clean(self):
        '''
        Method for cleaning and validating form data.

        This method is used to perform additional checks and modifications on cleaned data
        (cleaned_data) after it has been validated in the standard way.

        Here, the method first checks whether the edited article has the status field set to 'publish'
        (the article is intended for publishing and thus has a record in the whoosh index for faster full-text search).
        If so, it retrieves the content of the field (which is created as an HTML field via TinyMCE),
        then converts this content to text (without HTML tags) using BeautifulSoup,
        and then calls the update_index method of the ArticleSchema class to update the data of the respective field.

        The method returns cleaned data to the view for further processing.
        '''
        cleaned_data = super().clean()

        if self.instance.status == 'publish':
            html_text = cleaned_data.get('content')
            content_text = BeautifulSoup(html_text, 'html.parser').get_text(strip=True)
            ArticleSchema().update_field_in_index(self.instance.id, 'content', content_text)

        return cleaned_data

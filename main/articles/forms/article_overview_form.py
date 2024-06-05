from django import forms
from PIL import Image

from ..models.article import Article
from ..schema.article_schema import ArticleSchema


class ArticleOverviewForm(forms.ModelForm):
    '''
    Form for defining and managing selected fields of the Article model.

    This form is used in views:
    - ArticleCreateView: To create a new article.
    - ArticleUpdateView: To edit an existing article.

    This form is connected to the 'title', 'overview', and 'main_picture_max_size' fields
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
        - forms.TextInput: Field for entering short text.
        - forms.Textarea: Field for entering longer text (limited to 4 rows here).
        - forms.FileInput: Field for uploading files.
          (For the picture field, forms.FileInput is used to remove the field
          informing about the name of the current picture. The field has added
          restriction for input only for image files.)
        '''

        model = Article
        fields = ('title', 'overview', 'main_picture_max_size')
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "This field is mandatory for article creation."
            }),
            'overview': forms.Textarea(attrs={
                'placeholder': "Here, you can create an introduction to the article. " +
                               "It will be displayed in the preview and also on the article page. " +
                               "To continue with the article content, go to the Content tab.",
                'rows': 4
            }),
            'main_picture_max_size': forms.FileInput(attrs={
                'accept': 'image/*',
            }),
        }

    def clean(self):
        '''
        Method for cleaning and validating form data.

        This method is used to perform additional checks and modifications on cleaned data
        (cleaned_data) after it has been validated in the standard way.

        Here, the method first checks whether the edited article has the status field set to 'publish'
        (the article is intended for publishing and thus has a record in the whoosh index for faster full-text search).
        If so, it retrieves the content of the 'title' and 'overview' fields and then calls the update_index
        method of the ArticleSchema class to update the data of the respective fields.

        The method also checks whether an image has been uploaded.
        If so, it verifies whether the uploaded file can be opened in PIL (Python Imaging Library),
        and then internally using the PIL verify() method, it verifies that it is indeed an image.
        If the verification passes, the method sets the article instance attribute new_picture to True.
        This attribute is then used to detect changes to the image for capturing post_save signals of the article instance,
        for additional processing and editing of the main article image.
        If the verification fails, a forms.ValidationError exception is raised with an informative message.

        The method returns cleaned data to the view for further processing.
        '''

        cleaned_data = super().clean()

        if self.instance.status == 'publish':

            if 'title' in self.changed_data:
                title_text = cleaned_data.get('title')
                ArticleSchema().update_index(self.instance.id, 'title', title_text)

            if 'overview' in self.changed_data:
                overview_text = cleaned_data.get('title')
                ArticleSchema().update_index(self.instance.id, 'overview', overview_text)

        if 'main_picture_max_size' in self.changed_data:
            main_picture = cleaned_data.get('main_picture_max_size')
            try:
                with Image.open(main_picture) as img:
                    img.verify()
                self.instance.new_picture = True

            except (IOError, SyntaxError) as e:
                raise forms.ValidationError("Selected file is not a valid image file.")

        return cleaned_data

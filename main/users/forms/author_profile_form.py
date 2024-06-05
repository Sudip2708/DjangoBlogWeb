from django import forms
from PIL import Image

from articles.models.article_author import ArticleAuthor


class AuthorProfileForm(forms.ModelForm):
    '''
    Form for managing the author's account.

    This form defines the fields accessible to the user for editing content.
    It is used in the AuthorProfileView.

    Defined fields:
    - name: The author's username.
    - profile_picture: The author's profile picture.
    '''

    class Meta:
        '''
        The Meta class is used to configure the form.

        It defines the following attributes:
        - model: Specifies the model on which the form is based.
        - fields: The fields included in the form.
        - widgets: Specifies custom widgets for individual form fields.

        Used widgets:
        - forms.TextInput: A field for short text.
        - forms.FileInput: A field for uploading files.
          (For the image field, forms.FileInput is used with the accept attribute set to 'image/*',
          to restrict uploads to image files only.)
        '''

        model = ArticleAuthor
        fields = ['name', 'profile_picture']
        widgets = {
            'name': forms.TextInput(),
            'profile_picture': forms.FileInput(attrs={
                'accept': 'image/*',
            }),
        }

    def clean(self):
        '''
        Method for cleaning and validating form data.

        It is used to perform additional checks and modifications on cleaned_data
        after it has been validated in the standard way.

        It also checks if a profile picture has been uploaded.
        If so, it verifies whether it is a valid image using the PIL module.
        If the verification is successful, it sets the new_picture attribute of the article instance to True,
        which serves to detect the change of the image and for further processing in the post_save signals of the article instance.
        If the verification is not successful, it raises a forms.ValidationError with the information.

        Returns the cleaned data for further processing.
        '''

        cleaned_data = super().clean()

        if 'profile_picture' in self.changed_data:
            profile_picture = cleaned_data.get('profile_picture')
            try:
                with Image.open(profile_picture) as img:
                    img.verify()
                self.instance.new_picture = True

            except (IOError, SyntaxError) as e:
                raise forms.ValidationError("Selected file is not a valid image file.")

        return cleaned_data

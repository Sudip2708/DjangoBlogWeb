from django import forms
from PIL import Image

from ..models.custom_user import CustomUser


class UserProfileForm(forms.ModelForm):
    '''
    Form for managing the user account.

    This form defines the fields accessible to the user for editing content.
    It is used in the UserProfileView.

    Defined fields:
    - username: The user's nickname.
    - first_name: The user's first name.
    - last_name: The user's last name.
    - profile_picture: The user's profile picture.
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
        - forms.TextInput: A field for entering short text.
        - forms.FileInput: A field for uploading files.
          (For the image field, forms.FileInput is used with the accept attribute set to 'image/*',
          to restrict uploads to image files only.)
        '''

        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'profile_picture']
        widgets = {
            'username': forms.TextInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
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
        If the verification is successful, it sets the new_picture attribute of the instance to True,
        which serves to detect the change of the image and for further processing in the post_save signals of the instance.
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

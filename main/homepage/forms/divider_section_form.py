from django import forms
from tinymce.widgets import TinyMCE

from ..models.divider_section import HomePageDividerSection


class DividerSectionForm(forms.ModelForm):
    '''
    Form for setting up the Divider section of the home page.

    The form is linked to the EditDividerSection view.

    The form defines the following fields:
    - display_divider_section: Visibility of the section.
    - divider_image: Background image of the section.
    - divider_text: Text of the section.
    - divider_link_title: Description of the link.
    - divider_link: URL of the link.
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
        - forms.FileInput: Field for uploading files (limited to images here).
        - TinyMCE: Field for entering text using the TinyMCE module.
        - forms.TextInput: Field for entering short text.
        - forms.URLInput: Field for entering a URL.
        '''

        model = HomePageDividerSection
        fields = ['display_divider_section', 'divider_image', 'divider_text', 'divider_link_title', 'divider_link']
        widgets = {
            'display_divider_section': forms.CheckboxInput(),
            'divider_image': forms.FileInput(attrs={'accept': 'image/*',}),
            'divider_text': TinyMCE(),
            'divider_link_title': forms.TextInput(),
            'divider_link': forms.URLInput(),
        }

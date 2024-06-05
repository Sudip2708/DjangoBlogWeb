from django import forms
from tinymce.widgets import TinyMCE

from ..models.intro_section import HomePageIntroSection


class IntroSectionForm(forms.ModelForm):
    '''
    Form for setting up the Intro section of the homepage.

    This form class is associated with the EditIntroSection view.

    The form defines the following fields:
    - display_intro_section: Visibility of the section.
    - intro_title: Section title.
    - intro_description: Additional text.
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
        '''

        model = HomePageIntroSection
        fields = ['display_intro_section', 'intro_title', 'intro_description']
        widgets = {
            'display_intro_section': forms.CheckboxInput(),
            'intro_title': TinyMCE(),
            'intro_description': TinyMCE(),
        }

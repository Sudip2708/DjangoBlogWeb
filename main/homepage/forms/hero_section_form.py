from django import forms
from tinymce.widgets import TinyMCE

from ..models.hero_section import HomePageHeroSection


class HeroSectionForm(forms.ModelForm):
    '''
    Form for setting up the Hero section of the homepage.

    This form class is associated with the EditHeroSection view.

    The form defines the following fields:
    - display_hero_section: Visibility of the section.
    - hero_image: Background image of the section.
    - hero_title: Section title.
    - hero_link_title: Link description.
    - hero_link: Link URL.
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
        - forms.FileInput: Field for uploading files (restricted to images here).
        - TinyMCE: Field for entering text using the TinyMCE module.
        - forms.TextInput: Field for entering short text.
        - forms.URLInput: Field for entering URL.
        '''

        model = HomePageHeroSection
        fields = ['display_hero_section', 'hero_image', 'hero_title', 'hero_link_title', 'hero_link']
        widgets = {
            'display_hero_section': forms.CheckboxInput(),
            'hero_image': forms.FileInput(),
            'hero_title': TinyMCE(),
            'hero_link_title': forms.TextInput(),
            'hero_link': forms.URLInput(),
        }

from django import forms
from tinymce.widgets import TinyMCE

from homepage.models.newsletter_section import HomePageNewsletterSection


class NewsletterSectionForm(forms.ModelForm):
    '''
    Form for setting up the Newsletter section on the homepage.

    This form class is associated with the EditNewsletterSection view.

    The form defines the following fields:
    - display_newsletter_section: Visibility of the section.
    - newsletter_title: Section title.
    - newsletter_description: Descriptive text for the section.
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

        model = HomePageNewsletterSection
        fields = ['display_newsletter_section', 'newsletter_title', 'newsletter_description']
        widgets = {
            'display_newsletter_section': forms.CheckboxInput(),
            'newsletter_title': TinyMCE(),
            'newsletter_description': TinyMCE(),
        }

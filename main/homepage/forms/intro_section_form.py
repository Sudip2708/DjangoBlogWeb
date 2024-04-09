from django import forms
from tinymce.widgets import TinyMCE

from homepage.models.intro_section import HomePageIntroSection

class IntroSectionForm(forms.ModelForm):

    class Meta:
        model = HomePageIntroSection
        fields = ['display_intro_section', 'intro_title', 'intro_description']
        widgets = {
            'display_intro_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'intro_title': TinyMCE(),
            'intro_description': TinyMCE(),
        }

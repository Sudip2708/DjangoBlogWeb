from django import forms
from tinymce.widgets import TinyMCE

from homepage.models.divider_section import HomePageDividerSection


class DividerSectionForm(forms.ModelForm):
    class Meta:
        model = HomePageDividerSection
        fields = ['display_divider_section', 'divider_image', 'divider_text', 'divider_link_title', 'divider_link']
        widgets = {
            'display_divider_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'divider_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'divider_text': TinyMCE(),
            'divider_link_title': forms.TextInput(attrs={'class': 'form-control'}),
            'divider_link': forms.URLInput(attrs={'class': 'form-control'}),
        }

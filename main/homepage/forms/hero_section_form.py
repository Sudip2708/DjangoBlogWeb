from django import forms
from tinymce.widgets import TinyMCE

from homepage.models.hero_section import HomePageHeroSection


class HeroSectionForm(forms.ModelForm):
    class Meta:
        model = HomePageHeroSection
        fields = ['display_hero_section', 'hero_image', 'hero_title', 'hero_link_title', 'hero_link']
        widgets = {
            'display_hero_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'hero_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'hero_title': TinyMCE(),
            'hero_link_title': forms.TextInput(attrs={'class': 'form-control'}),
            'hero_link': forms.URLInput(attrs={'class': 'form-control'}),
        }

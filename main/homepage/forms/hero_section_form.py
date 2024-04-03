from django import forms
from homepage.models.hero_section import HomePageHeroSection

class HomePageHeroSectionForm(forms.ModelForm):
    class Meta:
        model = HomePageHeroSection
        fields = ['hero_image', 'hero_title', 'hero_link_title', 'hero_link']
        widgets = {
            'hero_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'hero_title': forms.TextInput(attrs={'class': 'form-control'}),
            'hero_link_title': forms.TextInput(attrs={'class': 'form-control'}),
            'hero_link': forms.URLInput(attrs={'class': 'form-control'}),
        }

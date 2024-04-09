from django import forms
from homepage.models.gallery_section import HomePageGallerySection

class GallerySectionForm(forms.ModelForm):
    class Meta:
        model = HomePageGallerySection
        fields = ['display_gallery_section', 'gallery_article_1', 'gallery_article_2', 'gallery_article_3', 'gallery_article_4']
        widgets = {
            'display_gallery_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'gallery_article_1': forms.Select(attrs={'class': 'form-control'}),
            'gallery_article_2': forms.Select(attrs={'class': 'form-control'}),
            'gallery_article_3': forms.Select(attrs={'class': 'form-control'}),
            'gallery_article_4': forms.Select(attrs={'class': 'form-control'}),
        }

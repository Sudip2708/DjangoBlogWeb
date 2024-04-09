from django import forms
from tinymce.widgets import TinyMCE

from homepage.models.newsletter_section import HomePageNewsletterSection

class NewsletterSectionForm(forms.ModelForm):
    class Meta:
        model = HomePageNewsletterSection
        fields = ['display_newsletter_section', 'newsletter_title', 'newsletter_description', 'newsletter_subscribers']
        widgets = {
            'display_newsletter_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'newsletter_title': TinyMCE(),
            'newsletter_description': TinyMCE(),
            'newsletter_subscribers': forms.Select(attrs={'class': 'form-control'}),
        }

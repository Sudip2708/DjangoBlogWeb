from django import forms
from django.utils import timezone

from homepage.models.featured_section import HomePageFeaturedArticles
from articles.models.article import Article

class FeaturedArticlesForm(forms.ModelForm):
    class Meta:
        model = HomePageFeaturedArticles
        fields = ['display_featured_section', 'featured_article_1', 'featured_article_2', 'featured_article_3']
        widgets = {
            'display_featured_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'featured_article_1': forms.Select(attrs={'class': 'form-control'}),
            'featured_article_2': forms.Select(attrs={'class': 'form-control'}),
            'featured_article_3': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Naplnění polí výběrovými možnostmi (seznamem publikovaných článků)
        self.fields['featured_article_1'].queryset = Article.objects.filter(status='publish', published__lte=timezone.now())
        self.fields['featured_article_2'].queryset = Article.objects.filter(status='publish', published__lte=timezone.now())
        self.fields['featured_article_3'].queryset = Article.objects.filter(status='publish', published__lte=timezone.now())

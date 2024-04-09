from django import forms
from tinymce.widgets import TinyMCE
from django.utils import timezone

from homepage.models.latest_section import HomePageLatestArticles
from articles.models.article import Article

class LatestArticlesForm(forms.ModelForm):
    class Meta:
        model = HomePageLatestArticles
        fields = ['display_latest_section', 'latest_title', 'latest_description', 'latest_article_1', 'latest_article_2', 'latest_article_3']
        widgets = {
            'display_latest_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'latest_title': TinyMCE(),
            'latest_description': TinyMCE(),
            'latest_article_1': forms.Select(attrs={'class': 'form-control'}),
            'latest_article_2': forms.Select(attrs={'class': 'form-control'}),
            'latest_article_3': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Naplnění polí výběrovými možnostmi (seznamem publikovaných článků)
        self.fields['latest_article_1'].queryset = Article.objects.filter(status='publish', published__lte=timezone.now())
        self.fields['latest_article_2'].queryset = Article.objects.filter(status='publish', published__lte=timezone.now())
        self.fields['latest_article_3'].queryset = Article.objects.filter(status='publish', published__lte=timezone.now())

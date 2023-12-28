### Definuje formuláře (na webu) pro pole s použitím TinyMCEWidget.

from django import forms

from .tinymce_winget import TinyMCEWidget
from articles.models.article import Article


class ArticleForm(forms.ModelForm):
    # Pole pro obsah článku s použitím TinyMCEWidget pro bohatý textový formát
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        # Specifikace modelu, pro který je formulář vytvořen
        model = Article

        # Seznam polí, která budou zahrnuta ve formuláři
        fields = (
            'title', 'overview', 'content', 'thumbnail',
            'categories', 'featured', 'previous_article', 'next_article'
        )

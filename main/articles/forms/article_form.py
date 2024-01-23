### Definuje formuláře (na webu) pro pole s použitím TinyMCEWidget.

from django import forms

from utilities.for_articles.tiny_mce_winget import TinyMCEWidget
from articles.models.article import Article
from utilities.shared.hide_current_in_image_field import hide_current_in_image_field


class ArticleForm(forms.ModelForm):

    main_picture_max_size = hide_current_in_image_field()

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
            'title', 'overview', 'content', 'main_picture_max_size',
            'categories', 'featured', 'previous_article', 'next_article'
        )

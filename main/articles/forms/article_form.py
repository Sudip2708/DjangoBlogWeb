### Definuje formuláře (na webu) pro pole s použitím TinyMCEWidget.

from django import forms

#from utilities.for_articles.tiny_mce_winget import TinyMCEWidget
from articles.models.article import Article
from articles.models.article_category import ArticleCategory
from utilities.shared.hide_current_from_image_field import hide_current_from_image_field
from tinymce.widgets import TinyMCE


class TinyMCEWidget(TinyMCE):
    # Předefinování metody use_required_attribute pro zakázání vyžadovaného atributu pro TinyMCEWidget
    def use_required_attribute(self, *args):
        return False

class ArticleForm(forms.ModelForm):

    main_picture_max_size = hide_current_from_image_field()

    # Pole pro obsah článku s použitím TinyMCEWidget pro bohatý textový formát
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        # Specifikace modelu, pro který je formulář vytvořen
        model = Article

        widgets = {'content': TinyMCE(attrs={'cols': 80, 'rows': 30})}


        # Seznam polí, která budou zahrnuta ve formuláři
        fields = (
            'main_picture_max_size', 'title', 'overview', 'content',
            'categories', 'featured', 'previous_article', 'next_article',

        )

### Definuje formuláře (na webu) pro pole s použitím TinyMCEWidget.

from django import forms

from articles.models.article import Article
from articles.models.article_category import ArticleCategory
from utilities.shared.hide_current_from_image_field import hide_current_from_image_field



class ArticleForm(forms.ModelForm):

    main_picture_max_size = hide_current_from_image_field()

    class Meta:
        # Specifikace modelu, pro který je formulář vytvořen
        model = Article

        # Seznam polí, která budou zahrnuta ve formuláři
        fields = (
            'main_picture_max_size',
            'title',
            'overview',
            'content',
            'public',
            'category',
            'tags',
            'previous_article',
            'next_article',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "This field is mandatory for article creation."
        self.fields['overview'].widget.attrs['placeholder'] = "Here, you can create an introduction to the article. It will be displayed in the preview and also on the article page. To continue with the article content, go to the Content tab."
        self.fields['content'].widget.attrs['placeholder'] = "Here, you can create the content of the article. After you're done here, don't forget to set the items in the Settings tab to complete and publish your article"


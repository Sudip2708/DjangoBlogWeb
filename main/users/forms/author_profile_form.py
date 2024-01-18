from django import forms

from articles.models.article_author import ArticleAuthor
from .hide_current_field import hide_current_field



# Formulář pro úpravu profilu autora
class AuthorProfileForm(forms.ModelForm):


    # Odebrání Current z ImageFields (pole s informací o aktuálně vybraném obrázku)
    profile_picture = hide_current_field()


    # Definice metadat
    class Meta:
        model = ArticleAuthor
        fields = ['author', 'profile_picture']


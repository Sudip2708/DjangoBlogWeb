from django import forms
from .models import CustomUser
from articles.models.article_author import ArticleAuthor


def remove_current():
    # Metoda pro odebrání zobrazení pole Current z ImageField
    return forms.ImageField(
        required=False,
        error_messages = {'invalid':"Image files only"},
        widget=forms.FileInput
    )

class UserProfileForm(forms.ModelForm):
    # Formulář pro úpravu uživatelského profilu

    # Odebrání z ImageFields pole pro aktuálně vybraný.
    profile_image = remove_current()
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'profile_image']


class AuthorProfileForm(forms.ModelForm):
    # Formulář pro úpravu profilu autora

    author_profile_picture = remove_current()
    class Meta:
        model = ArticleAuthor
        fields = ['author', 'author_profile_picture']


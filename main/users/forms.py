from django import forms
from .models import CustomUser
from articles.models.article_author import ArticleAuthor


def remove_current():
    '''
    Metoda pro odebrání zobrazení pole Current z ImageField.

    :return: Upravené pole ImageField
    '''

    return forms.ImageField(
        required=False,
        error_messages = {'invalid':"Image files only"},
        widget=forms.FileInput
    )


# Formulář pro úpravu uživatelského profilu
class UserProfileForm(forms.ModelForm):

    # Odebrání Current z ImageFields (pole s informací o aktuálně vybraném obrázku)
    profile_image = remove_current()

    # Definice metadat
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'profile_image']


# Formulář pro úpravu profilu autora
class AuthorProfileForm(forms.ModelForm):
    print("AuthorProfileForm constructor called")
    print()
    print("main/users/forms.py/AuthorProfileForm")
    print()

    # Odebrání Current z ImageFields (pole s informací o aktuálně vybraném obrázku)
    author_profile_picture = remove_current()

    # Definice metadat
    class Meta:
        model = ArticleAuthor
        fields = ['author', 'author_profile_picture']


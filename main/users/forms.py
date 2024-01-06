from django import forms
from .models import CustomUser
from articles.models.article_author import ArticleAuthor

class UserProfileForm(forms.ModelForm):
    # Formulář pro úpravu uživatelského profilu
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_image']

class AuthorProfileForm(forms.ModelForm):
    # Formulář pro úpravu profilu autora
    class Meta:
        model = ArticleAuthor
        fields = ['author', 'profile_picture']

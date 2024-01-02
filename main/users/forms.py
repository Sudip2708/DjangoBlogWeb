# forms.py
from django import forms
from django.contrib.auth.models import User

class FavoriteUserForm(forms.Form):
    username = forms.CharField(max_length=150)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Uživatel s tímto jménem neexistuje.')
        return username

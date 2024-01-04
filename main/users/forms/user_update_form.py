# forms.py

from django.contrib.auth.models import User
from django import forms


# Formulář pro aktualizaci údajů uživatele
class UserUpdateForm(forms.ModelForm):

    # Přidání pole pro e-mail
    email = forms.EmailField()

    # Meta třída definující metadata formuláře
    class Meta:

        # Specifikace modelu, který bude formulář vytvářet a aktualizovat (User)
        model = User

        # Pole, která budou zahrnuta ve formuláři
        fields = ['username', 'email', 'first_name', 'last_name']



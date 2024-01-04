# forms.py

from django import forms

from users.models.user_profile_model import UserProfile



# Formulář pro aktualizaci profilových informací uživatele
class ProfileUpdateForm(forms.ModelForm):

    # Meta třída definující metadata formuláře
    class Meta:

        # Specifikace modelu, který bude formulář vytvářet a aktualizovat (Profile)
        model = UserProfile

        # Pole, která budou zahrnuta ve formuláři
        fields = ['image']
from django import forms

from users.models import CustomUser
from .hide_current_field import hide_current_field



# Formulář pro úpravu uživatelského profilu
class UserProfileForm(forms.ModelForm):


    # Odebrání Current z ImageFields (pole s informací o aktuálně vybraném obrázku)
    profile_image = hide_current_field()


    # Definice metadat
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'profile_image']



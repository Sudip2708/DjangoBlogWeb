from django import forms

from users.models import CustomUser
from utilities.shared.hide_current_in_image_field import hide_current_in_image_field



# Formulář pro úpravu uživatelského profilu
class UserProfileForm(forms.ModelForm):


    # Odebrání Current z ImageFields (pole s informací o aktuálně vybraném obrázku)
    profile_picture = hide_current_in_image_field()


    # Definice metadat
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'profile_picture']



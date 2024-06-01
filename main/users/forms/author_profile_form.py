from django import forms
from PIL import Image

from articles.models.article_author import ArticleAuthor


class AuthorProfileForm(forms.ModelForm):
    '''
    Formulář pro správu účtu autora.

    Tento formulář definuje pole přístupná uživateli pro editaci obsahu.
    Je použit v pohledu AuthorProfileView.

    Definovaná pole:
    - name: Uživatelské jméno autora.
    - profile_picture: Profilový obrázek autora.
    '''

    class Meta:
        '''
        Třída Meta slouží k konfiguraci formuláře.

        Definuje následující atributy:
        - model: Určuje model, na kterém je formulář založen.
        - fields: Pole, která jsou zahrnuta ve formuláři.
        - widgets: Specifikuje vlastní widgety pro jednotlivá pole formuláře.

        Použité widgety:
        - forms.TextInput: Pole pro krátký text.
        - forms.FileInput: Pole pro nahrání souborů.
          (Pro pole obrázku je použito forms.FileInput s atributem accept nastaveným na 'image/*',
          aby se omezilo nahrání pouze obrazových souborů.)
        '''

        model = ArticleAuthor
        fields = ['name', 'profile_picture']
        widgets = {
            'name': forms.TextInput(),
            'profile_picture': forms.FileInput(attrs={
                'accept': 'image/*',
            }),
        }

    def clean(self):
        '''
        Metoda pro očištění a ověření dat formuláře.

        Používá se k provedení dodatečných kontrol a úprav na vyčištěných datech
        (cleaned_data), poté, co byla zvalidována standardním způsobem.

        Dále kontroluje, zda byl nahraný profilový obrázek.
        Pokud ano, ověří, zda jde o platný obrázek pomocí modulu PIL.
        Pokud ověření proběhne úspěšně, nastaví atributu instance článku new_picture na True,
        což slouží pro detekci změny obrázku a pro další zpracování v signálech post_save instance článku.
        Pokud ověření neproběhne úspěšně, vyvolá výjimku forms.ValidationError s informací.

        Navrací očištěná data pro další zpracování.
        '''

        cleaned_data = super().clean()

        if 'profile_picture' in self.changed_data:
            profile_picture = cleaned_data.get('profile_picture')
            try:
                with Image.open(profile_picture) as img:
                    img.verify()
                self.instance.new_picture = True

            except (IOError, SyntaxError) as e:
                raise forms.ValidationError("Selected file is not a valid image file.")

        return cleaned_data

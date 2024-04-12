from django import forms
from tinymce.widgets import TinyMCE

from homepage.models.divider_section import HomePageDividerSection


class DividerSectionForm(forms.ModelForm):
    '''
    Formulář pro editaci nastavení Divider sekce domácí stránky.

    Tato třída formuláře slouží k vytvoření formuláře pro úpravu nastavení sekce významných článků na domovské stránce.
    Obsahuje pole pro zobrazení a editaci jednotlivých nastavení,
    jako je například zobrazení sekce a výběr významných článků.
    '''

    class Meta:
        '''
        Meta třída pro specifikaci modelu a polí, která budou zahrnuta ve formuláři.

        Tato meta třída definuje strukturu a vzhled formuláře pro editaci nastavení této sekce.
        Obsahuje informace o tom, který model je použit pro tento formulář,
        jaká pole jsou zahrnuta a jaké widgety jsou použity pro jejich zobrazení.
        '''

        # Nastavení modelu a prázdného seznamu pro pole sekce
        model = HomePageDividerSection
        fields = ['display_divider_section', 'divider_image', 'divider_text', 'divider_link_title', 'divider_link']

        # Nastavení vzhledu widgetů pro pole formuláře
        widgets = {
            'display_divider_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'divider_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'divider_text': TinyMCE(),
            'divider_link_title': forms.TextInput(attrs={'class': 'form-control'}),
            'divider_link': forms.URLInput(attrs={'class': 'form-control'}),
        }

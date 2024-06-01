from django import forms
from tinymce.widgets import TinyMCE

from ..models.divider_section import HomePageDividerSection


class DividerSectionForm(forms.ModelForm):
    '''
    Formulář pro nastavení Divider sekce domácí stránky.

    Formulář je navázán na pohled EditDividerSection.

    Formulář definuje tato pole:
    - display_divider_section: Viditelnost sekce.
    - divider_image: Obrázek pozadí sekce.
    - divider_text: Text sekce.
    - divider_link_title: Popis odkazu.
    - divider_link: URL odkazu.
    '''

    class Meta:
        '''
        Třída Meta je speciální vnitřní třída pro konfiguraci formuláře.

        Třída Meta poskytuje metadata a konfiguraci pro hlavní třídu,
        a zde definuje následující atributy:
        - model: Určuje model, na kterém je formulář založen.
        - fields: Definuje pole, která budou zahrnuta ve formuláři.
        - widgets: Umožňuje specifikovat vlastní widgety pro jednotlivá pole formuláře.

        Widgety použité v tomto kódu:
        - forms.CheckboxInput: Pole pro zaškrtávací boolean hodnotu.
        - forms.FileInput: Pole pro nahrání souborů (zde omezeno na obrázek).
        - TinyMCE: Pole pro zadání textu pomocí modulu TinyMCE.
        - forms.TextInput: Pole pro zadání krátkého textu.
        - forms.URLInput: Pole pro zadání URL.
        '''

        model = HomePageDividerSection
        fields = ['display_divider_section', 'divider_image', 'divider_text', 'divider_link_title', 'divider_link']
        widgets = {
            'display_divider_section': forms.CheckboxInput(),
            'divider_image': forms.FileInput(attrs={'accept': 'image/*',}),
            'divider_text': TinyMCE(),
            'divider_link_title': forms.TextInput(),
            'divider_link': forms.URLInput(),
        }

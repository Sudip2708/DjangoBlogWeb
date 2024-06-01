from django import forms
from tinymce.widgets import TinyMCE

from ..models.hero_section import HomePageHeroSection


class HeroSectionForm(forms.ModelForm):
    '''
    Formulář pro nastavení Hero sekce domácí stránky.

    Formulář je navázán na pohled EditHeroSection.

    Formulář definuje tato pole:
    - display_hero_section: Viditelnost sekce.
    - hero_image: Obrázek pozadí sekce.
    - hero_title: Nadpis sekce.
    - hero_link_title: Popis odkazu.
    - hero_link: URL odkazu.
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

        model = HomePageHeroSection
        fields = ['display_hero_section', 'hero_image', 'hero_title', 'hero_link_title', 'hero_link']
        widgets = {
            'display_hero_section': forms.CheckboxInput(),
            'hero_image': forms.FileInput(),
            'hero_title': TinyMCE(),
            'hero_link_title': forms.TextInput(),
            'hero_link': forms.URLInput(),
        }

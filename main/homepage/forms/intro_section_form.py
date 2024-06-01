from django import forms
from tinymce.widgets import TinyMCE

from ..models.intro_section import HomePageIntroSection


class IntroSectionForm(forms.ModelForm):
    '''
    Formulář pro nastavení Intro sekce domácí stránky.

    Formulář je navázán na pohled EditIntroSection.

    Formulář definuje tato pole:
    - display_intro_section: Viditelnost sekce.
    - intro_title: Nadpis sekce.
    - intro_description: Doplňující text.
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
        - TinyMCE: Pole pro zadání textu pomocí modulu TinyMCE.
        '''

        model = HomePageIntroSection
        fields = ['display_intro_section', 'intro_title', 'intro_description']
        widgets = {
            'display_intro_section': forms.CheckboxInput(),
            'intro_title': TinyMCE(),
            'intro_description': TinyMCE(),
        }


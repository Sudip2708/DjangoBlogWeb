from django import forms
from tinymce.widgets import TinyMCE

from homepage.models.intro_section import HomePageIntroSection


class IntroSectionForm(forms.ModelForm):
    '''
    Formulář pro editaci nastavení Intro sekce domácí stránky.

    Tato třída formuláře slouží k vytvoření formuláře pro úpravu nastavení sekce
    významných článků na domovské stránce. Obsahuje pole pro zobrazení a editaci
    jednotlivých nastavení, jako je například zobrazení sekce a výběr významných
    článků.
    '''

    class Meta:
        '''
        Meta třída pro specifikaci modelu a polí, která budou zahrnuta ve formuláři.

        Tato meta třída definuje strukturu a vzhled formuláře pro editaci nastavení
        sekce významných článků na domovské stránce. Obsahuje informace o tom, který
        model je použit pro tento formulář, jaká pole jsou zahrnuta a jaké widgety
        jsou použity pro jejich zobrazení.
        '''

        # Nastavení modelu a prázdného seznamu pro pole sekce
        model = HomePageIntroSection
        fields = ['display_intro_section', 'intro_title', 'intro_description']

        # Nastavení vzhledu widgetů pro pole formuláře
        widgets = {
            'display_intro_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'intro_title': TinyMCE(),
            'intro_description': TinyMCE(),
        }

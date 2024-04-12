from django import forms
from tinymce.widgets import TinyMCE

from homepage.models.hero_section import HomePageHeroSection


class HeroSectionForm(forms.ModelForm):
    '''
    Formulář pro editaci nastavení Hero sekce domácí stránky.

    Tato třída formuláře slouží k vytvoření formuláře pro úpravu nastavení této sekce.
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
        model = HomePageHeroSection
        fields = ['display_hero_section', 'hero_image', 'hero_title', 'hero_link_title', 'hero_link']

        # Nastavení vzhledu widgetů pro pole formuláře
        widgets = {
            'display_hero_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'hero_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'hero_title': TinyMCE(),
            'hero_link_title': forms.TextInput(attrs={'class': 'form-control'}),
            'hero_link': forms.URLInput(attrs={'class': 'form-control'}),
        }

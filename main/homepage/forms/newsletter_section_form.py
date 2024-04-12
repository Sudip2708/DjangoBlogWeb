from django import forms
from tinymce.widgets import TinyMCE

from homepage.models.newsletter_section import HomePageNewsletterSection


class NewsletterSectionForm(forms.ModelForm):
    '''
    Formulář pro editaci nastavení Newsletter sekce domácí stránky.

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
        model = HomePageNewsletterSection
        fields = ['display_newsletter_section', 'newsletter_title', 'newsletter_description', 'newsletter_subscribers']

        # Nastavení vzhledu widgetů pro pole formuláře
        widgets = {
            'display_newsletter_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'newsletter_title': TinyMCE(),
            'newsletter_description': TinyMCE(),
            'newsletter_subscribers': forms.Select(attrs={'class': 'form-control'}),
        }

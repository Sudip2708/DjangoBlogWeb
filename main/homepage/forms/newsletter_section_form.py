from django import forms
from tinymce.widgets import TinyMCE

from homepage.models.newsletter_section import HomePageNewsletterSection


class NewsletterSectionForm(forms.ModelForm):
    '''
    Formulář pro nastavení sekce Novinek na domovské stránce.

    Formulář je navázán na pohled EditNewsletterSection.

    Formulář definuje tato pole:
    - display_newsletter_section: Viditelnost sekce.
    - newsletter_title: Nadpis sekce.
    - newsletter_description: Popisný text sekce.
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

        model = HomePageNewsletterSection
        fields = ['display_newsletter_section', 'newsletter_title', 'newsletter_description']
        widgets = {
            'display_newsletter_section': forms.CheckboxInput(),
            'newsletter_title': TinyMCE(),
            'newsletter_description': TinyMCE(),
        }

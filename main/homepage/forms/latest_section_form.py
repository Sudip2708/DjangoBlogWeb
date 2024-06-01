from django import forms
from tinymce.widgets import TinyMCE
from django.utils import timezone

from articles.models.article import Article

from ..models.latest_section import HomePageLatestArticles


class LatestArticlesForm(forms.ModelForm):
    '''
    Formulář pro nastavení sekce Nejnovější články na domovské stránce.

    Formulář je navázán na pohled EditLatestArticlesSection.

    Formulář definuje tato pole:
    - display_latest_section: Viditelnost sekce.
    - latest_title: Nadpis sekce.
    - latest_description: Popisný text sekce.
    - latest_article_1: První vybraný článek.
    - latest_article_2: Druhý vybraný článek.
    - latest_article_3: Třetí vybraný článek.
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
        - forms.Select: Pole pro výběr z přednastavených hodnot.
        '''

        model = HomePageLatestArticles
        fields = ['display_latest_section', 'latest_title', 'latest_description',
                  'latest_article_1', 'latest_article_2', 'latest_article_3']
        widgets = {
            'display_latest_section': forms.CheckboxInput(),
            'latest_title': TinyMCE(),
            'latest_description': TinyMCE(),
            'latest_article_1': forms.Select(),
            'latest_article_2': forms.Select(),
            'latest_article_3': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        '''
        Inicializační metoda formuláře.

        Metoda nejprve volá inicializaci nadřazené třídy a poté vytváří obsah
        pro nabídku pro výběr předchozího a následujícího článku.

        Metoda filtruje všechny publikované články a řadí je od nejnovějšího po nejstarší,
        a tento seznam přidává jako queryset pro vytvoření nabídky hodnot
        pro pole 'featured_article' 1 - 3.
        '''

        # Volání initu nadřazené třídy
        super().__init__(*args, **kwargs)

        published_articles = Article.objects.filter(status='publish').order_by('-published')
        self.fields['latest_article_1'].queryset = published_articles
        self.fields['latest_article_2'].queryset = published_articles
        self.fields['latest_article_3'].queryset = published_articles

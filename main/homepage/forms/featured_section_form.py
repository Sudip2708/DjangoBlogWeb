from django import forms
from django.utils import timezone

from articles.models.article import Article

from ..models.featured_section import HomePageFeaturedArticles


class FeaturedArticlesForm(forms.ModelForm):
    '''
    Formulář pro nastavení Featured Articles sekce domácí stránky.

    Formulář je navázán na pohled EditFeaturedArticlesSection.

    Formulář definuje tato pole:
    - display_featured_section: Viditelnost sekce.
    - featured_article_1: První vybraný článek.
    - featured_article_2: Druhý vybraný článek.
    - featured_article_3: Třetí vybraný článek.
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
        - forms.Select: Pole pro výběr z přednastavených hodnot.
        '''

        model = HomePageFeaturedArticles
        fields = ['display_featured_section', 'featured_article_1', 'featured_article_2', 'featured_article_3']
        widgets = {
            'display_featured_section': forms.CheckboxInput(),
            'featured_article_1': forms.Select(),
            'featured_article_2': forms.Select(),
            'featured_article_3': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        '''
        Inicializační metoda formuláře.

        Metoda nejprve volá inicializaci nadřazené třídy a poté vytváří obsah
        pro nabídku pro výběr předchozího a následujícího článku.

        Metoda filtruje všechny publikované články a řadí je od nejnovějšího po nejstarší,
        a tento seznam přidává jako queryset pro vytvoření nabídky hodnot
        pro pole 'featured_article_1' - 'featured_article_3'.
        '''

        super().__init__(*args, **kwargs)

        published_articles = Article.objects.filter(status='publish').order_by('-published')
        self.fields['featured_article_1'].queryset = published_articles
        self.fields['featured_article_2'].queryset = published_articles
        self.fields['featured_article_3'].queryset = published_articles

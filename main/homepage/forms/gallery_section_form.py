from django import forms

from articles.models.article import Article

from ..models.gallery_section import HomePageGallerySection


class GallerySectionForm(forms.ModelForm):
    '''
    Formulář pro editaci nastavení Gallery sekce domácí stránky.

    Formulář je navázán na pohled EditGalleryArticlesSection.

    Formulář definuje tato pole:
    - display_gallery_section: Viditelnost sekce.
    - gallery_article_1: První vybraný článek.
    - gallery_article_2: Druhý vybraný článek.
    - gallery_article_3: Třetí vybraný článek.
    - gallery_article_4: Čtvrtý vybraný článek.
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

        # Nastavení modelu a prázdného seznamu pro pole sekce
        model = HomePageGallerySection
        fields = ['display_gallery_section', 'gallery_article_1', 'gallery_article_2', 'gallery_article_3', 'gallery_article_4']
        widgets = {
            'display_gallery_section': forms.CheckboxInput(),
            'gallery_article_1': forms.Select(),
            'gallery_article_2': forms.Select(),
            'gallery_article_3': forms.Select(),
            'gallery_article_4': forms.Select(),
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

        all_articles = Article.objects.all().order_by('title')
        self.fields['gallery_article_1'].queryset = all_articles
        self.fields['gallery_article_2'].queryset = all_articles
        self.fields['gallery_article_3'].queryset = all_articles
        self.fields['gallery_article_4'].queryset = all_articles
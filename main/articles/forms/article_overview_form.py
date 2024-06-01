from django import forms
from PIL import Image

from ..models.article import Article
from ..schema.article_schema import ArticleSchema


class ArticleOverviewForm(forms.ModelForm):
    '''
    Formulář pro definování a správu vybraných polí modelu Article.

    Formulář je použit v pohledech:
    - ArticleCreateView: Pro vytvoření nového článku.
    - ArticleUpdateView: Pro úpravu existujícího článku.

    Tento formulář je napojen na pole 'title', 'overview' a 'main_picture_max_size'
    a příslušnou záložku stránky pro jejich úpravu.
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
        - forms.TextInput: Pole pro zadání krátkého textu.
        - forms.Textarea: Pole pro zadání delšího textu (zde omezeno na 4 řádky).
        - forms.FileInput: Pole pro nahrání souborů.
          (Pro pole obrázku je použito forms.FileInput, aby se odstranilo pole
          informující o názvu aktuálního obrázku. Poli je přidáno omezení
          na vstup pouze pro obrazové soubory.)
        '''

        model = Article
        fields = ('title', 'overview', 'main_picture_max_size')
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "This field is mandatory for article creation."
            }),
            'overview': forms.Textarea(attrs={
                'placeholder': "Here, you can create an introduction to the article. " +
                               "It will be displayed in the preview and also on the article page. " +
                               "To continue with the article content, go to the Content tab.",
                'rows': 4
            }),
            'main_picture_max_size': forms.FileInput(attrs={
                'accept': 'image/*',
            }),
        }

    def clean(self):
        '''
        Metoda pro očištění a ověření dat formuláře.

        Metoda se používá k provedení dodatečných kontrol a úprav na vyčištěných datech
        (cleaned_data) poté, co byla zvalidována standardním způsobem.

        Zde metoda nejprve ověří, zda upravovaný článek má hodnotu pole status nastavenou na 'publish'
        (článek je určen k publikování a má tak vytvořen záznam v indexu whoosh pro rychlejší fulltextové vyhledávání).
        Pokud ano, získá obsah pole 'title' a 'overview' a poté volá metodu update_index
        třídy ArticleSchema pro aktualizování dat daného pole.

        Metoda dále kontroluje, zda byl nahraný i obrázek.
        Pokud ano, obrázek ověří, zda jde otevřít v PIL (modul pro úpravu obrázků),
        a následně i vnitřní metodou PIL verify(), ověří že se skutečně jedná o obrázek.
        Pokud ověření projde, metoda nastavuje atribut instance článku new_picture na hodnotu True.
        Tento atribut pak slouží pro detekci změny obrázku, pro zachycení signálů post_save instance článku,
        pro dodatečné úpravy azpracování hlavního obrázku článku.
        Pokud ověření neproběhne úspěšně, je vyvolaná výjimka forms.ValidationError s informačním textem.

        Metoda navrací pohledu očištěná data pro další zpracování.
        '''

        cleaned_data = super().clean()

        if self.instance.status == 'publish':

            if 'title' in self.changed_data:
                title_text = cleaned_data.get('title')
                ArticleSchema().update_index(self.instance.id, 'title', title_text)

            if 'overview' in self.changed_data:
                overview_text = cleaned_data.get('title')
                ArticleSchema().update_index(self.instance.id, 'overview', overview_text)

        if 'main_picture_max_size' in self.changed_data:
            main_picture = cleaned_data.get('main_picture_max_size')
            try:
                with Image.open(main_picture) as img:
                    img.verify()
                self.instance.new_picture = True

            except (IOError, SyntaxError) as e:
                raise forms.ValidationError("Selected file is not a valid image file.")

        return cleaned_data

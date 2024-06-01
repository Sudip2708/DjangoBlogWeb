from django import forms
from tinymce.widgets import TinyMCE
from bs4 import BeautifulSoup

from ..models.article import Article
from ..schema.article_schema import ArticleSchema


class ArticleContentForm(forms.ModelForm):
    '''
    Formulář pro definování a správu pole 'content' modelu Article.

    Formulář je použit v pohledech:
    - ArticleCreateView: Pro vytvoření nového článku.
    - ArticleUpdateView: Pro úpravu existujícího článku.

    Tento formulář je napojen pouze na pole 'content'
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
        - TinyMCE: Pole je vykreslené pomocí rozšíření TinyMCE sloužícího
                   k vytváření a editaci obsahu článku jako HTML obsahu.
        '''

        model = Article
        fields = ('content',)
        widgets = {
            'content': TinyMCE(attrs={
                'placeholder': "Here, you can create the content of the article." +
                               " After you're done here, don't forget to set the items" +
                               " in the Settings tab to complete and publish your article."
            }),
        }

    def clean(self):
        '''
        Metoda pro očištění a ověření dat formuláře.

        Metoda se používá k provedení dodatečných kontrol a úprav na vyčištěných datech
        (cleaned_data) poté, co byla zvalidována standardním způsobem.

        Zde metoda nejprve ověří, zda upravovaný článek má hodnotu pole status nastavenou na 'publish'
        (článek je určen k publikování a má tak vytvořen záznam v indexu whoosh pro rychlejší fulltextové vyhledávání).
        Pokud ano, získá obsah pole (které je vytvořené jako HTML field prostřednictvím TinyMCE),
        a následně převede tento obsah na text (bez HTML tagů) pomocí BeautifulSoup,
        a poté volá metodu update_index třídy ArticleSchema pro aktualizování dat daného pole.

        Metoda navrací pohledu očištěná data pro další zpracování.
        '''
        cleaned_data = super().clean()

        if self.instance.status == 'publish':
            html_text = cleaned_data.get('content')
            content_text = BeautifulSoup(html_text, 'html.parser').get_text(strip=True)
            ArticleSchema().update_index(self.instance.id, 'content', content_text)

        return cleaned_data

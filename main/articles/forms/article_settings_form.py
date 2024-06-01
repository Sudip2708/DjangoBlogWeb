from django import forms
from taggit.forms import TagWidget

from ..models.article import Article


class ArticleSettingsForm(forms.ModelForm):
    '''
    Formulář pro definování a správu vybraných polí modelu Article.

    Formulář je použit v pohledech:
    - ArticleCreateView: Pro vytvoření nového článku.
    - ArticleUpdateView: Pro úpravu existujícího článku.

    Tento formulář je napojen na pole 'status', 'category', 'tags', 'previous_article' a 'next_article'
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
        - forms.Select: Pole pro výběr z přednastavených hodnot.
        - TagWidget: Pole modulu Taggit pro správu tagů.
        '''

        model = Article
        fields = ('status', 'category', 'tags', 'previous_article', 'next_article')
        widgets = {
            'status': forms.Select(),
            'category': forms.Select(),
            'tags': TagWidget(),
            'previous_article': forms.Select(),
            'next_article': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        '''
        Inicializační metoda formuláře.

        Metoda nejprve volá inicializaci nadřazené třídy a poté vytváří obsah
        pro nabídku pro výběr předchozího a následujícího článku.

        Metoda filtruje všechny publikované články a řadí je od nejnovějšího po nejstarší,
        a tento seznam přidává jako queryset pro vytvoření nabídky hodnot
        pro pole 'previous_article' a 'next_article'.
        '''
        super().__init__(*args, **kwargs)

        published_articles = Article.objects.filter(status='publish').order_by('-published')
        self.fields['previous_article'].queryset = published_articles
        self.fields['next_article'].queryset = published_articles

    def clean(self):
        '''
        Metoda pro očištění a ověření dat formuláře.

        Metoda se používá k provedení dodatečných kontrol a úprav na vyčištěných datech
        (cleaned_data) poté, co byla zvalidována standardním způsobem.

        Metoda nejprve ověří, zda bylo změněno pole pro tagy
        a zda neobsahuje některý z výrazů ze seznamu 'invalid_tags'.
        Pokud ano, pak tyto výrazy ze seznamu odstraní.
        Následně metoda vytáhne seznam tagů z předešlé relace a porovná ho s aktuální relací.
        Pokud došlo ke smazání tagu, přepíše tyto tagy do atributu instance 'tags_to_delete'.
        (Následuje ověření a případné smazání tagu v post_save signálu 'handle_delete_unused_tags_post_save'.)

        Dále metoda ověřuje, zda došlo ke změně pole 'status' a zda nová hodnota je 'publish'
        (článek je připraven k publikování) a následně probíhá kontrola,
        zda jsou vyplněna všechna pole potřebná pro publikování článku:
        - title: Titulek musí být definován a nesmí být automaticky generovaný název.
        - overview: Popis článku musí být definován, neboť je použit pro náhled článku.
        - content: Obsah článku musí být definován.
        - main_picture_max_size: Hlavní obrázek musí být definován (a nesmí být defaultním obrázkem).
        - category_id: Pole odkazující na kategorii nesmí obsahovat kategorii s ID 1 (Uncategorized).
        - tags: Pole pro tagy musí obsahovat alespoň jeden tag.

        Pokud metoda zjistí nějaký nedostatek, vrací formulář s příslušnou výjimkou.

        Pokud vše proběhne v pořádku, metoda navrací pohledu očištěná data pro další zpracování.
        '''
        cleaned_data = super().clean()

        # Zpracování změny tagů
        if 'tags' in self.changed_data:
            tags = cleaned_data.get('tags', [])

            # Odfiltrování nežádoucích položek
            invalid_tags = [':', '[{', 'value', '{', '}', '}]']
            cleaned_data['tags'] = [tag for tag in tags if tag not in invalid_tags]

            # Kontrola, zda došlo k smazání tagu (dojde k naplnění seznamu atributu tags_to_delete).
            original_tags = list(self.instance.tags.names() if self.instance.pk else [])
            self.instance.tags_to_delete = list(set(original_tags) - set(cleaned_data['tags']))

        # Kontrola článku před jeho publikací
        if 'status' in self.changed_data and cleaned_data.get('status') == 'publish':
            article = self.instance

            if article.title.startswith('#Article'):
                raise forms.ValidationError("To be published, the article must not start with the text 'Untitled Article'.")

            elif not article.overview:
                raise forms.ValidationError("To be published, the article must contain an overview.")

            elif not article.content:
                raise forms.ValidationError("To be published, the article must contain content.")

            elif article.main_picture_max_size.name == article.default_picture:
                raise forms.ValidationError("To be published, the article must contain a main picture.")

            elif article.category_id == 1:
                raise forms.ValidationError("To be published, the article must not be in the Uncategorized category.")

            elif not article.tags:
                raise forms.ValidationError("To be published, the article must contain at least one tag.")

        return cleaned_data

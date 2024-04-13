from django import forms

from homepage.models.gallery_section import HomePageGallerySection
from articles.models.article import Article


class GallerySectionForm(forms.ModelForm):
    '''
    Formulář pro editaci nastavení Gallery sekce domácí stránky.

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
        model = HomePageGallerySection
        fields = []

    def __init__(self, *args, **kwargs):
        '''
        Inicializační metoda formuláře.

        Tato metoda slouží k inicializaci instance formuláře.
        Přijímá libovolný počet pozicinálních argumentů a klíčových argumentů,
        které jsou dále předány nadřazené třídě.

        :param args: Pozicinální argumenty pro inicializaci.
        :param kwargs: Klíčové argumenty pro inicializaci.
        '''

        # Volání initu nadřazené třídy
        super().__init__(*args, **kwargs)

        # Načtení instance pro Gallery section
        instance = HomePageGallerySection.singleton()

        # Pole pro zobrazení footeru
        self.fields['display_gallery_section'] = forms.BooleanField(
            label='Display Gallery Section',
            initial=instance.display_gallery_section,
            required=False
        )

        # Získání seznamu s tuples obsahujících ID a názvy všech článků
        articles = Article.objects.all().order_by('title').values_list('id', 'title')
        articles_choices = list(articles)

        # Cyklus pro vytvoření polí pro výběr článků
        for n in range(1, 5):

            # Vytvoření názvu pole
            field_name = f"gallery_article_{n}"

            # Načtení aktuální hodnoty a následné přidání na začátek seznamu
            initial_choice = (instance.__dict__[field_name]["article_id"], instance.__dict__[field_name]["title"])
            self.fields[field_name] = forms.ChoiceField(
                label=f"{n}. Article",
                choices= [initial_choice] + articles_choices,
                widget=forms.Select(attrs={'class': 'form-control'})
            )


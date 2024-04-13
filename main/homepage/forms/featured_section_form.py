from django import forms
from django.utils import timezone

from homepage.models.featured_section import HomePageFeaturedArticles
from articles.models.article import Article


class FeaturedArticlesForm(forms.ModelForm):
    '''
    Formulář pro editaci nastavení Featured Articles sekce domácí stránky.

    Tato třída formuláře slouží k vytvoření formuláře pro úpravu nastavení této sekce.
    Obsahuje pole pro zobrazení a editaci jednotlivých nastavení,
    jako je například zobrazení sekce a výběr významných článků.
    Také obsahuje inicializační metodu pro úpravu widgetů
    a naplnění polí výběrovými možnostmi.
    '''

    class Meta:
        '''
        Meta třída pro specifikaci modelu a polí, která budou zahrnuta ve formuláři.

        Tato meta třída definuje strukturu a vzhled formuláře pro editaci nastavení této sekce.
        Obsahuje informace o tom, který model je použit pro tento formulář,
        jaká pole jsou zahrnuta a jaké widgety jsou použity pro jejich zobrazení.
        '''

        # Nastavení modelu a prázdného seznamu pro pole sekce
        model = HomePageFeaturedArticles
        fields = ['display_featured_section', 'featured_article_1', 'featured_article_2', 'featured_article_3']

        # Nastavení vzhledu widgetů pro pole formuláře
        widgets = {
            'display_featured_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'featured_article_1': forms.Select(attrs={'class': 'form-control'}),
            'featured_article_2': forms.Select(attrs={'class': 'form-control'}),
            'featured_article_3': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        '''
        Inicializační metoda formuláře.

        Tato metoda slouží k inicializaci instance formuláře.
        Přijímá libovolný počet pozicinálních argumentů a klíčových argumentů,
        které jsou dále předány nadřazené třídě.
        Zde přepisuje seznam nabízených článků pro pole Select tak,
        aby se nabídli jen články se statusem publish a srovnané sestupně dle data publish

        :param args: Pozicinální argumenty pro inicializaci.
        :param kwargs: Klíčové argumenty pro inicializaci.
        '''

        # Volání initu nadřazené třídy
        super().__init__(*args, **kwargs)

        # Naplnění polí pro výběr článků seznamem publikovaných článků
        published_articles = Article.objects.filter(status='publish', published__lte=timezone.now())
        self.fields['featured_article_1'].queryset = published_articles
        self.fields['featured_article_2'].queryset = published_articles
        self.fields['featured_article_3'].queryset = published_articles
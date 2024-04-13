from django import forms

from homepage.models.footer_section import FooterSettings
from articles.models.article import Article


class FooterSettingsForm(forms.ModelForm):
    '''
    Formulář pro editaci nastavení patičky.

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
        model = FooterSettings
        fields = []

    def __init__(self, *args, **kwargs):
        '''
        Inicializační metoda formuláře.

        Tato metoda inicializuje instanci formuláře pro úpravu sekce patičky.
        Vytváří pole pro jednotlivé části formuláře pomocí metody self.fields, která přidává pole do formuláře. 
        Každé pole má svůj vlastní widget, který určuje, jak bude pole zobrazeno ve webovém rozhraní.

        :param args: Pozicinální argumenty pro inicializaci.
        :param kwargs: Klíčové argumenty pro inicializaci.
        '''

        # Volání initu nadřazené třídy
        super().__init__(*args, **kwargs)

        # Načtení instance pro footer
        instance = FooterSettings.singleton()

        # Pole pro zobrazení footeru
        self.fields['display_footer_section'] = forms.BooleanField(
            label='Display Footer Section',
            initial=instance.display_footer_section,
            required=False
        )

        # Cyklus pro vytvoření polí pro zobrazení adresy
        for key, value in instance.address_values.items():
            # Pokud jde o email vytvoř pole pro email
            if key == 'email':
                self.fields[key] = forms.EmailField(
                    label=value["label"],
                    initial=value["value"],
                    required=False
                )
            # Ve všech ostatních případech vytvoř textové pole
            else:
                self.fields[key] = forms.CharField(
                    label=value["label"],
                    initial=value["value"],
                    required=False
                )

        # Cyklus pro vytvoření textových polí pro zadání url sociálních sítí
        for key, value in instance.social_media.items():
            self.fields[key] = forms.CharField(
                label=value["label"],
                initial=value["url"],
                required=False
            )

        # Cyklus pro vytvoření textových polí pro zadání odkazů na vybrané stránky
        for n, (name, dic) in enumerate(instance.site_links.items(), start=1):
            # Pole pro pojmenování odkazu (zobrazí se v patičce)
            self.fields[f"name_field_{n}"] = forms.CharField(
                label=f"{n}. Name",
                initial=dic["name"],
                required=False
            )
            # Pole pro zadání odkazu
            self.fields[f"url_field_{n}"] = forms.CharField(
                label=f"{n}. URL",
                initial=dic["url"],
                required=False
            )

        # Získání seznamu s tuples obsahujících ID a názvy všech článků
        articles = Article.objects.all().order_by('title').values_list('id', 'title')
        articles_choices = list(articles)

        # Cyklus pro vytvoření polí pro výběr článků
        for n, (key, value) in enumerate(instance.articles.items(), start=1):
            # Načtení aktuální hodnoty a následné přidání na začátek seznamu
            initial_choice = (value["article_id"], value["title"])
            self.fields[key] = forms.ChoiceField(
                label=f"{n}. Article",
                choices= [initial_choice] + articles_choices,
                widget=forms.Select(attrs={'class': 'form-control'})
            )

        # Cyklus pro vytvoření polí pro editaci hodnot posledního řádku
        for key, value in instance.end_line.items():
            # Pro nastavením viditelnosti vytvoř boolean pole
            if key == "display_footer_end_section":
                self.fields[key] = forms.BooleanField(
                    label=value["label"],
                    initial=value["value"],
                    required=False
                )
            # Pro všechny ostatní položky vytvoř textové pole
            else:
                self.fields[key] = forms.CharField(
                    label=value["label"],
                    initial=value["value"],
                    required=False
                )


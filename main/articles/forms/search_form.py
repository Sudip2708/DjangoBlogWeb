from django import forms

from ..models.article_author import ArticleAuthor


class ArticleSearchForm(forms.Form):
    '''
    Formulář pro definici polí pro vyhledávání v článcích.

    Formulář je použit následujícími pohledy:
    - SearchInputView: Stránka pro zadání dotazu pro vyhledávání v článcích.
    - SearchView: Stránka pro zpracování zadaného dotazu pro vyhledávání v článcích.

    Tento formulář definuje následující pole, která jsou použita
    pro zadání hledání v publikovaných článcích:
    - query: Pole pro zadání textu pro vyhledávání.
    - search_in_title: Pole pro specifikaci hledání zadaného textu v názvu článku.
    - search_in_description: Pole pro specifikaci hledání zadaného textu v popisu článku.
    - search_in_content: Pole pro specifikaci hledání zadaného textu v obsahu článku.
    - date_from: Pole pro specifikaci data, od kterého byl článek publikován.
    - date_to: Pole pro specifikaci data, před kterým byl článek publikován.
    - author: Pole pro specifikaci autora.

    Formulář má definovanou metodu clean pro validaci dat.
    '''

    query = forms.CharField(
        required=False,
        widget=forms.TextInput()
    )

    search_in_title = forms.BooleanField(
        required=False,
        label='Title',
        initial=True,
        widget=forms.CheckboxInput()
    )

    search_in_description = forms.BooleanField(
        required=False,
        label='Overview',
        initial=True,
        widget=forms.CheckboxInput()
    )

    search_in_content = forms.BooleanField(
        required=False,
        label='Content',
        initial=True,
        widget=forms.CheckboxInput()
    )

    date_from = forms.DateField(
        required=False,
        label='Published After',
        widget=forms.DateInput(
            attrs={'type': 'date'}
        )
    )

    date_to = forms.DateField(
        required=False,
        label='Published Before',
        widget=forms.DateInput(
            attrs={'type': 'date'}
        )
    )

    author = forms.ModelChoiceField(
        required=False,
        queryset=ArticleAuthor.objects.all(),
        empty_label='Choose author...',
        widget=forms.Select()
    )

    def clean(self):
        '''
        Metoda pro kontrolu zadaných dat formuláře.

        Metoda nejprve z formuláře vytáhne data a přiřadí je proměným.

        Po té zkontroluje, zda byl zadán dotaz pro hledání, nebo datup před, či po, a nebo autor,
        a pokud nebyl zadána ani jedna položky vyvolá výjimku upozorňující na nezadání parametru.

        Následně se ověří, zda byl zadán dotaz pro hledání a zda je vybraná alespoň jedna oblast hledání,
        v případě že není zadaná žádná oblast hledání, vyvolá výjimku upozorňující na tento stav.

        Následně proběhne kontrola, zda byl zdadán datum před i datum po,
        a pokud ano, ověří, zda datum před není větší než datum po,
        pokud ano, vyvolá výjimku upozorňující na tento problém.
        '''

        # Načtení dat z formuláře
        cleaned_data = super().clean()
        query = cleaned_data.get('query', '')
        before = cleaned_data.get('date_to', '')
        after = cleaned_data.get('date_from', '')
        author = cleaned_data.get('author', '')
        title = cleaned_data.get('search_in_title', False)
        overview = cleaned_data.get('search_in_description', False)
        content = cleaned_data.get('search_in_content', False)

        # Kontrola, zda byl zadán parametr pro hledání.
        if not (query or before or after or author):
            raise forms.ValidationError(
                "No search parameter was entered."
            )

        # Kontrola, zda při zadání dotazu je specifikována i oblast hledání.
        if query:
            if not title and not overview and not content:
                raise forms.ValidationError(
                    "A search term was entered, but no search area is checked."
                )

        # Kontrola, zda při zadání data před a po nedošlo k prohození těchto údajů.
        if before and after and before < after:
            raise forms.ValidationError(
                "The date for Published After must not be greater than the date for Published Before."
            )

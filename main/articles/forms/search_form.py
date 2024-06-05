from django import forms

from ..models.article_author import ArticleAuthor


class ArticleSearchForm(forms.Form):
    '''
    Form for defining fields for searching in articles.

    This form is used by the following views:
    - SearchInputView: Page for entering a query for searching in articles.
    - SearchView: Page for processing the entered query for searching in articles.

    This form defines the following fields used
    for entering search criteria in published articles:
    - query: Field for entering text for searching.
    - search_in_title: Field for specifying searching the entered text in the article title.
    - search_in_description: Field for specifying searching the entered text in the article overview.
    - search_in_content: Field for specifying searching the entered text in the article content.
    - date_from: Field for specifying the date from which the article was published.
    - date_to: Field for specifying the date before which the article was published.
    - author: Field for specifying the author.

    The form has a defined clean method for data validation.
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
        Method for checking the entered form data.

        The method first retrieves the data from the form and assigns it to variables.

        Then it checks whether a search query, date before or after, or author was entered,
        and if none of these parameters were entered, it raises an exception warning about the lack of input.

        It then verifies whether a search query was entered and whether at least one search area is selected,
        and if no search area is selected, it raises an exception alerting to this condition.

        Then it checks whether both a date before and a date after were entered,
        and if so, it verifies that the date before is not greater than the date after,
        if it is, it raises an exception alerting to this issue.
        '''

        # Retrieve data from the form
        cleaned_data = super().clean()
        query = cleaned_data.get('query', '')
        before = cleaned_data.get('date_to', '')
        after = cleaned_data.get('date_from', '')
        author = cleaned_data.get('author', '')
        title = cleaned_data.get('search_in_title', False)
        overview = cleaned_data.get('search_in_description', False)
        content = cleaned_data.get('search_in_content', False)

        # Check if a search parameter was entered
        if not (query or before or after or author):
            raise forms.ValidationError(
                "No search parameter was entered."
            )

        # Check if a search term was entered, but no search area is checked
        if query:
            if not title and not overview and not content:
                raise forms.ValidationError(
                    "A search term was entered, but no search area is checked."
                )

        # Check if the date for Published After is not greater than the date for Published Before
        if before and after and before < after:
            raise forms.ValidationError(
                "The date for Published After must not be greater than the date for Published Before."
            )

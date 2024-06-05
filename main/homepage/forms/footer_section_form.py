from django import forms

from articles.models.article import Article

from ..models.footer_section import FooterSettings


class FooterSettingsForm(forms.ModelForm):
    '''
    Form for editing footer settings.

    This form class is used to create a form for editing the settings of this section.
    It contains fields for displaying and editing individual settings,
    such as section visibility and selection of significant articles.
    It also includes an initialization method for editing widgets
    and populating fields with selection options.
    '''

    class Meta:
        '''
        Meta class for specifying the model and fields to be included in the form.

        This meta class defines the structure and appearance of the form for editing this section's settings.
        It contains information about which model is used for this form,
        which fields are included, and which widgets are used to display them.
        '''

        # Setting the model and an empty list for the section fields
        model = FooterSettings
        fields = []

    def __init__(self, *args, **kwargs):
        '''
        Form initialization method.

        This method initializes the form instance for editing the footer section.
        It creates fields for individual parts of the form using the self.fields method, which adds fields to the form.
        Each field has its own widget that determines how the field will be displayed in the web interface.
        '''

        # Calling the init of the parent class
        super().__init__(*args, **kwargs)

        # Loading the instance for the footer
        instance = FooterSettings.singleton()

        # Field for displaying the footer
        self.fields['display_footer_section'] = forms.BooleanField(
            label='Display Footer Section',
            initial=instance.display_footer_section,
            required=False
        )

        # Loop for creating fields for displaying the address
        for key, value in instance.address_values.items():
            # If it's an email, create a field for email
            if key == 'email':
                self.fields[key] = forms.EmailField(
                    label=value["label"],
                    initial=value["value"],
                    required=False
                )
            # For all other cases, create a text field
            else:
                self.fields[key] = forms.CharField(
                    label=value["label"],
                    initial=value["value"],
                    required=False
                )

        # Loop for creating text fields for entering social media URLs
        for key, value in instance.social_media.items():
            self.fields[key] = forms.CharField(
                label=value["label"],
                initial=value["url"],
                required=False
            )

        # Loop for creating text fields for entering links to selected pages
        for n, (name, dic) in enumerate(instance.site_links.items(), start=1):
            # Field for naming the link (displayed in the footer)
            self.fields[f"name_field_{n}"] = forms.CharField(
                label=f"{n}. Name",
                initial=dic["name"],
                required=False
            )
            # Field for entering the link
            self.fields[f"url_field_{n}"] = forms.CharField(
                label=f"{n}. URL",
                initial=dic["url"],
                required=False
            )

        # Getting a list of tuples containing IDs and titles of all articles
        articles = Article.objects.all().order_by('title').values_list('id', 'title')
        articles_choices = list(articles)

        # Loop for creating fields for selecting articles
        for n, (key, value) in enumerate(instance.articles.items(), start=1):
            # Loading the current value and then adding it to the beginning of the list
            initial_choice = (value["article_id"], value["title"])
            self.fields[key] = forms.ChoiceField(
                label=f"{n}. Article",
                choices=[initial_choice] + articles_choices,
                widget=forms.Select(attrs={'class': 'form-control'})
            )

        # Loop for creating fields for editing the values of the last row
        for key, value in instance.end_line.items():
            # For setting visibility, create a boolean field
            if key == "display_footer_end_section":
                self.fields[key] = forms.BooleanField(
                    label=value["label"],
                    initial=value["value"],
                    required=False
                )
            # For all other items, create a text field
            else:
                self.fields[key] = forms.CharField(
                    label=value["label"],
                    initial=value["value"],
                    required=False
                )

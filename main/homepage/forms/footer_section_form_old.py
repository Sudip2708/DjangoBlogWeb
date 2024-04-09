from django import forms
from homepage.models.footer_section import FooterSettings

class FooterSettingsForm(forms.ModelForm):

    class Meta:

        # Model pro tento formulář
        model = FooterSettings


        # Vytovření seznamu položek pro formulář
        fields = []

        # Seznam pro položky adresy
        address = ['company_name', 'address', 'phone', 'email']
        fields += address

        # Seznam pro položky sociálních účtů
        social_accounts = ['facebook_url', 'twitter_url', 'instagram_url', 'behance_url', 'pinterest_url']
        fields += social_accounts

        # Seznam pro položky vybraných odkazů
        selected_links = []
        for number in range(1, 9):
            selected_links.append(f'name_field_{number}')
            selected_links.append(f'url_field_{number}')
        fields += selected_links

        # Seznam pro položky vybraných článků
        selected_articles = [f'footer_article_{number}' for number in range(1, 4)]
        fields += selected_articles



        # Vytvoření slovníku pro vykreslení položek
        widgets = {}

        # Položky adresy
        for field in address:
            widgets[field] = forms.TextInput(attrs={'class': 'form-control'})

        # Položky sociálních účtů
        for field in social_accounts:
            widgets[field] = forms.URLInput(attrs={'class': 'form-control'})

        # Položky vybraných odkazů
        for index, field in enumerate(selected_links):
            if index % 2 == 0:
                widgets[field] = forms.TextInput(attrs={'class': 'form-control'})
            else:
                widgets[field] = forms.URLInput(attrs={'class': 'form-control'})

        # Položky vybraných článků
        for field in selected_articles:
            widgets[field] = forms.Select(attrs={'class': 'form-control'})
from django import forms
from homepage.models.footer_section import FooterSettings

class FooterSettingsForm(forms.ModelForm):

    class Meta:
        # Model pro tento formulář
        model = FooterSettings

        # Vytovření seznamu položek pro formulář
        fields = [
            'display_footer_section',
            'display_footer_end_section',
        ]

        # Seznam pro položky adresy
        address = ['company_name', 'address', 'phone', 'email']

        # Seznam pro položky sociálních účtů
        social_accounts = ['facebook_url', 'twitter_url', 'instagram_url', 'behance_url', 'pinterest_url']

        # Seznam pro položky vybraných odkazů
        selected_links = [f'name_field_{number}' for number in range(1, 9)]
        selected_links_urls = [f'url_field_{number}_url' for number in range(1, 9)]

        # Seznam pro položky vybraných článků
        selected_articles = [f'footer_article_{number}' for number in range(1, 4)]

        # Seznam pro položky koncové patičky
        footer_end = ['end_right_text', 'end_left_text', 'end_left_link_text', 'end_left_link_url']

        # Seskupení položek do sekcí
        section_fields = {
            'address': address,
            'social_accounts': social_accounts,
            'selected_links': selected_links + selected_links_urls,
            'selected_articles': selected_articles,
            'footer_end': footer_end
        }

        # Přidání položek do fields
        for fields_list in section_fields.values():
            fields += fields_list

        # Vytvoření slovníku pro vykreslení položek
        widgets = {
            'display_footer_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'display_footer_end_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        # Nastavení widgetů pro jednotlivé položky
        for section, fields_list in section_fields.items():
            for field in fields_list:

                # Pokud je pole součástí sociálních účtů nebo končí URL
                if field in social_accounts or field.endswith('_url'):
                    widgets[field] = forms.URLInput(attrs={'class': 'form-control'})

                # Pokud je pole součástí vybraných článků
                elif section == 'selected_articles':
                    widgets[field] = forms.Select(attrs={'class': 'form-control'})

                # Pro ostatní sekce
                else:
                    widgets[field] = forms.TextInput(attrs={'class': 'form-control'})

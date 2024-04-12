from homepage.models.footer_section import FooterSettings
from articles.models.article import Article


def save_footer_data(form):
    '''
    Ukládá data formuláře do modelu sekce patičky.

    Tato metoda je volaná pohledem EditFooterSection a slouží k uložení dat z POST požadavku.
    :param form: Formulář obsahující data k uložení.
    :return: None
    '''

    # Načtení instance pro footer
    instance = FooterSettings.singleton()

    # Uložení hodnoty do pole zobrazení footeru
    instance.display_footer_section = form.cleaned_data.get('display_footer_section')

    # Uložení hodnot do slovníku adresy
    fields = ['company_name', 'address', 'phone', 'email']
    for field in fields:
        instance.address_values[field]['value'] = form.cleaned_data.get(field)

    # Uložení hodnot url do slovníku pro sociální stránky
    social_media_platforms = ['facebook', 'twitter', 'instagram', 'behance', 'pinterest']
    for platform in social_media_platforms:
        instance.social_media[platform]['url'] = form.cleaned_data.get(platform)

    # Uložení hodnot do slovníku pro odkazy na vybrané stránky
    for n in enumerate(instance.site_links, start=1):
        name_field = f"name_field_{n}"
        url_field = f"url_field_{n}"
        instance.site_links[f"site_links_{n}"]["name"] = form.cleaned_data.get(name_field)
        instance.site_links[f"site_links_{n}"]["url"] = form.cleaned_data.get(url_field)

    # Uložení hodnot do slovníku pro čvybrané články
    for n in enumerate(instance.articles, start=1):
        article_id = form.cleaned_data.get(f"article_{n}")
        if article_id != "0":
            article = Article.objects.get(pk=article_id)
            instance.articles[f"article_{n}"]["picture_path"] = article.main_picture_miniature
            instance.articles[f"article_{n}"]["title"] = article.title
            instance.articles[f"article_{n}"]["date"] = article.published.strftime("%B %d, %Y")
            instance.articles[f"article_{n}"]["article_url"] = article.get_absolute_url
            instance.articles[f"article_{n}"]["article_id"] = article.id

    # Uložení hodnot do slovníku pro poslední řádek patičky
    end_line_fields = ['display_footer_end_section', 'right_text', 'left_text', 'left_link_text', 'left_link_url']
    for field in end_line_fields:
        instance.end_line[field]['value'] = form.cleaned_data.get(field)

    # Uložení hodnot do databáze
    instance.save()


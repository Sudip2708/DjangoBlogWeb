from articles.models.article import Article

from ..footer_section import FooterSettings


def save_footer_data(form):
    '''
    Function for saving data from the form into the footer section model.

    This method is called by the EditFooterSection view and is used to save data from the POST request.
    '''

    # Load the instance for the footer
    instance = FooterSettings.singleton()

    # Save the value for the footer display field
    instance.display_footer_section = form.cleaned_data.get('display_footer_section')

    # Save values into the address dictionary
    fields = ['company_name', 'address', 'phone', 'email']
    for field in fields:
        instance.address_values[field]['value'] = form.cleaned_data.get(field)

    # Save URL values into the dictionary for social media platforms
    social_media_platforms = ['facebook', 'twitter', 'instagram', 'behance', 'pinterest']
    for platform in social_media_platforms:
        instance.social_media[platform]['url'] = form.cleaned_data.get(platform)

    # Save values into the dictionary for selected site links
    for n in enumerate(instance.site_links, start=1):
        name_field = f"name_field_{n}"
        url_field = f"url_field_{n}"
        instance.site_links[f"site_links_{n}"]["name"] = form.cleaned_data.get(name_field)
        instance.site_links[f"site_links_{n}"]["url"] = form.cleaned_data.get(url_field)

    # Save values into the dictionary for selected articles
    for n in enumerate(instance.articles, start=1):
        article_id = form.cleaned_data.get(f"article_{n}")
        if article_id != "0":
            article = Article.objects.get(pk=article_id)
            instance.articles[f"article_{n}"]["picture_path"] = article.main_picture_miniature
            instance.articles[f"article_{n}"]["title"] = article.title
            instance.articles[f"article_{n}"]["date"] = article.published.strftime("%B %d, %Y")
            instance.articles[f"article_{n}"]["article_url"] = article.get_absolute_url
            instance.articles[f"article_{n}"]["article_id"] = article.id

    # Save values into the dictionary for the last footer row
    end_line_fields = ['display_footer_end_section', 'right_text', 'left_text', 'left_link_text', 'left_link_url']
    for field in end_line_fields:
        instance.end_line[field]['value'] = form.cleaned_data.get(field)

    # Save values into the database
    instance.save()

from django.shortcuts import render
from django.contrib import messages
from PIL import Image


def resize_and_jpg_format(request, form, return_url):
    '''
    Funkce pro změnu obrázku na formát JPG a změnu velikosti pro obrázek z formuláře.

    :param request: Request z formuláře.
    :param form: Formulář s daty.
    :param return_url: Název návratové url.

    :return: Změna formátu a velikosti obrázku ve formuláři,
            nebo přerušení nahrávání dat a návrat na stránku s oznamem o chybě.
    '''


    try:

        # Otevření obrázku
        image = Image.open(form.cleaned_data['profile_picture'])

        # Změna velikosti
        image.thumbnail((300, 300))

        # Změna formátu
        image.convert("RGB").save(form.cleaned_data['profile_picture'], "JPEG")

    except ValueError as e:

        # Výpis chyby
        messages.error(request, str(e))

        # Návrat na stránku
        return render(request, return_url)


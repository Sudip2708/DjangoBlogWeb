from django.shortcuts import render
from django.contrib import messages
from PIL import Image


def resize_and_jpg_format(request, form, field_name, dimensions, return_url):
    '''
    Funkce pro změnu obrázku na formát JPG a změnu velikosti pro obrázek z formuláře.

    :param request: Request z formuláře.
    :param form: Formulář s daty.
    :param field_name: Název pole v modelu databáze.
    :param dimensions: Požadovaná velikost.
    :param return_url: Název návratové url.

    :return: Změna formátu a velikosti obrázku ve formuláři,
            nebo přerušení nahrávání dat a návrat na stránku s oznamem o chybě.
    '''

    print("############################################")
    print("### main/users/utils/resize_and_jpg_format.py")
    print()

    try:

        # Otevření obrázku
        image = Image.open(form.cleaned_data[field_name])

        # Změna velikosti
        image.thumbnail(dimensions)

        # Změna formátu
        image.convert("RGB").save(form.cleaned_data[field_name], "JPEG")

    except ValueError as e:

        # Výpis chyby
        messages.error(request, str(e))

        # Návrat na stránku
        return render(request, return_url)


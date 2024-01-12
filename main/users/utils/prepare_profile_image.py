from django.shortcuts import render
from django.contrib import messages
from PIL import Image
import os
from django.core.files.storage import default_storage



def resize_and_format_upload_image(request, form, field, dimensions, return_page):
    '''
    Funkce pro změnu obrázku na formát JPG a změnu velikosti pro obrázek z formuláře.

    :param form: Formulář s daty.
    :param field: Název pole obrázku.
    :param dimensions: Požadovaná velikost.
    :param return_page: Návratová stránka, pro případ neúspěchu.
    :return: Změna formátu a velikosti obrázku ve formuláři,
            nebo přerušení nahrávání dat a návrat na stránku s oznamem o chybě.
    '''

    try:

        # Otevření obrázku
        image = Image.open(form.cleaned_data[field])

        # Změna velikosti
        image.thumbnail(dimensions)

        # Změna formátu
        image.convert("RGB").save(form.cleaned_data[field], "JPEG")

    except ValueError as e:

        # Výpis chyby
        messages.error(request, str(e))

        # Návrat na stránku
        return render(request, return_page)



def delete_old_image(image_path):
    '''
    Funkce pro smazání obrázku.

    :param image: Obrázek.
    :return: Smazání obrázku.
    '''

    # Kontrola existence starého souboru
    image_exists = default_storage.exists(image_path)
    print("### image_exists")
    print(image_exists)
    print()

    # Smazání souboru pokud existuje
    if image_exists:
        default_storage.delete(image_path)




def rename_upload_image(image, image_name):
    '''
    Funkce pro přejmenování obrázku z formuláře.

    :param form: Formulář s daty.
    :param field: Název pole obrázku.
    :param image_name: Jméno obrázku.
    :return: Formulář s přejmenovaným obrázkem
    '''

    print("### image_name")
    print(image_name)
    print()
    print("### image.name")
    print(image.name)
    print()

    # Přejmenování obrázku
    image.name = image_name

    print("### image.name")
    print(image.name)
    print()



def prepare_image(request, form, instance):
    '''
    Zpracování nahrávaného profilového obrázku.

    :param form: Formulář s daty.
    :param instance: Instance modelu pro data formuláře.
    :return: Obrázek připravený na uložení.
    '''

    # Příprava dat
    if form.cleaned_data.get('profile_image'):

        # Název pole obrázku
        field = 'profile_image'

        # Návratová adresa
        return_page = 'profile_update.html'

        # Nahraný obrázek
        upload_image = instance.profile_image

        # Získání cesty k původnímu obrázku
        original_image_path = instance.tracker.previous(field).path

        # Získání názvu původního obrázku
        original_image_name = os.path.basename(original_image_path)

        # Získání cesty k původnímu obrázku
        image_path = f"images/profile_pictures/users/{original_image_name}"

    elif form.cleaned_data.get('author_profile_picture'):

        # Název pole obrázku
        field = 'author_profile_picture'

        # Návratová adresa
        return_page = 'profile_update.html'

        # Nahraný obrázek
        upload_image = instance.author_profile_picture

        # Získání cesty k původnímu obrázku
        original_image_path = instance.tracker.previous(field).path
        print("### original_image_path")
        print(original_image_path)
        print()

        # Získání názvu původního obrázku
        original_image_name = os.path.basename(original_image_path)
        print("### original_image_name")
        print(original_image_name)
        print()

        # Získání cesty k původnímu obrázku
        image_path = f"images/profile_pictures/authors/{original_image_name}"
        print("### image_path")
        print(image_path)
        print()

    # Požadovaný rozměr obrázku
    dimensions = (300, 300)

    # Změna velikosti a formátu
    resize_and_format_upload_image(request, form, field, dimensions, return_page)

    # Smazání původního obrázku
    delete_old_image(image_path)

    # Změna jména nahrávaného obrázku na jméno původního obrázku
    rename_upload_image(upload_image, original_image_name)

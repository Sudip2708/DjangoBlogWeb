from .resize_and_jpg_format import resize_and_jpg_format
from .delete_old_image import delete_old_image
from .rename_new_image import rename_new_image
import os


def change_profile_picture(request, form, instance, field_name, return_url):
    '''
    Zpracování nahrávaného profilového obrázku.

    :param request: Request z formuláře.
    :param form: Formulář s daty.
    :param instance: Instance modelu pro data formuláře.
    :param field_name: Název pole v modelu databáze.
    :param return_url: Název návratové url.

    :return: Obrázek připravený na uložení.
    '''


    print("############################################")
    print("### main/users/utils/change_profile_picture.py")
    print()


    # Požadovaný rozměr obrázku
    dimensions = (300, 300)

    # Změna velikosti a formátu
    resize_and_jpg_format(request, form, field_name, dimensions, return_url)

    # Získání názvu původního obrázku
    original_image_name = instance.profile_image_name

    # Získání cesty k původnímu obrázku
    image_path = os.path.join(instance.profile_image_directory, original_image_name)

    # Smazání původního obrázku
    delete_old_image(image_path)

    # Změna jména
    rename_new_image(form, instance, field_name, original_image_name)


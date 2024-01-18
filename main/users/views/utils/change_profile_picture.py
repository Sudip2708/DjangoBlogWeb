from .resize_and_jpg_format import resize_and_jpg_format
from .delete_old_image import delete_old_image
from .rename_new_image import rename_new_image
import os


def change_profile_picture(request, form, instance, return_url):
    '''
    Zpracování nahrávaného profilového obrázku.

    :param request: Request z formuláře.
    :param form: Formulář s daty.
    :param instance: Instance modelu pro data formuláře.
    :param field_name: Název pole v modelu databáze.
    :param return_url: Název návratové url.

    :return: Obrázek připravený na uložení.
    '''

    # Změna velikosti a formátu
    resize_and_jpg_format(request, form, return_url)

    # Smazání původního obrázku
    delete_old_image(instance.profile_picture_path)

    # Změna jména
    rename_new_image(form, instance)


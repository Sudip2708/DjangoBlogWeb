from django.core.files.storage import default_storage

def delete_old_image(image_path):
    '''
    Funkce pro smazání obrázku.

    :param image_path: Cesta k obrázku z media root + název obrázku
    :return: Smazání obrázku.
    '''

    # Kontrola existence starého souboru
    image_exists = default_storage.exists(image_path)

    # Smazání souboru pokud existuje
    if image_exists:
        default_storage.delete(image_path)



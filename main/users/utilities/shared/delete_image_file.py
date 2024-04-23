from django.core.files.storage import default_storage
from django.conf import settings
import os


def delete_image_file(image_path):
    '''
    Metoda pro smazání obrázku umístěného ve složce media

    Společná metoda pro main/users/models.py a main/articles/models/article_author.py

    :param image_path: Cesta k obrázku z media root + název obrázku
    :return: Ověření, zda obrázek existuje, a jeho smazání.
    '''

    # Definice OS cesty k souboru
    os_path_to_image = os.path.join(settings.MEDIA_ROOT, image_path)

    # Kontrola existence souboru
    image_exists = default_storage.exists(os_path_to_image)

    # Smazání souboru (pokud existuje)
    if image_exists:
        default_storage.delete(os_path_to_image)



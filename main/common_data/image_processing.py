import os
from PIL import Image

from .image_resize_and_crop import image_resize_and_crop


def image_processing(image_path, image_parameters, instance, name):
    '''
    Funkce na zpracování nového obrázku a nahrazení původního.

    Funkce je použita v těchto souborech:
    - articles/models/article_data/main_picture_processing.py
    - articles/models/article_author_data/profile_picture_processing.py
    - users/models/custom_user_data/profile_picture_processing.py

    Funkce očekává následující parametry:
    - image_path: Cesta k zpracovávanému obrázku.
    - image_parameters: Parametry pro zpracování obrázku.
    - id: ID instance pro
    - name: Pojmenování modelu k jakému se obrázek vstahuje.

    Funkce nejprve otevře obrázek v PIL a následně z parametrů vytáhne hodnoty
    pro poměr stran obrázku a pro požadovanou maximální šířku
    a po té volá funkci 'image_resize_and_crop' pro úpravu velikosti obrázku.

    Funkce následně vytváří proměné pro cestu k složce obrázku 'image_directory'
    a název soubory vygeneruje z hodnoty 'name', 'instance_id' a hodnoty pro šířku obrázku.
    Společně pak z těchto hodnot vytvoří absolutní cestu, pro uložení obrázku 'new_image_path'.

    Funkce následně překontroluje, zda se na této cestě nenachází už nějaký soubor.
    Pokud ano, pak jej smažem protože se jedná se o předešlí obrázek.

    Následně nový obrázek uloží na dané umístění.

    Funkce nakonec vytvoří a vrátí relativní cestu k obrázku.
    '''

    # Změna velikosti obrázku
    image = Image.open(image_path)
    new_aspect_ratio = image_parameters['aspect_ratio']
    new_width = image_parameters['width']
    processed_image = image_resize_and_crop(image, new_width, new_aspect_ratio)

    # Získání cesty pro uložení obrázku
    image_directory = os.path.dirname(image_path)
    new_image_name = f'{name}-{instance.id:08d}-{image_parameters["width"]:04d}.jpg'
    new_image_path = os.path.join(image_directory, new_image_name)

    # Odstranění původního obrázku
    if os.path.exists(new_image_path):
        os.remove(new_image_path)

    # Uložení nového obrázku do složky media
    processed_image.save(new_image_path)

    # Vytvoření a vrácení relativní cesty k obrázku
    relative_picture_path = os.path.join(instance.upload_path, new_image_name)
    return relative_picture_path
from django.utils.text import slugify
from django.conf import settings
from shutil import copyfile
import os

def create_profile_picture(email):

    # Cesta k defaultnímu obrázku
    default_image_path = 'images/profile_pictures/default.jpg'

    # Název souboru pro nový obrázek
    new_image_name = f"{slugify(email.replace('@', '_').replace('.', '_'))}_upp_300.jpg"
    new_image_path = f"images/profile_pictures/users/{new_image_name}"

    # Úplná cesta k souboru defaultního obrázku
    default_image_full_path = os.path.join(settings.MEDIA_ROOT, default_image_path)

    # Úplná cesta k novému souboru
    new_image_full_path = os.path.join(settings.MEDIA_ROOT, new_image_path)

    # Kopírování defaultního obrázku na nové místo
    copyfile(default_image_full_path, new_image_full_path)

    # Přidání vytvořeného souboru do pole profile_image
    return new_image_path
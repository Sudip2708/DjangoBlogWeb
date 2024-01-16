
from django.conf import settings
from shutil import copyfile
import os

def create_profile_picture(profile_image_directory, profile_image_name):

    # Cesta k defaultnímu obrázku ze složky media
    default_media_path = 'images/profile_pictures/default.jpg'
    default_os_path = os.path.join(settings.MEDIA_ROOT, default_media_path)

    # Cesta pro nový obrázek ze složky media
    new_media_path = f"{profile_image_directory}{profile_image_name}"
    new_os_path = os.path.join(settings.MEDIA_ROOT, new_media_path)

    # Kopírování defaultního obrázku na nové místo
    copyfile(default_os_path, new_os_path)

    # Navrácení cesty k novému obrázku ze složky media
    return new_media_path
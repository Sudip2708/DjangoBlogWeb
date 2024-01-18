
from django.conf import settings
from shutil import copyfile
import os

def create_profile_picture(profile_picture_path, default_profile_picture_path):

    # Cesta k defaultnímu obrázku ze složky media
    default_os_path = os.path.join(settings.MEDIA_ROOT, default_profile_picture_path)

    # Cesta pro nový obrázek ze složky media
    new_os_path = os.path.join(settings.MEDIA_ROOT, profile_picture_path)

    # Kopírování defaultního obrázku na nové místo
    copyfile(default_os_path, new_os_path)

    # Navrácení cesty k novému obrázku ze složky media
    return profile_picture_path
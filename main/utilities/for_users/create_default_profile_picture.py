
from django.conf import settings
from shutil import copyfile
import os

def create_default_profile_picture(user_profile_picture_path):
    '''
    Vytvoření defaultního profilového obrázku (při založení instance CustomUser)

    :param user_profile_picture_path: Definovaná cesta k profilovému obrázku uživatele
    :return: Definovaná cesta k profilovému obrázku uživatele
    '''

    # Definice proměnných
    default_profile_picture_path = 'images/profile_pictures/default.jpg'
    os_path_to_default_profile_picture = os.path.join(settings.MEDIA_ROOT, default_profile_picture_path)
    os_path_to_user_profile_picture = os.path.join(settings.MEDIA_ROOT, user_profile_picture_path)

    # Kopírování defaultního obrázku na nové místo
    copyfile(os_path_to_default_profile_picture, os_path_to_user_profile_picture)

    # Navrácení cesty k novému obrázku
    return user_profile_picture_path
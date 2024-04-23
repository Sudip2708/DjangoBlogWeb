from PIL import Image
from django.conf import settings
import os

from .delete_image_file import delete_image_file


def create_thumbnail(account):
    """
    Uloží miniaturu profilového obrázku do pole profile_picture_thumbnail.

    (+ smazání předešlé varianty)

    [hint]
    os.path.join("os_path", "file_path")
    settings.MEDIA_ROOT
    delete_image_file("image_path")
    with Image.open(image_os_path) as img:
    img.thumbnail((size), quality)
    img.save("os_path", 'format')
    """

    # Definice proměnných
    os_path_to_profile_picture = os.path.join(settings.MEDIA_ROOT, account.profile_picture_path)
    os_path_to_profile_picture_thumbnail = os.path.join(settings.MEDIA_ROOT, account.profile_picture_thumbnail_path)

    # Smazání předchozí miniatury
    delete_image_file(account.profile_picture_thumbnail_path)

    # Zpracování a uložení profilového obrázku
    with Image.open(os_path_to_profile_picture) as img:
        img.thumbnail((150, 150), resample=3)
        img.save(os_path_to_profile_picture_thumbnail, 'JPEG')

    # Přiřazení cesty k obrázku do databáze
    account.profile_picture_thumbnail = account.profile_picture_thumbnail_path

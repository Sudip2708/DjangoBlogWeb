from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import CustomUser
from PIL import Image
import os
from django.utils.text import slugify
from django.core.files.storage import default_storage


@receiver(pre_save, sender=CustomUser)
def pre_save_check_profile_picture(sender, instance, **kwargs):

    # Zkontroluj, zda došlo ke změně profile_picture
    if instance.tracker.has_changed('profile_image'):

        try:
            if instance.profile_image:

                # Přejmenování původního obrázku:
                # Získání původní cesty k souboru
                original_image_path = instance.tracker.previous('profile_image').path

                # Získání původního názvu souboru
                original_image_name = os.path.basename(original_image_path)

                # Vytvoření nového názvu souboru
                new_image_name = f"{os.path.splitext(original_image_name)[0]}_old{os.path.splitext(original_image_name)[1]}"

                # Složení nové cesty k souboru
                new_image_path = os.path.join(os.path.dirname(original_image_path), new_image_name)

                # Přejmenování souboru
                os.rename(original_image_path, new_image_path)

                # Přejmenování a úprava nového obrázku:
                # Otevři obrázek pomocí Pillow
                image = Image.open(instance.profile_image)

                # Změň rozměry obrázku na specifikované rozměry
                image.thumbnail((300, 300))

                # Převede obrázek na formát JPEG a uloží jej zpět do instance.profile_image
                image.convert("RGB").save(instance.profile_image.path, "JPEG")

                # Vytvoř nový název souboru
                new_image_name = f"{slugify(instance.email.replace('.', ''))}_pp_300.jpg"

                # Aktualizuj název
                instance.profile_image.name = new_image_name

                # Smazat soubor s "_old" příponou
                # Získání názvu starého a nového souboru
                old_image_path = f"images/profile_pictures/users/{slugify(instance.email.replace('.', ''))}_pp_300_old.jpg"

                # Kontrola existence starého souboru
                old_image_exists = default_storage.exists(old_image_path)

                # Smazání souboru pouze pokud existuje
                if old_image_exists:
                    default_storage.delete(old_image_path)


        except Exception as e:

            # Navrácení do původního stavu:
            # Získání názvu starého a nového souboru
            old_image_path = f"images/profile_pictures/users/{slugify(instance.email.replace('.', ''))}_pp_300_old.jpg"
            new_image_path = f"images/profile_pictures/users/{slugify(instance.email.replace('.', ''))}_pp_300.jpg"

            # Kontrola existence starého souboru
            old_image_exists = default_storage.exists(old_image_path)

            # Přejmenování souboru pouze pokud existuje
            if old_image_exists:
                default_storage.move(old_image_path, new_image_path)

            # Výpis do konzole o chybě (změnit na message)
            print(f"Error processing image: {e}")





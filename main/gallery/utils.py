from PIL import Image
import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def process_and_save_image(instance, image_field, dimensions, tag):
    try:
        # Získej název souboru a cestu k němu
        file_path = image_field.path

        print(f"@@@@@@@@@@@@@File path: {file_path}")

        # Převede obrázek na formát JPEG
        new_file_path = os.path.join("images/profile_pictures/users/", f"{instance.email.split('@')[0].lower()}_{tag}.jpg")

        # Otevři obrázek pomocí Pillow
        image = Image.open(file_path)

        # Změň rozměry obrázku na specifikované rozměry
        image.thumbnail(dimensions)

        # Ulož změněný obrázek na novou cestu
        image.convert("RGB").save(new_file_path, "JPEG")

        # Aktualizuj cestu k profilovému obrázku v databázi
        image_field.name = new_file_path

        # Ulož změny v instanci do databáze
        instance.save()

    except Exception as e:
        # Pokud dojde k chybě při zpracování obrázku, vyvolá výjimku s chybovou zprávou
        raise ValidationError(_("Nelze zpracovat obrázek. Chyba: ") + str(e))

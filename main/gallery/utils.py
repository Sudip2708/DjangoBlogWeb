from django.core.files.storage import default_storage
from django.utils.text import slugify
from PIL import Image
import os

def process_profile_image(form, field, dimensions, return_page):
    '''
    Funkce pro změnu obrázku na formát JPG a změnu velikosti - v případě neúspěchu nevyvolá chybu

    '''

    # Změna parametrů obrázku
    try:

        # Otevření obrázku
        image = Image.open(form.cleaned_data[field])

        # Změna velikosti
        image.thumbnail(dimensions)

        # Změna formátu
        image.convert("RGB").save(form.cleaned_data[field].path, "JPEG")


    # V případě neúspěchu:
    except ValueError as e:

        # Vytvoření zprávy o chybě
        messages.error(request, str(e))

        # Návrat na stránku
        return render(request, return_page)

# # Získání nového jména obrázku
# new_image_name = f"{slugify(instance.email.replace('@', '_').replace('.', '_'))}{image_tag}.jpg"
#
# # Změna názvu
# instance.profile_image.name = new_image_name


# def delete_image(image_path):
#     '''
#     Funkce pro smazání obrázku
#
#     :param image_path: Cesta k obrázku
#     :return: Smazání obrázku
#     '''
#
#     # Načtení cesty obrázku
#     image_exists = default_storage.exists(image_path)
#
#     # Kontrola zda existuje
#     if image_exists:
#
#         # Smazání obrázku
#         default_storage.delete(image_path)


def rename_image(original_image_path, new_image_name):
    '''
    Funkce pro přejmenování obrázku

    :param original_image_path:
    :return:
    '''
    original_image_name = os.path.basename(original_image_path)
    new_image_name = f"{os.path.splitext(original_image_name)[0]}_old{os.path.splitext(original_image_name)[1]}"
    new_image_path = os.path.join(os.path.dirname(original_image_path), new_image_name)
    os.rename(original_image_path, new_image_path)

# def process_and_rename_new_image(instance, new_image_name, dimensions):
#     image = Image.open(instance.profile_image)
#     image.thumbnail(dimensions)
#     image.convert("RGB").save(instance.profile_image.path, "JPEG")
#     instance.profile_image.name = new_image_name
#
#
#
# def recreate_old_file(instance, storage, old, new):
#     old_image_path = f"{storage}{old}"
#     new_image_path = f"{storage}{new}"
#     old_image_exists = default_storage.exists(old_image_path)
#     new_image_exists = default_storage.exists(new_image_path)
#     if old_image_exists:
#         if new_image_exists:
#             pass
#         else:
#             default_storage.move(old_image_path, new_image_path)


# def image_resize_and_convert_to_jpg(instance, dimensions):
#     '''
#     Funkce pro změnu obrázku na formát JPG a změnu velikosti
#
#     :param instance:
#     :param dimensions:
#     :return:
#     '''
#
#     # Otevření obrázku
#     image = Image.open(instance.profile_image)
#
#     # Změna velikosti
#     image.thumbnail(dimensions)
#
#     # Změna formátu
#     image.convert("RGB").save(instance.profile_image.path, "JPEG")






# from PIL import Image
# import os
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _
#
# def process_and_save_image(instance, image_field, dimensions, tag):
#     try:
#         # Získej název souboru a cestu k němu
#         file_path = image_field.path
#
#         print(f"@@@@@@@@@@@@@File path: {file_path}")
#
#         # Převede obrázek na formát JPEG
#         new_file_path = os.path.join("images/profile_pictures/users/", f"{instance.email}_{tag}.jpg")
#
#         # Otevři obrázek pomocí Pillow
#         image = Image.open(file_path)
#
#         # Změň rozměry obrázku na specifikované rozměry
#         image.thumbnail(dimensions)
#
#         # Ulož změněný obrázek na novou cestu
#         image.convert("RGB").save(new_file_path, "JPEG")
#
#         # Aktualizuj cestu k profilovému obrázku v databázi
#         image_field.name = new_file_path
#
#         # Ulož změny v instanci do databáze
#         instance.save()
#
#     except Exception as e:
#         # Pokud dojde k chybě při zpracování obrázku, vyvolá výjimku s chybovou zprávou
#         raise ValidationError(_("Nelze zpracovat obrázek. Chyba: ") + str(e))

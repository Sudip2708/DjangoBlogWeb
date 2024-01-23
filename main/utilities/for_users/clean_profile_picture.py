from django import forms
from PIL import Image
from django.core.files.storage import default_storage
from utilities.shared.delete_image_file import delete_image_file
from utilities.shared.resize_and_square_crop_image import resize_and_square_crop_image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


def clean_profile_picture(form):
    '''
    Validace a zpracování profilového obrázku

    :param form: Formulář s obrázkem
    :return: Formulář s upraveným obrázkem, nebo chybu
    '''

    # Načtení obrázku
    new_image = form.cleaned_data['profile_picture']

    # Ověření, zda jde u obrázek uložit jako jpg
    try:
        # Otevření souboru
        edited_image = Image.open(new_image)

        # Změna velikosti
        edited_image = resize_and_square_crop_image(edited_image, target_size=300)

        # Převod na formát JPEG do bufferu
        buffer = BytesIO()
        edited_image.save(buffer, format='JPEG')

        # Vytvoření nového InMemoryUploadedFile s formátem JPEG z buferu
        field_name = 'profile_picture'
        picture_name = form.instance.profile_picture_name
        file_type = 'image/jpeg'
        context_type = None
        new_image = InMemoryUploadedFile(
            buffer,  # Výstupní buffer
            field_name,  # field_name
            picture_name,  # název souboru
            file_type,  # MIME typ
            buffer.tell(),  # velikost souboru
            context_type  # content_type_extra
        )

    # Navrácení oznamu při neúspěšném průběhu
    except Exception as e:
        error_message = "Nepodařilo se změnit obrázek na formát JPEG. Zkontrolujte, zda je obrázek ve správném formátu."
        raise forms.ValidationError(error_message)


    # Smazání starého souboru:
    old_image_path = form.instance.profile_picture_path
    delete_image_file(old_image_path)


    # Uložení nového obrázku do pole profile_picture
    form.instance.profile_picture = new_image

    return form






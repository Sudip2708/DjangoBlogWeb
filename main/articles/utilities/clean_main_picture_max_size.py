from django import forms
from PIL import Image
from django.core.files.storage import default_storage
from articles.utilities.shared.delete_image_file import delete_image_file
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


def clean_main_picture_max_size(form):
    '''
    Validace a zpracování hlavního obrázku

    :param form: Formulář s obrázkem
    :return: Formulář s upraveným obrázkem, nebo chybu
    '''

    # Načtení obrázku
    new_image = form.cleaned_data['main_picture_max_size']

    # Ověření, zda jde u obrázek uložit jako jpg
    try:

        # Otevření souboru
        edited_image = Image.open(new_image)

        # Změna velikosti
        edited_image.thumbnail((1920, 1920))

        # Převod na formát JPEG do bufferu
        buffer = BytesIO()
        edited_image.save(buffer, format='JPEG')

        # Vytvoření nového InMemoryUploadedFile s formátem JPEG z buferu
        field_name = 'main_picture_max_size'
        picture_name = form.instance.main_picture_max_size_name
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
    old_image_path = form.instance.main_picture_max_size_path
    delete_image_file(old_image_path)

    # Uložení nového obrázku do pole profile_picture
    form.instance.main_picture_max_size = new_image
    # form.cleaned_data['main_picture_max_size'] = new_image


    return form






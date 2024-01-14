
def rename_new_image(form, instance, field_name, original_image_name):
    '''
    Funkce pro přejmenování obrázku

    :param form: Formulář s daty.
    :param instance: Instance modelu pro data formuláře.
    :param field_name: Název pole v modelu databáze.
    :param original_image_name: Požadovaný název obrázku.

    :return: Přejmenovaný obrázek na původní jméno souboru.
    '''


    print("############################################")
    print("### main/users/utils/rename_new_image.py")
    print()


    # Změna jména
    if form.cleaned_data.get('profile_image'):
        instance.profile_image.name = original_image_name
        form.cleaned_data[field_name] = original_image_name

    elif form.cleaned_data.get('author_profile_picture'):
        instance.author_profile_picture.name = original_image_name
        form.cleaned_data[field_name] = original_image_name

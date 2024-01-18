
def rename_new_image(form, instance):
    '''
    Funkce pro přejmenování obrázku

    :param form: Formulář s daty.
    :param instance: Instance modelu pro data formuláře.
    :return: Přejmenovaný obrázek na původní jméno souboru.
    '''

    # Změna jména
    if form.cleaned_data.get('profile_picture'):
        instance.profile_picture.name = instance.profile_picture_name
        form.cleaned_data['profile_picture'] = instance.profile_picture_name


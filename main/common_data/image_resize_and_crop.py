def image_resize_and_crop(image, new_width='as_original', new_aspect_ratio='as_original'):
    '''
    Funkce pro zmenšení a oříznutí obrázku.

    Funkce je součástí souboru common_data/image_processing.py,
    který je použit v těcto souborech:
    - articles/models/article_data/main_picture_processing.py
    - articles/models/article_author_data/profile_picture_processing.py
    - users/models/custom_user_data/profile_picture_processing.py

    Funkce očekává následující parametry:
    - image = Obrázek otevřený v PIL.
    - new_width = Požadovaná šířka obrázku v px (nepovinný parametr).
    - new_aspect_ratio = Požadovaný poměr stran nového obrázku (šířka/výška) (nepovinný parametr).

    Funkce nejprve vytvoří kopii obrázku a definuje základní proměnné:
    - width = Hodnota šířky obrázku (v px).
    - height = Hodnota výšky obrázku (v px).
    - image_aspect_ratio = Hodnota poměru stran.

    Poté funkce zkontroluje, zda bylo uvedeno, že se nemá měnit poměr stran
    (new_aspect_ratio='as_original'). Pokud ano, dopočte hodnotu pro new_aspect_ratio
    z výšky a šířky obrázku (to je potřeba pro případ, že se obrázek bude zmenšovat a bude potřeba vypočítat jeho výšku).

    Pokud je nastavena hodnota pro poměr stran (new_aspect_ratio),
    funkce nejprve zjistí, zda je nový poměr větší než poměr stran u obrázku.
    Pokud ano, vypočte dle nového poměru novou výšku a nastaví hodnoty pro oříznutí.
    Pokud ne, vypočte dle nového poměru novou šířku a nastaví hodnoty pro oříznutí.
    Následně funkce ořízne obrázek dle vypočítaných údajů.

    Poté funkce zkontroluje, zda byla zadána požadovaná šířka obrázku
    a zda šířka obrázku je větší než požadovaná šířka.
    Pokud ano, vypočte dle poměru i požadovanou výšku a obrázek zmenší.

    Funkce vrací upravený obrázek otevřený v PIL.
    '''

    # Vytvoření kopie obrázku a definice základních proměnných
    new_image = image.copy()
    width, height = image.size
    image_aspect_ratio = width / height

    # Když se nemá měnit poměr stran
    if new_aspect_ratio == 'as_original':
        # Nastaví poměr stran obrázku jako požadovaný poměr stran
        new_aspect_ratio = image_aspect_ratio
    else:
        if new_aspect_ratio > image_aspect_ratio:
            # Když je nový rozměr 'širší' než původní obrázek (bude se ořezávat výška)
            img_height = int(width / new_aspect_ratio)
            top = (height - img_height) / 2
            bottom = height - top
            left, right = 0, width
        else:
            # Když je nový rozměr 'užší' než původní obrázek (bude se ořezávat šířka)
            img_width = int(height * new_aspect_ratio)
            left = (width - img_width) / 2
            right = width - left
            top, bottom = 0, height
        # Oříznutí obrázku
        new_image = new_image.crop((left, top, right, bottom))

    # Když je zadána požadovaná šířka a šířka obrázku je větší než požadovaná šířka
    if new_width != 'as_original' and width > new_width:
        # Vypočte požadovanou výšku a zmenší obrázek
        new_height = int(new_width / new_aspect_ratio)
        new_image = new_image.resize((new_width, new_height))

    return new_image

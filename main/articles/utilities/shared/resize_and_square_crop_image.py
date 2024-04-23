
def resize_and_square_crop_image(image, target_size):
    '''
    Zmenší daný obrázek na požadovaný rozměr ožíznutím delší strany

    :param image: Instance obrázku k spracování
    :param target_size: Velikost v px
    :return: Zpracovaný obrázek
    '''

    # Zjištění poměru stran
    aspect_ratio = image.width / image.height

    # Nastavení výšky a šířky
    if aspect_ratio < 1:
        width = target_size
        height = int(target_size / aspect_ratio)
    else:
        width = int(target_size * aspect_ratio)
        height = target_size

    # Změna velikosti
    image = image.resize((width, height))

    # Oříznutí obrázku
    left = (width - target_size) / 2
    top = (height - target_size) / 2
    right = (width + target_size) / 2
    bottom = (height + target_size) / 2
    image = image.crop((left, top, right, bottom))

    return image



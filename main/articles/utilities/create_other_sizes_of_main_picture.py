from PIL import Image
from articles.utilities.shared.resize_and_square_crop_image import resize_and_square_crop_image
from articles.utilities.shared.delete_image_file import delete_image_file
import os
from django.conf import settings


def create_other_sizes_of_main_picture(article):
    '''
    Metoda vytvoří z nahraného hlavního obrázku článku, další tři varianty:

    Varianta pro článek 800 px
    Varianta pro náhled 450 px (čtverec)
    Varianta pro miniaturu 120px (čtverec)

    :param article: Instance článku

    :return: Vytvoří a uloží zmíněné varianty.
    '''

    # Smazání předešlých souborů (pokud existují)
    delete_image_file(article.main_picture_for_article_path)
    delete_image_file(article.main_picture_preview_path)
    delete_image_file(article.main_picture_miniature_path)

    os_path_to_main_picture_max_size = os.path.join(
        settings.MEDIA_ROOT,
        article.main_picture_max_size_path
    )

    # Zpracování a přeuložení obrázku do jeho dalších 3 variant
    with Image.open(os_path_to_main_picture_max_size) as img:

        # Varianta pro článek
        img.thumbnail((800, 800), resample=3)
        os_path = os.path.join(settings.MEDIA_ROOT, article.main_picture_for_article_path)
        img.save(os_path, 'JPEG')
        article.main_picture_for_article = article.main_picture_for_article_path

        # Varianta pro náhled
        target_size = 450
        img = resize_and_square_crop_image(img, target_size)  # Oříznutí na 450x450
        os_path = os.path.join(settings.MEDIA_ROOT, article.main_picture_preview_path)
        img.save(os_path, 'JPEG')
        article.main_picture_preview = article.main_picture_preview_path

        # Varianta pro miniaturu
        img.thumbnail((150, 150), resample=0)
        os_path = os.path.join(settings.MEDIA_ROOT, article.main_picture_miniature_path)
        img.save(os_path, 'JPEG')
        article.main_picture_miniature = article.main_picture_miniature_path

    # Uložení změn do databáze
    article.save()
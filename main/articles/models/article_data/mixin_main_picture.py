from django.db import models

from .main_picture_processing import main_picture_processing


class MainPictureMixin(models.Model):
    '''
    Mixin for the Article model adding fields for storing various sizes of the main article image.

    The mixin defines these attributes:
    - default_picture: Path from Media to the default image (used when creating an instance without specifying an image).
    - upload_path: Path from Media to store all sizes of the main article image.
    - new_picture: Boolean value indicating whether a new image has been uploaded (set in the form
        after receiving a new image file and captured in the post_save signal for image processing).

    Fields created by this mixin:
    - main_picture_max_size: Largest size of the image for full-screen display.
        (maximum dimensions: 1920px / 1080px, minimum dimensions: 800px / 800px)
    - main_picture_for_article: Medium size of the image for use on the article page.
        (maximum width: 440px, minimum width: 800px)
    - main_picture_preview: Smaller size of the image for display on the article list page.
        (cropped to a 4:3 aspect ratio and resized to 440px / 330px)
    - main_picture_thumbnail: Thumbnail used for article links.
        (cropped to square format and resized to 150px)

    The mixin defines an inner Meta class to set abstract behavior.
    (It does not create its own ID or table in the database.)

    The mixin contains the method 'picture_processing',
    which creates various size variants of the uploaded image.
    '''

    default_picture = 'images/articles/no-image.jpg'
    upload_path = 'images/articles/main_picture/'
    new_picture = False

    main_picture_max_size = models.ImageField(
        'Article Main Picture Max-Size',
        default=default_picture,
        upload_to=upload_path,
    )

    main_picture_for_article = models.ImageField(
        'Article Main Picture',
        default=default_picture,
        upload_to=upload_path,
    )

    main_picture_preview = models.ImageField(
        'Article Main Picture Preview',
        default=default_picture,
        upload_to=upload_path,
    )

    main_picture_thumbnail = models.ImageField(
        'Article Main Picture Miniature',
        default=default_picture,
        upload_to=upload_path,
    )

    class Meta:
        abstract = True

    def main_picture_processing(self):
        ''' Method for creating size variants of the main article image. '''
        return main_picture_processing(self)

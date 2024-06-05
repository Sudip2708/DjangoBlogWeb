from django.db import models

from users.models.custom_user import CustomUser
from .article_author_data.profile_picture_processing import profile_picture_processing


class ArticleAuthor(models.Model):
    '''
    Model representing an article author.

    This model stores information about the user who is the author of an article
    and includes the following fields:
    - linked_user: Field linking the author's account to the user account using a "one-to-one" relationship with the CustomUser model.
    - name: Field for the author's display name, which appears in connection with their articles.
    - slug: Field for a unique "slug" used to create a URL derived from the author's name.
    - profile_picture: Field for the author's profile picture.
    - profile_picture_thumbnail: Field for the thumbnail of the author's profile picture.

    The model defines these attributes for profile pictures:
    - default_picture: Path from Media to the default image (used when creating an instance without specifying an image).
    - upload_path: Path from Media to store all sizes of the main image.
    - new_picture: Boolean value indicating whether a new image has been uploaded (set in the form
        after receiving a new image file and captured in the post_save signal for image processing).

    Model methods:
    - __str__: Obtains the textual representation of the model (based on the author's name field value).
    - profile_picture_processing: Method for processing the profile picture.

    The model has several pre_save, post_save, pre_delete, and post_delete signals attached to it,
    processing its content.
    '''

    linked_user = models.OneToOneField(
        CustomUser,
        verbose_name='Linked User',
        related_name='linked_author',
        null=True,
        on_delete=models.SET_NULL,
    )

    name = models.CharField(
        verbose_name='Author Name',
        blank=True,
        unique=True,
        max_length=50,
    )

    slug = models.SlugField(
        verbose_name='Author Slug',
        blank=True,
        unique=True,
    )

    default_picture = 'images/profile_pictures/default.jpg'
    upload_path = 'images/profile_pictures/authors/'
    new_picture = False

    profile_picture = models.ImageField(
        verbose_name='Profile Picture',
        default=default_picture,
        upload_to=upload_path,
    )

    profile_picture_thumbnail = models.ImageField(
        verbose_name='Profile Picture Thumbnail',
        default=default_picture,
        upload_to=upload_path,
    )

    def __str__(self):
        return self.name

    def profile_picture_processing(self):
        ''' Method for processing the profile picture (and creating a thumbnail). '''
        return profile_picture_processing(self)

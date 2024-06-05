from django.contrib.auth.models import AbstractUser
from django.db import models

from .custom_user_data.managers import CustomUserManager
from .custom_user_data.mixin_settings import UserSettingsMixin
from .custom_user_data.profile_picture_processing import profile_picture_processing


class CustomUser(AbstractUser, UserSettingsMixin):
    '''
    Class defining field settings for authenticated users.

    The class inherits from:
    - AbstractUser: Class providing implementation of common functions for managing user accounts.
    - UserSettingsMixin: Class for separating content for managing and setting sidebar panels.

    The class creates or overrides these fields:
    - email: User's email.
    - username: User-chosen username.
    - username_slug: Slug for the user-chosen username (for URL).
    - profile_picture: User's profile picture.
    - profile_picture_thumbnail: Thumbnail of the profile picture.

    From the UserSettingsMixin mixin, the class inherits these fields:
    - sidebar_settings: Field for a dictionary with data for setting the appearance of the sidebar.
    - sidebar_order: Field for a dictionary with data for setting the order of sidebar panels.
    - settings: Field for a dictionary with data for additional user settings.

    It also inherits these fields from the AbstractUser class:
    - id: User's identification number.
    - password: User's password.
    - first_name: User's first name.
    - last_name: User's last name.
    - date_joined: Date of registration.
    - last_login: Date of the last login.
    - is_superuser: Setting whether the user is also a superuser.
    - is_staff: Setting whether the user is in the staff group.
    - is_active: Setting whether the user is logged in.
    - groups: Settings for groups to which the user belongs.
    - user_permissions: User's permissions settings.

    The class defines these attributes for profile pictures:
    - default_picture: Path from Media to the default picture (used when creating an instance without specifying an image).
    - upload_path: Path from Media to save all size variants of the main image.
    - new_picture: Boolean value indicating whether a new image has been uploaded (set in the form after receiving a new image file and captured in the post_save signal for image processing).

    Furthermore, the class sets:
    - USERNAME_FIELD: Definition of the field to be used as the primary identifier for login (here 'email').
    - REQUIRED_FIELDS: Overriding the default value ('email') with the value for 'username' to resolve conflicts with migration.

    And it sets a custom manager via 'objects',
    which should be used to change the user and superuser identification settings (from username to email).

    Methods defined in this part of the model:
    - __str__: Getting the text representation of the model (based on the value of the author's name field).
    - profile_picture_processing: Method for processing the profile picture.

    Methods defined in UserSettingsMixin:
    - get_sorted_sidebar_panels: Method returns data for rendering sidebar panels in the specified order.
    - change_sidebar_bool_value: Method for changing boolean values for sidebar settings.
    - change_sidebar_order_value: Method for changing the order of sidebar panels.
    - change_settings_bool_value: Method for changing boolean values for additional user settings.
    '''

    email = models.EmailField(
        verbose_name='Email',
        unique=True
    )

    username = models.CharField(
        verbose_name='User Name',
        blank=True,
        unique=True,
        max_length=50,
    )

    slug = models.SlugField(
        verbose_name='Username Slug',
        blank=True,
        unique=True,
    )

    default_picture = 'images/profile_pictures/default.jpg'
    upload_path = 'images/profile_pictures/users/'
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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.slug

    def profile_picture_processing(self):
        ''' Method for processing the profile picture (and creating a thumbnail). '''
        return profile_picture_processing(self)

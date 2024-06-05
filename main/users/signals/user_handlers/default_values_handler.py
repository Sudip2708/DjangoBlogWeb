from django.utils.text import slugify

from common_data.get_unique_value import get_unique_value


def handle_default_values_pre_save(user):
    '''
    Handler to capture the pre_save signal for checking default values.

    First, the handler checks if the username field is empty.
    If so, it creates a new username based on the front part of the email
    and the function for creating a unique value within the model field 'get_unique_value'.

    Then, the handler checks if the value of the 'slug' field matches the value of the 'username' field.
    If not, it updates this field with the correct value.
    '''

    # Creating a unique username
    if not user.username:
        user_class = user._meta.model
        field = 'username'
        value = slugify(user.email.split('@')[0])
        user.username = get_unique_value(user_class, field, value)

    # Checking if slug matches the current username
    if user.slug != slugify(user.username):
        user.slug = slugify(user.username)

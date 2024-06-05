from django.utils.text import slugify

from common_data.get_unique_value import get_unique_value


def handle_default_values_pre_save(author):
    '''
    Handler to capture the pre_save signal for checking default values.

    First, the handler checks if the field for the username is not empty.
    If it is, it creates a new username based on the front part of the email
    and the function to create a unique value within the model field 'get_unique_value'.

    Then, the handler checks if the value of the 'slug' field corresponds to the value of the 'username' field.
    If not, it updates this field with the correct value.
    '''

    # Creating a unique username
    if not author.name:
        author_class = author._meta.model
        field = 'name'
        value = slugify(author.linked_user.username)
        author.name = get_unique_value(author_class, field, value)

    # Checking if the slug corresponds to the current username
    if author.slug != slugify(author.name):
        author.slug = slugify(author.name)

def get_unique_value(model, field, value):
    '''
    Function to verify the uniqueness of a given value within a model field.

    This function is used in the following files:
    - articles/signals/article_handlers/default_values_handler.py
    - articles/signals/article_author_handlers/default_values_handler.py
    - users/signals/user_handlers/default_values_handler.py

    The function expects these three parameters:
    - model: Instance of the model used for checking.
    - field: Model field where the check will take place.
    - value: Value to be verified within the field and model.

    The function first checks the value itself for uniqueness within the model field.
    If it's not unique, the function appends a digit 1 to the value and checks its uniqueness.
    This way, the function continues with a while loop until it finds an expression
    that doesn't exist in the database field.

    The function returns either the original input value (if it's unique)
    or the modified value with an added number.
    '''

    # Check if the provided value exists
    if model.objects.filter(**{field: value}).exists():

        suffix = 1
        new_value = f"{value}{suffix}"

        # Loop to find a unique value
        while model.objects.filter(**{field: new_value}).exists():
            suffix += 1
            new_value = f"{value}{suffix}"

        value = new_value

    return value

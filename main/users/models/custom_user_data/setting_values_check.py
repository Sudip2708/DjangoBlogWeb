def setting_values_check(dictionary, default_values):
    '''
    Function for checking dictionary items against default values.

    The function is used to update the settings list based on the list of default values.
    The function receives a dictionary to be checked and a dictionary with default settings.
    The function then iterates through all items of the dictionary with default settings
    and checks if the checked dictionary contains all keys
    that are present in the default values.

    If any key is missing or does not have a value filled in,
    it will be added (or updated) with the default value.

    The function returns the checked or updated dictionary.
    '''

    for key, value in default_values.items():
        dictionary.setdefault(key, value)
    return dictionary

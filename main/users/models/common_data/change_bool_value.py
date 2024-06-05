def change_bool_value(dictionary, field_key):
    '''
    Function for changing boolean values in a dictionary.

    This function receives a dictionary with the relevant data and a key,
    based on which it then searches for the entry in the dictionary
    and changes the boolean value to its opposite.

    The function returns the dictionary with updated data.
    '''

    try:
        dictionary[field_key] = not dictionary[field_key]
        return dictionary

    except Exception as e:
        print(f"###ERROR### change_sidebar_bool_value: {e}")

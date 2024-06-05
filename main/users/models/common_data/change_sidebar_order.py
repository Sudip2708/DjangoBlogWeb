def change_sidebar_order(dictionary, hash):
    '''
    Function for changing the order of sidebar panels.

    This function receives a dictionary with the names of the sidebar panels and their order as keys,
    and a hash containing information about the direction of movement (#MoveUp/#MoveDn)
    and information about which panel is being moved (the 7th character is an underscore,
    so the 8th character and beyond is the key name of the panel in the dictionary).

    The function first generates these two values from the received hash.
    Then it retrieves the value of the position of the currently moved sidebar panel.
    Afterwards, using the variable for the direction of movement, it calculates the new order value (+1/-1),
    and then iterates through the dictionary values and returns the key for the value that corresponds to the new position.

    Finally, the function swaps the values between these two dictionaries,
    and returns the modified dictionary.
    '''

    try:

        # Retrieving variables from the received hash
        move = hash[:7]
        actual_sidebar = hash[8:]

        # Getting the second sidebar (with which the position will be swapped)
        actual_position = dictionary[actual_sidebar]
        new_position = actual_position + (-1 if move == '#MoveUp' else +1)
        next_sidebar = next(key for key, value in dictionary.items() if value == new_position)

        # Swapping order values and returning the dictionary
        dictionary[actual_sidebar], dictionary[next_sidebar] = (
            dictionary[next_sidebar], dictionary[actual_sidebar]
        )
        return dictionary

    except Exception as e:
        print(f"###ERROR### change_sidebar_order_value: {e}")

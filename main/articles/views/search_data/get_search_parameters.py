def get_search_parameters(form_cleaned_data):
    '''
    Function for processing cleaned data obtained from a form.

    The function first creates a dictionary with search parameters from the cleaned data obtained from the form.
    If date values are provided in the data, it converts them to the required format.
    If an author instance is provided in the data, it converts it to their ID.

    The function returns a dictionary with processed data.
    '''

    # Creating a dictionary from form data
    search_parameters = {
        'query': form_cleaned_data.get('query'),
        'title': form_cleaned_data.get('search_in_title'),
        'overview': form_cleaned_data.get('search_in_description'),
        'content': form_cleaned_data.get('search_in_content'),
        'before': form_cleaned_data.get('date_to'),
        'after': form_cleaned_data.get('date_from'),
        'author': form_cleaned_data.get('author')
    }

    # Converting date to the 'yyyy-mm-dd' format
    if search_parameters['before']:
        formatted_date = search_parameters['before'].strftime("%Y-%m-%d")
        search_parameters['before'] = formatted_date

    # Converting date to the 'yyyy-mm-dd' format
    if search_parameters['after']:
        formatted_date = search_parameters['after'].strftime("%Y-%m-%d")
        search_parameters['after'] = formatted_date

    # Converting author instance to their ID
    if search_parameters['author']:
        author_id = search_parameters['author'].id
        search_parameters['author'] = str(author_id)

    return search_parameters

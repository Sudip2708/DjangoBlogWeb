from django.http import JsonResponse

def user_sidebar_appearance(request):
    '''
    View for changing boolean values in the database for sidebar settings.

    The view accepts a request received via AJAX from the page script.

    First, the view checks if it's a POST request and if the HTTP request is sent using JavaScript
    as an AJAX request (the header contains the value XMLHttpRequest).

    Then, the view retrieves the value 'menu_id' from the request, from which it removes the initial hash
    to obtain the name of the dictionary key for which the value is to be changed.

    Subsequently, the view calls the method 'change_sidebar_bool_value' of the user with this key,
    which changes the value of the respective key to its opposite (True/False),
    and upon successful execution, returns an empty dictionary.
    '''

    # Check if it's a POST request sent via AJAX
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':

        # Get the key for which the value is to be changed
        menu_id = request.POST.get('menu_id')
        field_id = menu_id[1:]

        # Call the method to change the value and return an empty dictionary
        request.user.change_sidebar_bool_value(field_id)
        return JsonResponse({})

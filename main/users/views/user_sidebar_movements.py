from django.http import HttpResponseRedirect

def user_sidebar_movements(request, hash):
    '''
    View for changing the order of sidebars.

    The view first verifies if the request contains a 'hash' requesting a change in the position of the sidebar,
    and if so, calls the method to change its order.

    Then, it retrieves the previous page and redirects to it.
    '''

    # Check if it's a sidebar movement and call the corresponding method
    if hash.startswith('#Move'):
        request.user.change_sidebar_order_value(hash)

    # Get the previous page link and redirect to it
    previous_page = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(previous_page)

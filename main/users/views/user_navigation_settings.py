from django.http import HttpResponseRedirect

def user_navigation_settings(request, hash):
    '''
    View for setting the visibility of navigation panels and the sidebar.

    This view handles the following dictionary keys:
    - show_sidebars: Visibility of sidebars.
    - show_category_navigation: Visibility of category navigation.
    - show_tab_for_similar: Visibility for navigation for similar articles.

    The view first loads the address of the page from which the request came.

    Then, it verifies whether the value of 'hash' starts with '#bool' (items for changing True/False),
    If yes, it generates a part from the hash containing the key to find the item in the dictionary.

    It then checks whether it's a request to change the visibility of the sidebar,
    or to change the visibility of category navigation,
    or to change the visibility of navigation for similar articles,
    and calls the corresponding method to make the change in the database.

    If it's a request to change the visibility of navigation for similar articles,
    the view checks if we are on the tab for similar articles for a given tag,
    if yes, it removes this part from the address.
    The view then checks if we are on the category tab for a given tag,
    if yes, it removes this part from the address.

    Both steps aim to ensure that when returning to a given tag,
    the page for that tag is loaded upon return and not a certain tab
    for the category articles of that tag or similar articles to that tag.

    Finally, the view either calls the modified return page for the given tag,
    or returns to the page where the request came from.
    '''

    # Get the link to the previous page
    previous_page = request.META.get('HTTP_REFERER', '/')

    # Verify the request and redirect to the corresponding method
    if hash.startswith('#bool'):
        key = hash[6:]

        # Request to change the visibility of sidebars
        if key == 'show_sidebars':
            request.user.change_sidebar_bool_value(key)

        # Request to change the visibility of category navigation
        elif key == 'show_category_navigation':
            request.user.change_settings_bool_value(key)

        # Request to change the visibility of navigation for similar articles
        elif key == 'show_tab_for_similar':
            request.user.change_settings_bool_value(key)

            # If we are on the tab for similar articles for a given tag, return to the page for that tag
            if '/similar/' in previous_page:
                previous_page = previous_page.split('/similar/')[0]

            # If we are on the category tab for a given tag, return to the page for that tag
            elif '/category/' in previous_page:
                previous_page = previous_page.split('/category/')[0]

    return HttpResponseRedirect(previous_page)

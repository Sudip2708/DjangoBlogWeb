def get_paginate_by(self, queryset):
    '''
    Method to determine the number of articles per page when paginating search results.

    This method is used in the following files:
    - articles/views/article_list.py
    - articles/views/my_articles.py
    - articles/views/search.py

    The method checks if the user has the sidebar displayed,
    and based on that, it determines the number of articles per page.
    If the user doesn't have the sidebar displayed,
    it returns a value of 6, otherwise, it returns a value of 4.
    '''
    if self.user.sidebar.get('show_sidebars'):
        return 4
    return 6

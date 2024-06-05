from taggit.models import Tag

def get_sorted_sidebar_panels(self):
    '''
    Method to create a list of sorted panels with data needed for rendering.

    The method first defines a list of dictionaries with values for rendering all panels.
    Then, it creates a new list for sorted order based on a loop that verifies the set panel order in the self.sidebar_order field.
    Based on this order, the method adds two keys to each dictionary in the list:
    - is_first: For the first panel.
    - is_last: For the last panel.
    These keys ensure that during rendering on the page, only one direction of movement is shown for the first and last panels.

    Subsequently, the method sorts the list according to the first value in the tuple (order value),
    and in the resulting list, it keeps only dictionaries.

    The method returns a list of dictionaries with data needed for rendering the sidebar panel,
    sorted according to the set order.
    '''

    from articles.models.article_category import ArticleCategory

    panels = [

        {'name': 'Search',
         'slug': 'search',
         'visible': self.sidebar.get('show_search_sidebar'),
         'template': '2_main/_sidebars/__search__.html',
         'show_options': self.sidebar.get('show_search_options'),
         },

        {'name': 'User',
         'slug': 'user',
         'visible': self.sidebar.get('show_user_sidebar'),
         'template': '2_main/_sidebars/__user__.html',
         'show_user_options': self.sidebar.get('show_user_options'),
         'show_author_options': self.sidebar.get('show_author_options'),
         },

        {'name': 'Category',
         'slug': 'category',
         'visible': self.sidebar.get('show_category_sidebar'),
         'template': '2_main/_sidebars/__category__.html',
         'show_options': self.sidebar.get('show_category_options'),
         },

        {'name': 'Tags',
         'slug': 'tags',
         'visible': self.sidebar.get('show_tags_sidebar'),
         'template': '2_main/_sidebars/__tags__.html',
         'show_options': self.sidebar.get('show_tags_options'),
         'tags': Tag.objects.all().order_by('?')[:20],
         }

    ]

    # Filling the list with tuples with assigned order value
    sorted_panels = []
    for panel in panels:
        order = self.sidebar_order.get(panel['slug'], float('inf'))
        panel['is_first'] = (order == 1)
        panel['is_last'] = (order == len(self.sidebar_order))
        sorted_panels.append((order, panel))

    # Sorting the order and keeping only dictionaries
    sorted_panels.sort(key=lambda x: x[0])
    sorted_panels = [panel for order, panel in sorted_panels]

    return sorted_panels

from taggit.models import Tag


def get_sorted_sidebar_panels(self):
    '''
    Metoda pro vytvoření seznamu setříděných panelů s daty potřebnými pro jejich vykreslení.

    Metoda nejprve definuje seznam slovníků s hodnotami pro vykreslení všech panelů.
    Metoda následně vytváří nový seznam pro setříděné pořadí a na základě cyklu,
    který ověřuje nastavené pořadí panelu v poli self.sidebar_order,
    a na základě tohoto pořadí přidává každému seznamu dva klíče:
    - is_first: Pro první panel.
    - is_last: Pro poslední panel.
    Které zajistí, že při vykreslení na stránce se u prvního a posledního panelu
    bude objevovat pro posun pouze jeden směr.

    Následně metoda setřídí seznam podle první hodnoty v tuple (hodnota pořadí)
    a ve výsledném seznamu pak ponechá pouze slovníky.

    Metoda vrací seznam slovníků s daty potřebnými pro vykreslení bočního panelu,
    setříděných dle nastaveného pořadí.
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

    # Naplnění seznamu s tuple s přiřazenou hodnotou pořadí
    sorted_panels = []
    for panel in panels:
        order = self.sidebar_order.get(panel['slug'], float('inf'))
        panel['is_first'] = (order == 1)
        panel['is_last'] = (order == len(self.sidebar_order))
        sorted_panels.append((order, panel))

    # Setřídění pořadí a ponechání pouze slovníků
    sorted_panels.sort(key=lambda x: x[0])
    sorted_panels = [panel for order, panel in sorted_panels]

    return sorted_panels

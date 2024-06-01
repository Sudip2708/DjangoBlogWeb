def get_paginate_by(self, queryset):
    '''
    Metoda pro určení počtu článků na stránce při stránkování výsledků vyhledávání.

    Metoda je použita v těchto souborech:
    - articles/views/article_list.py
    - articles/views/my_articles.py
    - articles/views/search.py

    Metoda zkontroluje zda má uživatele zapnutý postranní panel,
    a podle toho určí počet článků na stráncu.
    Pokud je uživatel nemá zobrazen postranní panel,
    vrátí hodnotu 6, jinak vrátí hodnotu 4.
    '''
    if self.user.sidebar.get('show_sidebars'):
        return 4
    return 6
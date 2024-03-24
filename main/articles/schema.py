print("### Schema: ArticleSchema")

import os
from whoosh.index import create_in, open_dir
from whoosh.fields import SchemaClass, TEXT, DATETIME, ID
from django.conf import settings


class ArticleSchema:
    '''
    Třída ArticleSchema definuje schéma pro indexování článků pomocí Whoosh.

    Tato třída umožňuje inicializaci a správu Whoosh indexu pro indexaci článků.
    Obsahuje metodu pro vytvoření indexu a definuje schéma, které se použije
    k indexaci jednotlivých atributů článků, jako jsou titulek, přehled, obsah,
    autor, datum vytvoření, datum aktualizace, datum publikace, tagy, kategorie
    a stav.
    '''


    def __init__(self):
        '''Inicializuje instanci schématu a vytváří Whoosh index.'''

        # Vytvoření Whoosh indexu
        self.ix = self.create_index()


    def create_index(self):
        '''
        Vytvoří index Whoosh v adresáři nastaveném v settings.

        :return: Inicializovaný index Whoosh.
        '''

        # Vytvoření složky
        if not os.path.exists(settings.INDEX_DIRECTORY):
            os.makedirs(settings.INDEX_DIRECTORY)

        # Načtení složky
        if not os.listdir(settings.INDEX_DIRECTORY):
            ix = create_in(settings.INDEX_DIRECTORY, self.get_schema())
        else:
            ix = open_dir(settings.INDEX_DIRECTORY)

        # Navrácení složky
        return ix


    def get_schema(self):
        '''
        Vrací schéma pro indexování článků.

        :return: Schéma pro indexování článků.
        '''

        return SchemaClass(
            id=ID(stored=True, unique=True),
            slug=ID(stored=True),

            title=TEXT(stored=True),
            overview=TEXT(stored=True),
            content=TEXT(stored=True),

            author=ID(stored=True),

            created=DATETIME(stored=True),
            updated=DATETIME(stored=True),
            published=DATETIME(stored=True),

            tags=ID(stored=True),
            category=ID(stored=True),
            status=TEXT(stored=True)
        )
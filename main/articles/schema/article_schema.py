import os
from whoosh.index import create_in, open_dir
from django.conf import settings
from whoosh.fields import SchemaClass, TEXT, DATETIME, ID

from .data.print_indexed_articles import print_indexed_articles
from .data.index_article import index_article
from .data.delete_article_from_index import delete_article_from_index
from .data.update_field_in_index import update_field_in_index


class ArticleSchema:
    '''
    Třída ArticleSchema definuje schéma pro indexování článků pomocí Whoosh.

    Třída umožňuje inicializaci a správu indexu Whoosh pro indexaci článků.
    Obsahuje metodu pro vytvoření indexu a definuje schéma,
    které se použije k indexaci jednotlivých atributů článků,
    kterými jsou: titulek, přehled, obsah, autor, datum publikace.

    Schéma je použito k efektivnějšímu fulltextovému vyhledávání v publikovaných článcích.
    Na schéma jsou tak navázány funkce spojené s obsluhou vyhledávání.
    Na třídu je také navázaná funkce rebuild_schema umístěná v modulu data,
    která slouží k reindexaci celého schématu.

    Tato třída obsahuje následující metody:
    - update_field_in_index: Pro aktualizaci konkrétního pole indexu.
    - delete_article_from_index: Pro smazání indexu článku.
    - index_article: Pro indexaci článku.
    - print_indexed_articles: Pro výpis názvů všech indexovaných článků.
    '''

    def __init__(self):
        ''' Inicializační metoda třídy. '''
        self.ix = self.create_index()

    def create_index(self):
        '''
        Metoda otvírá, nebo vytváří a navrací otevřený index z jeho umístění.

        Metoda create_index vytváří nebo otevírá index Whoosh
        v adresáři nastaveném v proměnné settings.INDEX_DIRECTORY.
        Pokud adresář ještě neexistuje, metoda ho vytvoří.
        Poté zkontroluje, zda je adresář prázdný.
        Pokud ano, vytvoří nový index s použitím schématu získaného pomocí metody get_schema().
        Pokud adresář již obsahuje nějaké soubory,
        metoda pouze otevře existující index v daném adresáři.

        Nakonec vrátí otevřený index.
        '''

        # Kontrola/vytvoření adresáře
        if not os.path.exists(settings.INDEX_DIRECTORY):
            os.makedirs(settings.INDEX_DIRECTORY)

        # Načtení a navrácení indexu
        if not os.listdir(settings.INDEX_DIRECTORY):
            ix = create_in(settings.INDEX_DIRECTORY, self.get_schema())
        else:
            ix = open_dir(settings.INDEX_DIRECTORY)

        return ix

    def get_schema(self):
        '''
        Metoda definuje pole instance schématu.

        Metoda vrací instanci třídy SchemaClass,
        která obsahuje definice polí (fields) pro indexování článků.
        '''

        return SchemaClass(
            id=ID(stored=True, unique=True),
            title=TEXT(stored=True),
            overview=TEXT(stored=True),
            content=TEXT(stored=True),
            author=ID(stored=True),
            published=DATETIME(stored=True),
        )

    def update_field_in_index(self, article_id, field_name, new_value):
        ''' Metoda pro aktualizaci konkrétního pole indexu. '''
        update_field_in_index(self, article_id, field_name, new_value)

    def delete_article_from_index(self, article_id):
        ''' Metoda pro smazání indexu článku. '''
        delete_article_from_index(self, article_id)

    def index_article(self, article):
        ''' Metoda pro indexaci článku. '''
        index_article(self, article)

    def print_indexed_articles(self):
        ''' Metoda pro výpis názvů všech indexovaných článků. '''
        print_indexed_articles(self)

from whoosh.index import open_dir
from django.conf import settings

def delete_article_from_index(self, article_id):
    '''
    Metoda třídy ArticleSchema pro smazání indexu článku.

    Tato metoda se používá k odstranění indexu článku,
    například v případě, kdy článek změní status a již není veřejný.

    Metoda očekává instanci článku.
    Nejprve otevře soubor s indexy a poté načte metody pro zápis (writen).
    Následně metoda odstraní záznamy z indexu a uloží změny.
    '''

    # Načtení souboru s indexem pro zápis.
    ix = open_dir(settings.INDEX_DIRECTORY)
    writer = ix.writer()

    # Odstranění dokumentu z indexu a uložení změn.
    writer.delete_by_term('id', str(article_id))
    writer.commit()

from whoosh.index import open_dir
from django.conf import settings

def update_field_in_index(self, article_id, field_name, new_value):
    '''
    Metoda třídy ArticleSchema pro aktualizaci konkrétního pole indexu.

    Metoda očekává následující údaje:
    article_id = ID článku, pro který má být aktualizace provedena.
    field_name = Jméno pole, které má být aktualizováno.
    new_value = Nová data pro toto pole.

    Nejprve metoda otevře soubor s indexy a poté načte metody pro zápis (writer).
    Následně aktualizuje data pro dané pole a článek a uloží změny.
    '''

    # Načtení souboru s indexem pro zápis.
    ix = open_dir(settings.INDEX_DIRECTORY)
    writer = ix.writer()

    # Aktualizace dat a uložení změn.
    writer.update_document(id=str(article_id), **{field_name: new_value})
    writer.commit()

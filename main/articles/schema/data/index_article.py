from whoosh.index import open_dir
from django.conf import settings
from bs4 import BeautifulSoup


def index_article(self, article):
    '''
    Metoda třídy ArticleSchema pro indexaci článku.

    Metoda očekává instanci článku, který má být indexován.
    Nejprve otevře soubor s indexy a poté načte metody pro zápis (writen).

    Poté načte obsah pole content, který je tvořen HTML obsahem od TinyMCE,
    a pomocí metod BeautifulSoup a get_text převede HTML text
    na normální text a poté odstraní bílé znaky na začátku a konci textu.

    Metoda přiřadí všechna indexovaná pole do indexu
    a uloží změny.
    '''

    # Načtení souboru s indexem pro zápis.
    ix = open_dir(settings.INDEX_DIRECTORY)
    writer = ix.writer()

    # Převod HTML obsahu na text.
    html_content = article.content
    text_content = BeautifulSoup(html_content, 'html.parser').get_text(strip=True)

    # Aktualizace hodnot polí v indexu a uložení změn.
    writer.update_document(
        id=str(article.id),
        title=article.title,
        overview=article.overview,
        content=text_content,
        author=str(article.author.id),
        published=article.published,
    )

    writer.commit()

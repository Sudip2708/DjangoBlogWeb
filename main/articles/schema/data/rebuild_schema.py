import os
import shutil
from whoosh.index import open_dir
from django.conf import settings

from ...models.article import Article


def rebuild_schema(self):
    '''
    Funkce pro smazání a znovuvytvoření celého schématu.

    Nejprve funkce zjišťuje, zda existuje složka pro schémata (podle umístění definovaného v settings.py).
    Pokud složka existuje, funkce nejprve uzavře index (pro případ, že by byl někde otevřen)
    a poté smaže celou složku pomocí příkazu shutil.rmtree().

    Poté funkce vytvoří novou složku pro index a zavolá metodu pro vytvoření indexu.

    Následně funkce načte všechny články ze modelu Article se statusem 'publish'
    a každý článek cyklem zapíše do indexu.
    '''

    # Načtení schématu
    from ...schema.article_schema import ArticleSchema

    # Smazání původní složky (pokud existuje)
    if os.path.exists(settings.INDEX_DIRECTORY):
        ix = open_dir(settings.INDEX_DIRECTORY)
        ix.close()
        shutil.rmtree(settings.INDEX_DIRECTORY)

    # Vytvoření nové složky s indexem
    os.makedirs(settings.INDEX_DIRECTORY)
    ArticleSchema().create_index()

    # Indexování článků
    articles = Article.objects.filter(status='publish')
    for article in articles:
        ArticleSchema().index_article(article)

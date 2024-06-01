import os

from ...schema.article_schema import ArticleSchema
from .delete_unused_tags_handler import handle_delete_unused_tags_post_save


def handle_article_pre_delete(article):
    '''
    Handler pro zachycení signálu pre_delete pro smazání článku.

    Handler nejprve ověří, zda je u článku nastavený status 'publish',
    pokud ano, znamená to, že je článek indexovaný ve Whoosh pro rychlejší fulltextové vyhledávání,
    a tak v další části kódu dojde k odstranění tohoto záznamu z indexu Whoosh.

    Handler dále vytvoří atribut '_picture_paths' obsahující prázdný seznam,
    a vytvoří seznam s poli pro různé velikosti hlavního obrázku článku.

    Následně cyklem projde všechna tato pole a pokud nejsou prázdná (což by neměla být),
    a pokud neobsahují odkaz na výchozí obrázek (což mohou),
    pak do seznamu '_picture_paths' přidá cestu k umístění tohoto obrázku.

    Handler dále naplní atribut pro odstraněné tagy 'tags_to_delete'
    všemi tagy z článku (tento seznam bude předán do post_delete signálu
    na kontrolu a případné smazání tagů, které již nejsou použity nikde jinde).
    '''

    # Odstranění z indexu Whoosh (je-li článek publikován)
    if article.status == 'publish':
        article_schema = ArticleSchema()
        article_schema.delete_article_from_index(article.id)

    # Vytvoření seznamu s cestami k obrázkům
    article._picture_paths = []
    picture_fields = [
        article.main_picture_max_size,
        article.main_picture_for_article,
        article.main_picture_preview,
        article.main_picture_thumbnail,
    ]

    # Naplnění seznamu hodnotami z instance článku
    for field in picture_fields:
        if field and field.name != article.default_picture:
            article._picture_paths.append(field.path)

    # Naplnění atributu 'tags_to_delete' všemi tagy článku.
    article.tags_to_delete = list(article.tags.names())


def handle_article_post_delete(article):
    '''
    Handler pro zachycení signálu post_delete pro smazání článku.

    Handler pracuje s atributem '_picture_paths' vytvořeným v handle_article_pre_delete.
    Handler v cyklu projde obsah tohoto seznamu a metodou getattr zkontroluje,
    zda obsahuje nějaké hodnoty pro cesty ke smazání.
    A pokud ano, nejprve ověří existenci souboru a poté soubor smaže.

    Handler dále volá handler, který zkontroluje a smaže ty tagy,
    které nejsou použity v žádném jiném článku.
    '''

    # Smazání obrázků
    for path in getattr(article, '_picture_paths', []):
        if os.path.exists(path):
            os.remove(path)

    # Kontrola a smazání nepoužívaných tagů
    handle_delete_unused_tags_post_save(article)


from articles.models.article_category import ArticleCategory
from articles.schema import ArticleSchema


def get_category_count():
    '''
    Získání počtu článků v každé kategorii.

    :return: Počet článků v každé kategorii - řazeno podle počtu sestupně
    '''

    # Získání všech kategorií
    categories = ArticleCategory().get_all_category_except_default

    # Inicializace slovníku pro ukládání počtu článků v každé kategorii
    category_counts = {}

    # Inicializace instance schématu Whoosh
    article_schema = ArticleSchema()

    # Pro každou kategorii získání počtu článků
    for category in categories:
        category_id = category.id

        # Získání všech článků v dané kategorii pomocí schématu Whoosh
        article_ids = article_schema.find_all_articles_by_category(category_id)

        # Počet článků v kategorii
        count = len(article_ids)

        # Uložení počtu článků do slovníku
        category_counts[category.title] = count

    # Seřazení slovníku podle počtu článků sestupně
    sorted_counts = dict(sorted(category_counts.items(), key=lambda item: item[1], reverse=True))

    print("### sorted_counts: ", sorted_counts)

    # Navrácení výsledu
    return []

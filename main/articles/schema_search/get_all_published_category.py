from articles.models.article_category import ArticleCategory
from articles.schema_methods.is_category_published import is_category_published



def get_all_published_category():
    '''
    Metoda pro získání všech publikovaných kategorií.

    Tato metoda získává všechny kategorie vyjma kategorie 'Uncategorized'.
    Prochází každou kategorií a ověřuje, zda má alespoň jeden článek se statusem 'publish'.
    Pokud ano, přidá tuto kategorii do seznamu.
    Nakonec navrátí seznam instancí kategorií, které mají alespoň jeden článek se statusem 'publish'.

    :return: Seznam instancí kategorií, které mají alespoň jeden článek se statusem 'publish'.
    '''

    # Získání všech kategorií vyjma 'Uncategorized'
    all_categories = ArticleCategory.get_all_category_except_default()

    # Seznam na kategorie, které mají alespoň jeden článek se statusem 'publish'
    check_categories = []

    # Cyklus na každou kategorii
    for category in all_categories:

        # Ověření, zda má alespoň jeden článek se statusem 'publish'
        if is_category_published(category.id):

            # Přidání kategorie do seznamu
            check_categories.append(category)

    # Navrácení seznamu instancí kategorii, které mají alespoň jeden článek se statusem 'publish'
    return check_categories


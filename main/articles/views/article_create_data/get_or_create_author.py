from ...models.article_author import ArticleAuthor


def get_or_create_author(user):
    '''
    Funkce pro získání instance autora na základě uživatelského jména.

    Funkce vyhledá dle instance uživatele instanci autora v modelu ArticleAuthor.
    Pokud uživatel nemá založený účet autora,
    vytvoří pro něj metodou 'get_or_create' nový.

    Funkce navrací instanci autora.
    '''

    author, created = ArticleAuthor.objects.get_or_create(linked_user=user)
    return author

### Definice podpůrných utils

from articles.models.article_author import ArticleAuthor


def get_author(user):
    '''
    Získání autora na základě uživatelského jménanebo jeho vytvoření.

    :param user: Instance uživatele
    :return: Instance autora
    '''

    # Získání, nebo vytvoření autora na základě dat uživatele
    author, created = ArticleAuthor.objects.get_or_create(user=user)

    # Navrácení výsledu
    return author

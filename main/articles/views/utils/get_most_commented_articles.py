### Definice podpůrných utils

from articles.models.article import Article


def get_most_commented_articles():
    '''
    Získání tří nejvíce komentovaných článků

    :return: Tří nejvíce komentované články
    '''

    # Vyhledání tří článků s největším počtem komentářů
    queryset = Article.objects.order_by('-comment_count')[:3]

    # Navrácení výsledu
    return queryset

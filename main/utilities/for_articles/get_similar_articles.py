### Definice podpůrných utils

from django.db.models import Count

from articles.models.article import Article


def get_similar_articles(article):
    '''
    Získání podobných článků na základě sdílených tagů.

    :param article: Instance článku
    :return: Tři články se stejnémi tagy - řazeno podle počtu sdílených tagů a data vytvoření
    '''

    # Načtení tagů z článku
    article_tags_ids = article.tags.values_list('id', flat=True)

    # Načtení článků obsahující některý z tagů
    similar_articles = Article.objects.filter(tags__in=article_tags_ids).exclude(id=article.id)

    # Seřazení článků podle počtu shodných tagů
    similar_articles = similar_articles.annotate(same_tags_in_article=Count('tags')) \
                           .order_by('-same_tags_in_article', '-created')[:3]

    # Navrácení výsledu
    return similar_articles

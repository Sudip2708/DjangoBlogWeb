### Definice podpůrných utils

from django.db.models import Count

from articles.models.article import Article


def get_category_count():
    '''
    Získání počtu článků v každé kategorii.

    :return: Počet článků v každé kategorii - řazeno podle počtu sestupně
    '''

    # Získání počtu článků pro každou kategorii
    queryset = Article.objects.values('categories__title', 'categories__slug')\
        .annotate(Count('categories__title'))\
        .order_by('-categories__title__count')

    # Navrácení výsledu
    return queryset

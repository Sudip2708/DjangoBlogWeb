### Definice podpůrných utils

from django.db.models import Count

from articles.models.article import Article
from articles.models.article_author import ArticleAuthor


def get_category_count():
    # Získání počtu článků v každé kategorii, seřazeno podle počtu sestupně
    queryset = Article.objects.values('categories__title', 'categories__slug').annotate(Count('categories__title')).order_by('-categories__title__count')
    return queryset

def get_author(user):
    # Získání autora na základě uživatelského jména
    queryset = ArticleAuthor.objects.filter(user=user)
    if queryset.exists():
        return queryset[0]
    return None

def get_most_commented_articles():
    # Získání tří nejvíce komentovaných článků
    queryset = Article.objects.order_by('-comment_count')[:3]
    return queryset

def get_similar_articles(article):
    # Získání podobných článků na základě sdílených tagů, seřazeno podle počtu sdílených tagů a data vytvoření
    article_tags_ids = article.tags.values_list('id', flat=True)
    similar_articles = Article.objects.filter(tags__in=article_tags_ids).exclude(id=article.id)
    similar_articles = similar_articles.annotate(same_tags_in_article=Count('tags')) \
                           .order_by('-same_tags_in_article', '-created')[:3]
    return similar_articles

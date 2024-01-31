### Registrace modelů pro zobrazení v administrátorském rozhraní Django

from django.contrib import admin
from .models.article import Article
from .models.article_author import ArticleAuthor
from .models.article_category import ArticleCategory
from .models.article_comment import ArticleComment
from .models.article_view import ArticleView


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # Zobrazení vybraných polí v seznamu článků v administrátorském rozhraní
    list_display = ['title', 'author', 'updated', 'created', 'id', 'comment_count', 'public', 'featured']

    # Možnost filtrování seznamu článků podle různých kritérií
    list_filter = ['created', 'created', 'categories']

    # Možnost vyhledávání článků podle různých polí
    search_fields = ['title', 'overview', 'content']

    # Hierarchie dat v seznamu podle data vytvoření
    date_hierarchy = 'created'

    # Výchozí řazení seznamu článků podle data poslední aktualizace sestupně
    ordering = ['-updated']


# Pro další modely se používá podobný přístup

@admin.register(ArticleView)
class ArticleViewAdmin(admin.ModelAdmin):
    list_display = ['created', 'article', 'user']
    list_filter = ['user', 'article']
    search_fields = ['user', 'article']
    date_hierarchy = 'created'
    ordering = ['article']


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['article', 'content', 'user', 'created']
    list_filter = ['user', 'article']
    search_fields = ['user', 'article']
    ordering = ['-created']


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_filter = ['title']
    search_fields = ['title']
    ordering = ['title']


@admin.register(ArticleAuthor)
class ArticleAuthorAdmin(admin.ModelAdmin):
    list_filter = ['author']
    search_fields = ['author']
    ordering = ['author']




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
    list_display = ['title', 'author', 'id', 'updated', 'created', 'status', 'featured', 'comment_count', 'category', 'tag_list']

    # Možnost filtrování seznamu článků podle různých kritérií
    list_filter = ['created', 'created', 'category']

    # Možnost vyhledávání článků podle různých polí
    search_fields = ['title', 'overview', 'content']

    # Hierarchie dat v seznamu podle data vytvoření
    date_hierarchy = 'created'

    # Výchozí řazení seznamu článků podle data poslední aktualizace sestupně
    ordering = ['-updated']

    # Metody na zobrazení tagů v admin sekci
    def get_queryset(self, request):
        '''
        Tato metoda je volána při načítání dat do seznamu v administrátorském rozhraní.
        V tomto případě se vrací dotaz na databázi, který zahrnuje i přednačítání (prefetching) souvisejících tagů pro každý objekt v seznamu.
        Tím se snižuje počet dotazů na databázi, protože všechny související tagy jsou předem načteny.
        '''
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):

        '''
        Tato metoda slouží k zobrazení tagů v seznamu objektů.
        Používá se v administrátorském rozhraní pro získání reprezentace tagů, které jsou pak zobrazeny v jednom sloupci.
        Metoda vrací řetězec, ve kterém jsou tagy spojeny čárkou a mezerou.
        Jde o čistě vizuální zobrazování informací o tagu.
        :param obj:
        :return:
        '''
        return u", ".join(o.name for o in obj.tags.all())


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




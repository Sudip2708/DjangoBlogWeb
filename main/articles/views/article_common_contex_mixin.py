print("### main/articles/views/article_common_contex_mixin.py")

### Definice třídy pro společný obsah

from django.db.models import Count
from taggit.models import Tag
from django.views.generic.base import ContextMixin
from django.contrib.auth.models import AnonymousUser
from django.urls import resolve


from articles.models.article import Article
from articles.models.article_author import ArticleAuthor
from articles.schema_search.get_all_published_category import get_all_published_category
from utilities.for_articles.get_category_count import get_category_count
from homepage.models.footer_section import FooterSettings


class CommonContextMixin(ContextMixin):
    print("### class CommonContextMixin(ContextMixin):")
    def get_context_data(self, **kwargs):
        print("### def get_context_data(self, **kwargs):")
        context = super().get_context_data(**kwargs)

        # Získání kategorie a počtu
        category_count = get_category_count()
        context['category_count'] = category_count

        # Získání nejčastěji zobrazovaných článků
        most_viewed = (
            Article.objects
            .annotate(views_count=Count('articleview'))
            .order_by('-views_count')[:3]
        )
        context['most_viewed'] = most_viewed

        # Získání všech tagů
        tags = Tag.objects.all()
        context['tags'] = tags

        # Předání slugů z URL
        context['tag_slug'] = self.kwargs.get('tag_slug')
        context['category_slug'] = self.kwargs.get('category_slug')

        # Nastavení dalších proměnných do contextu
        context['page_request_var'] = "page"

        # Získání autora - je-li
        author = None
        if self.request.user.is_authenticated:
            try:
                user = self.request.user
                author = ArticleAuthor.objects.get(id=user.linked_author_id)
            except:
                author = None
        # Přidání autora do kontextu
        context['author'] = author

        # Pořadí postranních panelů
        # Seřazení panelů podle jejich pořadí uživatele
        user = self.request.user

        if user.is_anonymous:
            sorted_panels = [
                {'name': 'search', 'order': user.sidebar_search_order},
                {'name': 'category', 'order': user.sidebar_category_order},
                {'name': 'tags', 'order': user.sidebar_tags_order},
            ]

        else:
            sorted_panels = [
                {'name': 'search', 'order': user.sidebar_search_order},
                {'name': 'user', 'order': user.sidebar_user_order},
                {'name': 'category', 'order': user.sidebar_category_order},
                {'name': 'tags', 'order': user.sidebar_tags_order},
            ]

        # Seřazení podle pořadí
        sorted_panels.sort(key=lambda x: x['order'])
        # Přidání seřazených panelů do kontextu
        context['sorted_panels'] = sorted_panels


        # Poslání všech autoru do sidebaru pro vyhledávání
        all_authors = ArticleAuthor.objects.all()
        context['all_authors'] = all_authors

        # Vytažení všech publikovaných kategorií
        published_category = get_all_published_category()
        context['published_category'] = published_category

        footer_data = FooterSettings.singleton().get_footer_settings
        context['footer_data'] = footer_data

        return context

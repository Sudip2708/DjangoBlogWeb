### Definice třídy pro společný obsah

from django.db.models import Count
from taggit.models import Tag
from django.views.generic.base import ContextMixin

from articles.models.article import Article
from articles.models.article_author import ArticleAuthor

from utilities.for_articles.get_category_count import get_category_count


class CommonContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
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
        if not self.request.user.is_anonymous:
            try:
                user = self.request.user
                author = ArticleAuthor.objects.get(id=user.linked_author_id)
            except:
                author = None

        context['author'] = author

        return context
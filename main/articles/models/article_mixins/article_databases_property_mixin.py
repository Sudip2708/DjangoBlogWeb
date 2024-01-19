
from articles.models.article_view import ArticleView


class ArticleDatabasesPropertyMixin:
    @property
    def get_comments(self):
        """
        Vrátí všechny komentáře k článku, seřazené sestupně podle data vytvoření.
        """
        return self.comments.all().order_by('-created')


    @property
    def view_count(self):
        """
        Vrátí počet zobrazení článku.
        """
        return ArticleView.objects.filter(article=self).count()


    @property
    def get_tags(self):
        """
        Vrátí všechny tagy přiřazené k článku.
        """
        return self.tags.all()


    @property
    def comment_count(self):
        """
        Vrátí počet komentářů k článku.
        """
        return self.comments.count()
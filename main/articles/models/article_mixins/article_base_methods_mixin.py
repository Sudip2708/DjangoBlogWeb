from django.urls import reverse


class ArticleBaseMethodsMixin:

    def __str__(self):
        """
        Vrátí textovou reprezentaci instance (pro administrační rozhraní a výpisy)
        """
        return self.title

    def get_absolute_url(self):
        """
        Vrátí absolutní URL pro zobrazení detailu článku.
        """
        return reverse('article-detail', kwargs={'slug': self.slug})


    def get_update_url(self):
        """
        Vrátí URL pro aktualizaci článku.
        """
        return reverse('article-update', kwargs={'slug': self.slug})


    def get_delete_url(self):
        """
        Vrátí URL pro smazání článku.
        """
        return reverse('article-delete', kwargs={'slug': self.slug})
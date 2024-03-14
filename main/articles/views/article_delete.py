print("### main/articles/views/article_delete.py")

### Definice třídy pohledu pro smazání článku

from django.views.generic import DeleteView

from articles.models.article import Article


class ArticleDeleteView(DeleteView):
    # Použitý model pro smazání článku
    model = Article

    # URL, na kterou bude uživatel přesměrován po úspěšném smazání článku
    success_url = '/blog'

    # Cesta k šabloně pro potvrzení smazání článku
    template_name = 'article_confirm_delete_.html'



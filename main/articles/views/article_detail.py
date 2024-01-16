### Definice třídy pohledu pro jeden článek

from django.shortcuts import redirect, reverse
from django.views.generic import DetailView

from articles.models.article import Article
from articles.models.article_view import ArticleView
from articles.forms.comment_form import CommentForm
from articles.views.utils.get_similar_articles import get_similar_articles
from articles.views.utils.article_common_contex import CommonContextMixin


class ArticleDetailView(CommonContextMixin, DetailView):
    # Použitý model pro zobrazení detailu článku
    model = Article

    # Cesta k šabloně pro zobrazení detailu článku
    template_name = '40_article.html'

    # Název objektu v kontextu
    context_object_name = 'article'

    # Inicializace prázdného formuláře pro komentáře
    form = CommentForm()

    def get_object(self):
        # Získání instance článku, zároveň zaznamenání zobrazení, pokud je uživatel přihlášený
        obj = super().get_object()
        if self.request.user.is_authenticated:
            ArticleView.objects.get_or_create(
                user=self.request.user,
                article=obj
            )
        return obj

    def post(self, request, *args, **kwargs):
        # Zpracování odeslaného formuláře pro komentář
        form = CommentForm(request.POST)
        if form.is_valid():
            article = self.get_object()
            form.instance.user = request.user
            form.instance.article = article
            form.save()
            # Přesměrování na detail článku po úspěšném odeslání komentáře
            return redirect(reverse("article-detail", kwargs={'slug': article.slug}))

    def get_context_data(self, **kwargs):
        # Získání běžného kontextu a přidání podobných článků
        context = super().get_context_data(**kwargs)
        context['similar_articles'] = get_similar_articles(self.object)
        return context

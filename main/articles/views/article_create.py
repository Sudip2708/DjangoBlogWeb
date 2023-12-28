### Definice třídy pohledu pro vytvoření článku

from django.shortcuts import redirect, reverse
from django.views.generic import CreateView

from .utils import get_author
from articles.forms.article_form import ArticleForm
from articles.views.article_common_contex import CommonContextMixin
from articles.models.article import Article
from articles.views.utils import get_author


class ArticleCreateView(CommonContextMixin, CreateView):
    # Použitý model pro vytvoření nového článku
    model = Article

    # Cesta k šabloně pro vytvoření článku
    template_name = '50_article_create.html'

    # Použitý formulář pro vytvoření článku
    form_class = ArticleForm

    def get_context_data(self, **kwargs):
        # Získání běžného kontextu a přidání vlastního názvu pro stránku
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context

    def form_valid(self, form):
        # Při úspěšném odeslání formuláře, nastavíme autora na aktuálního uživatele
        form.instance.author = get_author(self.request.user)

        # Uložení formuláře a přesměrování na detail nově vytvořeného článku
        form.save()
        return redirect(reverse("article-detail", kwargs={'slug': form.instance.slug}))


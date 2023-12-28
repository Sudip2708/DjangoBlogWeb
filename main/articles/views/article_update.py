### Definice třídy pohledu pro úpravu článku

from django.shortcuts import redirect, reverse
from django.views.generic import UpdateView

from articles.forms.article_form import ArticleForm
from articles.models.article import Article
from articles.views.article_common_contex import CommonContextMixin
from articles.views.utils import get_author


class ArticleUpdateView(CommonContextMixin, UpdateView):
    # Použitý model pro aktualizaci článku
    model = Article

    # Cesta k šabloně pro aktualizaci článku
    template_name = '50_article_create.html'

    # Použitý formulář pro aktualizaci článku
    form_class = ArticleForm

    def get_context_data(self, **kwargs):
        # Získání běžného kontextu a přidání vlastního názvu pro stránku
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context

    def form_valid(self, form):
        # Při úspěšném odeslání formuláře, nastavíme autora na aktuálního uživatele
        form.instance.author = get_author(self.request.user)

        # Uložení formuláře a přesměrování na detail aktualizovaného článku
        form.save()
        return redirect(reverse("article-detail", kwargs={'slug': form.instance.slug}))



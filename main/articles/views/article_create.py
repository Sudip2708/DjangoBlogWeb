### Definice třídy pohledu pro vytvoření článku

from django.shortcuts import redirect, reverse
from django.views.generic import CreateView

from articles.forms.article_form import ArticleForm
from utilities.for_articles.views_common_contex_mixin import CommonContextMixin
from articles.models.article import Article
from utilities.for_articles.get_author import get_author


class ArticleCreateView(CreateView, CommonContextMixin):
    '''
    Definice pohledu pro stránku pro vytvoření článku.

    :param CreateView: Třída pro definici pohledu pro vytvoření článku
    :param CommonContextMixin: Společný obsah pro stránky pro vytvoření a úpravu článku.
    :return: Stránka pro správu uživatelského účtu.
    '''

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


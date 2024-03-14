print("### main/articles/views/article_create.py")

### Definice třídy pohledu pro vytvoření článku

from django.shortcuts import redirect, reverse
from django.views.generic import CreateView
import pdb

from articles.forms.article_form import ArticleForm
from .article_common_contex_mixin import CommonContextMixin
from articles.models.article import Article
from utilities.for_articles.get_author import get_author
from utilities.for_articles.clean_tagify_input import clean_tagify_input
from utilities.for_articles.check_and_delete_unused_tags import check_and_delete_unused_tags


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
    template_name = '5_create_article/50__base__.html'

    # Použitý formulář pro vytvoření článku
    form_class = ArticleForm

    def get_context_data(self, **kwargs):
        # Získání běžného kontextu a přidání vlastního názvu pro stránku
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create an Article'
        return context

    def form_valid(self, form):
        # Při úspěšném odeslání formuláře, nastavíme autora na aktuálního uživatele
        form.instance.author = get_author(self.request.user)

        # Úprava tagů
        if form.cleaned_data['tags']:
            form.cleaned_data['tags'] = clean_tagify_input(form.cleaned_data['tags'])

        # Uložení formuláře a přesměrování na detail nově vytvořeného článku
        form.save()

        # Kontrola, zda bylo zmáčknuté tlačítko pro odeslání dat s návratem na stránku pro úpravy
        submit_change_value = self.request.POST.get('submit_change')
        if submit_change_value:
            return redirect(reverse("article-update",
                                    kwargs={'slug': form.instance.slug, 'current_tab': submit_change_value }))
        else:
            return redirect(reverse("article-detail",
                                    kwargs={'slug': form.instance.slug}))


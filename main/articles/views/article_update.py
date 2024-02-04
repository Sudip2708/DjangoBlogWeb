### Definice třídy pohledu pro úpravu článku


from taggit.models import Tag



from django.shortcuts import redirect, reverse
from django.views.generic import UpdateView
from django.http import HttpResponse


from articles.forms.article_form import ArticleForm
from articles.models.article import Article
from .article_common_contex_mixin import CommonContextMixin
from utilities.for_articles.get_author import get_author
from utilities.for_articles.clean_main_picture_max_size import clean_main_picture_max_size
from utilities.for_articles.clean_tagify_input import clean_tagify_input
from utilities.for_articles.check_and_delete_unused_tags import check_and_delete_unused_tags


class ArticleUpdateView(UpdateView, CommonContextMixin):
    '''
    Definice pohledu pro stránku pro úpravu článku.

    :param UpdateView: Třída pro definici pohledu pro úpravu článku
    :param CommonContextMixin: Společný obsah pro stránky pro vytvoření a úpravu článku.
    :return: Stránka pro správu uživatelského účtu.
    '''

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

        # Validace a změna formátu obrázku
        if form.instance.main_picture_max_size_tracker.has_changed('main_picture_max_size'):
            form = clean_main_picture_max_size(form)

        # Úprava tagů
        form.cleaned_data['tags'] = clean_tagify_input(form.cleaned_data['tags'])
        check_and_delete_unused_tags(form.instance, form.cleaned_data['tags'])

        # Uložení formuláře a přesměrování na detail aktualizovaného článku
        form.save()

        # Kontrola, zda bylo zmáčknuté tlačítko pro odeslání dat s návratem na stránku pro úpravy
        submit_change_value = self.request.POST.get('submit_change')
        if submit_change_value:
            return redirect(reverse("article-update", kwargs={'slug': form.instance.slug}))

        return redirect(reverse("article-detail", kwargs={'slug': form.instance.slug}))



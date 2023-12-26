### Definuje pohledy (views), které obsluhují HTTP požadavky


from django.shortcuts import redirect, reverse
from django.views.generic import UpdateView
from articles.forms.article_form import ArticleForm
from articles.models.article import Article
from marketing.forms import EmailSignupForm


form = EmailSignupForm()


class ArticleUpdateView(UpdateView):
    '''
    Tento kód definuje pohled (ArticleUpdateView) v rámci frameworku Django, který zdědil od třídy UpdateView.
    Pohled slouží k aktualizaci existujícího článku.
    Tento kód umožňuje uživatelům aktualizovat existující články pomocí formuláře a být přesměrován na stránku s detaily aktualizovaného článku.
    Klíčové body kódu:
    form_class = ArticleForm: Určuje třídu formuláře (ArticleForm), která bude použita pro aktualizaci existujícího článku.
    get_context_data: Přetěžená metoda pro získání dalších informací do kontextu šablony. Zde je do kontextu přidán titul 'Update'.
    form_valid: Přetěžená metoda pro zpracování platného formuláře. Zde je přiřazován autor článku na základě přihlášeného uživatele (pomocí funkce get_author). Následně je aktualizovaný článek uložen do databáze a uživatel je přesměrován na stránku s detaily aktualizovaného článku.
    '''
    model = Article
    template_name = 'article_create.html'
    form_class = ArticleForm

    def get_context_data(self, **kwargs):
        # Přetěžená metoda pro získání dalších informací do kontextu šablony
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'  # Přidání titulu do kontextu
        return context

    def form_valid(self, form):
        # Přetěžená metoda pro zpracování platného formuláře
        form.instance.author = get_author(self.request.user)  # Přiřazení autora článku
        form.save()  # Uložení aktualizovaného článku do databáze
        return redirect(reverse("article-detail", kwargs={'slug': form.instance.slug}))  # Přesměrování na detaily aktualizovaného článku


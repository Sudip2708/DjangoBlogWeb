### Definuje pohledy (views), které obsluhují HTTP požadavky


from django.shortcuts import redirect, reverse
from django.views.generic import CreateView
from articles.forms.article_form import ArticleForm
from articles.models.article import Article
from marketing.forms import EmailSignupForm


form = EmailSignupForm()


class ArticleCreateView(CreateView):
    '''
    Tento kód definuje pohled (ArticleCreateView) v rámci frameworku Django, který zdědil od třídy CreateView.
    Pohled slouží k vytváření nového článku.
    Tento kód umožňuje uživatelům vytvářet nové články pomocí formuláře a následně být přesměrován na stránku s detaily nově vytvořeného článku.
    Klíčové body kódu:
    form_class = ArticleForm: Určuje třídu formuláře (ArticleForm), která bude použita pro vytvoření nového článku.
    get_context_data: Přetěžená metoda pro získání dalších informací do kontextu šablony. Zde je do kontextu přidán titul 'Create'.
    form_valid: Přetěžená metoda pro zpracování platného formuláře. Zde je přiřazován autor článku na základě přihlášeného uživatele (pomocí funkce get_author). Následně je článek uložen do databáze a uživatel je přesměrován na stránku s detaily vytvořeného článku.
    '''
    model = Article
    template_name = '50_article_create.html'
    form_class = ArticleForm

    def get_context_data(self, **kwargs):
        # Přetěžená metoda pro získání dalších informací do kontextu šablony
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'  # Přidání titulu do kontextu
        return context

    def form_valid(self, form):
        # Přetěžená metoda pro zpracování platného formuláře
        form.instance.author = get_author(self.request.user)  # Přiřazení autora článku
        form.save()  # Uložení článku do databáze
        return redirect(reverse("article-detail", kwargs={'slug': form.instance.slug}))  # Přesměrování na detaily nového článku

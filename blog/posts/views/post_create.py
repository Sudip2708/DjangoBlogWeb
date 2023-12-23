### Definuje pohledy (views), které obsluhují HTTP požadavky


from django.shortcuts import redirect, reverse
from django.views.generic import CreateView
from posts.forms.post_form import PostForm
from posts.models.post import Post
from marketing.forms import EmailSignupForm


form = EmailSignupForm()


class PostCreateView(CreateView):
    '''
    Tento kód definuje pohled (PostCreateView) v rámci frameworku Django, který zdědil od třídy CreateView.
    Pohled slouží k vytváření nového článku.
    Tento kód umožňuje uživatelům vytvářet nové články pomocí formuláře a následně být přesměrován na stránku s detaily nově vytvořeného článku.
    Klíčové body kódu:
    form_class = PostForm: Určuje třídu formuláře (PostForm), která bude použita pro vytvoření nového článku.
    get_context_data: Přetěžená metoda pro získání dalších informací do kontextu šablony. Zde je do kontextu přidán titul 'Create'.
    form_valid: Přetěžená metoda pro zpracování platného formuláře. Zde je přiřazován autor článku na základě přihlášeného uživatele (pomocí funkce get_author). Následně je článek uložen do databáze a uživatel je přesměrován na stránku s detaily vytvořeného článku.
    '''
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        # Přetěžená metoda pro získání dalších informací do kontextu šablony
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'  # Přidání titulu do kontextu
        return context

    def form_valid(self, form):
        # Přetěžená metoda pro zpracování platného formuláře
        form.instance.author = get_author(self.request.user)  # Přiřazení autora článku
        form.save()  # Uložení článku do databáze
        return redirect(reverse("post-detail", kwargs={'pk': form.instance.pk}))  # Přesměrování na detaily nového článku

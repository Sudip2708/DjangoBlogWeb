### Definuje pohledy (views), které obsluhují HTTP požadavky


from django.shortcuts import redirect, reverse
from django.views.generic import UpdateView
from posts.forms.comment_form import CommentForm
from posts.forms.post_form import PostForm
from posts.models.post import Post
from posts.models.author import Author
from posts.models.post_view import PostView
from marketing.forms import EmailSignupForm


form = EmailSignupForm()


class PostUpdateView(UpdateView):
    '''
    Tento kód definuje pohled (PostUpdateView) v rámci frameworku Django, který zdědil od třídy UpdateView.
    Pohled slouží k aktualizaci existujícího článku.
    Tento kód umožňuje uživatelům aktualizovat existující články pomocí formuláře a být přesměrován na stránku s detaily aktualizovaného článku.
    Klíčové body kódu:
    form_class = PostForm: Určuje třídu formuláře (PostForm), která bude použita pro aktualizaci existujícího článku.
    get_context_data: Přetěžená metoda pro získání dalších informací do kontextu šablony. Zde je do kontextu přidán titul 'Update'.
    form_valid: Přetěžená metoda pro zpracování platného formuláře. Zde je přiřazován autor článku na základě přihlášeného uživatele (pomocí funkce get_author). Následně je aktualizovaný článek uložen do databáze a uživatel je přesměrován na stránku s detaily aktualizovaného článku.
    '''
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        # Přetěžená metoda pro získání dalších informací do kontextu šablony
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'  # Přidání titulu do kontextu
        return context

    def form_valid(self, form):
        # Přetěžená metoda pro zpracování platného formuláře
        form.instance.author = get_author(self.request.user)  # Přiřazení autora článku
        form.save()  # Uložení aktualizovaného článku do databáze
        return redirect(reverse("post-detail", kwargs={'pk': form.instance.pk}))  # Přesměrování na detaily aktualizovaného článku


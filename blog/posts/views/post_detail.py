### Definuje pohledy (views), které obsluhují HTTP požadavky


from django.shortcuts import redirect
from django.shortcuts import reverse
from django.views.generic import DetailView
from posts.forms.comment_form import CommentForm
from posts.models.post import Post
from posts.models.post_view import PostView
from marketing.forms import EmailSignupForm
from .utils import get_category_count


form = EmailSignupForm()


class PostDetailView(DetailView):
    '''
    Tento kód definuje pohled (PostDetailView) v rámci frameworku Django, který zdědil od třídy DetailView.
    Pohled slouží k zobrazení detailů konkrétního článku.
    Tento kód umožňuje uživatelům prohlížet detaily konkrétního článku, zobrazuje tři nejnovější články a poskytuje formulář pro odeslání komentářů.
    Klíčové body kódu:
    get_object: Přetěžená metoda ze třídy DetailView, která získává instanci článku pro zobrazení. Navíc, pokud je uživatel přihlášený, vytváří záznam v modelu PostView pro sledování zobrazení článku.
    get_context_data: Přetěžená metoda pro získání dalších informací, které budou přidány do kontextu šablony. Zde jsou získávány tři nejnovější články a počet článků v každé kategorii.
    post: Metoda pro zpracování HTTP POST požadavku, který může obsahovat odeslaný formulář pro komentář. Pokud je formulář platný, přiřazují se mu uživatel a článek a formulář se ukládá. Následně je uživatel přesměrován na stránku s detaily článku.
    '''
    model = Post
    template_name = '30_article.html'
    context_object_name = 'post'
    form = CommentForm()

    def get_object(self):
        # Získání instance článku pomocí metody get_object() ze třídy DetailView
        obj = super().get_object()

        # Zaznamenání zobrazení článku, pokud je uživatel přihlášen
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(
                user=self.request.user,
                post=obj
            )

        return obj

    def get_context_data(self, **kwargs):
        # Získání dalších informací pro kontext šablony
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]

        # Příprava kontextu pro šablonu
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        context['category_count'] = category_count
        context['form'] = self.form

        return context

    def post(self, request, *args, **kwargs):
        # Zpracování HTTP POST požadavku pro odeslání komentáře
        form = CommentForm(request.POST)

        if form.is_valid():
            # Získání instance článku
            post = self.get_object()

            # Přiřazení uživatele a článku k instanci formuláře a uložení komentáře
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            # Přesměrování na detaily článku
            return redirect(reverse("post-detail", kwargs={'pk': post.pk}))

### Definuje pohledy (views), které obsluhují HTTP požadavky


from django.views.generic import DeleteView
from posts.models.post import Post
from posts.models.author import Author
from posts.models.post_view import PostView
from marketing.forms import EmailSignupForm


form = EmailSignupForm()


class PostDeleteView(DeleteView):
    '''
    Tento kód definuje pohled (PostDeleteView) v rámci frameworku Django, který zdědil od třídy DeleteView.
    Pohled slouží k odstranění existujícího článku.
    Tento kód umožňuje uživatelům odstranit existující články a po úspěšném smazání budou přesměrováni na specifikovanou URL.

    Klíčové body kódu:
    model = Post: Určuje model (Post), podle kterého bude probíhat mazání.
    success_url = '/blog': Udává URL, na kterou bude uživatel přesměrován po úspěšném smazání článku.
    template_name = 'post_confirm_delete.html': Specifikuje název šablony, která bude použita pro potvrzení smazání. V této šabloně by měl být uživateli prezentován potvrzovací formulář pro smazání.
    '''
    model = Post
    success_url = '/blog'  # URL pro přesměrování po úspěšném smazání článku
    template_name = 'post_confirm_delete.html'  # Název šablony pro potvrzení smazání


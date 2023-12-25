### Definuje pohledy (views), které obsluhují HTTP požadavky


from django.views.generic import DeleteView
from articles.models.article import Article
from marketing.forms import EmailSignupForm


form = EmailSignupForm()


class ArticleDeleteView(DeleteView):
    '''
    Tento kód definuje pohled (ArticleDeleteView) v rámci frameworku Django, který zdědil od třídy DeleteView.
    Pohled slouží k odstranění existujícího článku.
    Tento kód umožňuje uživatelům odstranit existující články a po úspěšném smazání budou přesměrováni na specifikovanou URL.

    Klíčové body kódu:
    model = Article: Určuje model (Article), podle kterého bude probíhat mazání.
    success_url = '/blog': Udává URL, na kterou bude uživatel přesměrován po úspěšném smazání článku.
    template_name = 'article_confirm_delete.html': Specifikuje název šablony, která bude použita pro potvrzení smazání. V této šabloně by měl být uživateli prezentován potvrzovací formulář pro smazání.
    '''
    model = Article
    success_url = '/blog'  # URL pro přesměrování po úspěšném smazání článku
    template_name = 'article_confirm_delete.html'  # Název šablony pro potvrzení smazání


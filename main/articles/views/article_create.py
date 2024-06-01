from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from common_data.base_view import BaseView

from ..models.article import Article
from .article_create_data.get_form_class import get_form_class
from .article_create_data.get_or_create_author import get_or_create_author
from .article_create_data.get_success_url import get_success_url
from .article_create_data.get_context_data import get_context_data


@method_decorator(login_required, name='dispatch')
class ArticleCreateView(BaseView, CreateView):
    '''
    Pohled pro vytvoření článku (jen pro přihlášené uživatele).

    Pohled zpracovává následující URL:
    - article-create: Stránka pro vytvoření nového článku.

    Pohled dědí ze základní třídy CreateView a vlastní třídy BaseView.

    Atributy přetížené z CreateView:
    - self.model: Určuje model, se kterým tento pohled pracuje.
    - self.template_name: Určuje cestu k šabloně, která bude použita pro zobrazení výsledků.

    Atributy poděděné z BaseView:
    - self.user: Instance uživatele (buď CustomUser, nebo AnonymousUserWithSettings).
    - self.url_name: URL adresa, ze které požadavek přišel.

    Metody definované v tomto pohledu:
    - get_form_class: Metoda, která vrací formulář na základě zvolené záložky stránky.
    - form_valid: Metoda, která do formuláře přidává instanci autora.
    - get_success_url: Metoda, která vrací adresu pro přesměrování po úspěšném založení článku.
    - get_context_data: Metoda, která vrací obsah pro vykreslení šablony.
    '''

    model = Article
    template_name = '5_create_article/50__base__.html'

    def get_form_class(self):
        '''
        Metoda pro navrácení příslušného formuláře (dle záložky stránky).

        Metoda volá stejnojmennou metodu uloženou v samostatném souboru
        a vrací její výsledek.
        '''
        return get_form_class(self)

    def form_valid(self, form):
        '''
        Metoda pro validaci formuláře (+ přidává autora).

        Metoda volá funkci pro získání nebo vytvoření a získání instance autora.
        Následně metoda volá validační metodu nadřazené třídy.
        '''
        form.instance.author = get_or_create_author(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        '''
        Metoda pro vytvoření návratové adresy (po úspěšném uložení formuláře).

        Metoda volá stejnojmennou metodu uloženou v samostatném souboru
        a vrací její výsledek.
        '''
        return get_success_url(self)

    def get_context_data(self, **kwargs):
        '''
        Metoda pro předání kontextu potřebného pro vykreslení stránky.

        Metoda nejprve načte kontext nadřazené třídy,
        a poté volá stejnojmennou metodu uloženou v samostatném souboru,
        které kontext předá a následně vrací její výsledek.
        '''
        context = super().get_context_data(**kwargs)
        return get_context_data(self, context, **kwargs)

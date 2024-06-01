from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from common_data.base_view import BaseView

from ..models.article import Article


@method_decorator(login_required, name='dispatch')
class ArticleDeleteView(BaseView, DeleteView):
    '''
    Pohled pro smazání článku (jen pro přihlášené uživatele).

    Pohled zpracovává následující URL:
    - article-delete: Stránka pro potvrzení smazání článku.

    Pohled dědí ze základní třídy DeleteView a vlastní třídy BaseView.

    Atributy přetížené z DeleteView:
    - self.model: Určuje model, se kterým tento pohled pracuje.
    - self.template_name: Určuje cestu k šabloně, která bude použita pro zobrazení výsledků.
    - self.success_url: Definuje návratovou cestu po úspěšném provedení úkonu.

    Atributy poděděné z BaseView:
    - self.user: Instance uživatele (buď CustomUser, nebo AnonymousUserWithSettings).
    - self.url_name: URL jméno adresy, ze které požadavek přišel.

    Metody definované v tomto pohledu:
    - get_context_data: Metoda, která vytváří obsah pro vykreslení šablony.
    '''

    model = Article
    template_name = '5_create_article/55__confirm_delete__.html'
    success_url = reverse_lazy('my-articles', kwargs={'current_tab': 'all'})

    def get_context_data(self, **kwargs):
        '''
        Metoda pro předání kontextu potřebného pro vykreslení stránky.

        Kontext poděděný z BaseView:
        - context['user']: Instance uživatele.
        - context['url_name']: URL jménu adresy z které požadavek přišel.
        - context['sidebar_search_form']: Formulář pro hledání (pro postranní panel).
        - context['published_categories']: Publikované kategorie (pro dropdown menu a postranní panel).
        - context['footer']: Data pro vykreslení patičky (na domácí stránce je již zahrnuto)
        - context['user_thumbnail']: Miniatura profilového obrázku (pro přihlášeného a nepřihlášeného uživatele).

        Kontext vytvořený tímto pohledem:
        - context['article']: Instance článku.
        '''
        context = super().get_context_data(**kwargs)
        context['article'] = self.get_object()
        return context

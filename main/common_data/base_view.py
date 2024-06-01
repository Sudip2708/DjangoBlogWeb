from django.views.generic import View
from django.urls import resolve

from articles.forms.search_form import ArticleSearchForm
from articles.models.article_category import ArticleCategory
from homepage.models.footer_section import FooterSettings


class BaseView(View):
    '''
    Definice základní třídy pohledu z které dědí všechny ostatní třídy pohledu.

    Tato třída nejprve v metodě dispatch po obdržení requestu vytvoří atributy:
    - self.user: Instance uživatele.
    - self.url_name: URL jménu adresy z které požadavek přišel

    Dále pak v metodě get_context_data přidává kontext:
    - context['user']: Instance uživatele.
    - context['url_name']: URL jménu adresy z které požadavek přišel.
    - context['sidebar_search_form']: Formulář pro hledání (pro postranní panel).
    - context['published_categories']: Publikované kategorie (pro dropdown menu a postranní panel).
    - context['footer']: Data pro vykreslení patičky (na domácí stránce je již zahrnuto)
    - context['user_thumbnail']: Miniatura profilového obrázku (pro přihlášeného a nepřihlášeného uživatele).
    '''

    def dispatch(self, request, *args, **kwargs):
        '''
        Metoda definuje základní atributy společné všem ostatním třídám, které z této třídy budou dědit.

        Atributy definopvané touto metodou:
        - self.user: Instance uživatele (buď CustomUser, nebo AnonymousUserWithSettings).
        - self.url_name: URL jménu adresy z které požadavek přišel
        - self.default_profile_picture: URL cesta k defaultnímu obrázku pro nepřihlášeného uživatele.

        Metoda následně volá dispatch() nadřazené třídy.
        '''

        self.user = request.user
        self.url_name = resolve(self.request.path_info).url_name
        self.default_profile_picture = request.build_absolute_uri('/media/images/profile_pictures/default.jpg')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        '''
        Metoda definuje základní kontext společný všem ostatním třídám, které z této třídy budou dědit.

        Kontext definovaný touto metodou:
        - context['user']: Instance uživatele.
        - context['url_name']: URL jménu adresy z které požadavek přišel.
        - context['sidebar_search_form']: Formulář pro hledání (pro postranní panel).
        - context['published_categories']: Publikované kategorie (pro dropdown menu a postranní panel).
        - context['footer']: Data pro vykreslení patičky (na domácí stránce je již zahrnuto)
        - context['user_thumbnail']: Miniatura profilového obrázku (pro přihlášeného a nepřihlášeného uživatele).

        Metoda nejprve načte kontext z nadřazené třídy
        a následně ho vrací, společně s přidáním vlastních hodnot.
        '''

        context = super().get_context_data(**kwargs)

        context['user'] = self.user
        context['url_name'] = self.url_name
        context['sidebar_search_form'] = ArticleSearchForm()
        context['published_categories'] = ArticleCategory.objects.exclude(id=1)
        context['footer'] = FooterSettings.singleton().get_data()
        if self.user.is_authenticated:
            context['user_thumbnail'] = self.user.profile_picture_thumbnail.url
        else:
            context['user_thumbnail'] = self.default_profile_picture

        return context
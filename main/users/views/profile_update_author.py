from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect

from articles.models.article_author import ArticleAuthor
from common_data.base_view import BaseView
from ..forms.author_profile_form import AuthorProfileForm


class AuthorProfileView(BaseView, FormView):
    '''
    Pohled pro úpravu a nastavení dat autora.

    Pohled zpracovává následující URL:
    - profile-update-author: Stránka pro úpravu autorského účtu.

    Pohled dědí ze základní třídy FormView a vlastní třídy BaseView.

    Atributy přetížené z CreateView:
    - self.model: Určuje model, se kterým tento pohled pracuje.
    - self.template_name: Určuje cestu k šabloně, která bude použita pro zobrazení výsledků.
    - self.form_class: Určuje formulář napojený na tento pohled.
    - self.success_url: Určuje návratovou adresu po úspěšném uložení dat (stejná stránka).

    Atributy poděděné z BaseView:
    - self.user: Instance uživatele (buď CustomUser, nebo AnonymousUserWithSettings).
    - self.url_name: URL adresa, ze které požadavek přišel.

    Metody definované v tomto pohledu:
    - get_form_kwargs: Metoda pro získání argumentů pro vytvoření instance formuláře (zde pro přidání instance autora).
    - form_valid: Metoda, která se volá po úspěšném ověření formuláře (zde pro zobrazení oznamu o úspěšném uložení dat).
    - get_context_data: Metoda, která vrací obsah pro vykreslení šablony.
    '''

    model = ArticleAuthor
    template_name = '2_main/23__profile_update__.html'
    form_class = AuthorProfileForm
    success_url = reverse_lazy('profile-update-author')

    def get_form_kwargs(self):
        '''
        Metoda pro získání argumentů pro vytvoření instance formuláře.

        Metoda nejprve načte argumenty z nadřazené třídy,
        následně vytvoří a přidá argument pro instanci přihlášeného uživatele
        a data předává dál do formuláře.
        '''
        kwargs = super().get_form_kwargs()
        self.author = self.request.user.linked_author
        kwargs['instance'] = self.author
        return kwargs

    def form_valid(self, form):
        '''
        Metoda, která se volá po úspěšném ověření formuláře.

        Metoda nejprve uloží data formuláře,
        po té vytvoří oznam o úspěšné aktualizaci dat
        a přesměruje na stránku pro editaci dat autora.
        '''
        form.save()
        messages.success(self.request, 'Your profile has been updated successfully.')
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        '''
        Metoda pro získání dat pro kontext šablony.

        Metoda nejprve získá kontext z nadřazené třídy
        a po té vytváří a přidává vlastní kontext pro vykreslení šablony.
        Metoda vrací kontext pro vykreslení šablony.

        Kontext poděděný z BaseView:
        - context['user']: Instance uživatele.
        - context['url_name']: URL jménu adresy z které požadavek přišel.
        - context['sidebar_search_form']: Formulář pro hledání (pro postranní panel).
        - context['published_categories']: Publikované kategorie (pro dropdown menu a postranní panel).
        - context['footer']: Data pro vykreslení patičky (na domácí stránce je již zahrnuto)
        - context['user_thumbnail']: Miniatura profilového obrázku (pro přihlášeného a nepřihlášeného uživatele).

        Kontext přidaný v tomto kódu:
        - context['page_title']: Nadpis stránky.
        - context['profile_form']: Formulář stránky.
        - context['profile_picture_url']: URL adresa profilového obrázku.
        - context['profile_picture_alt']: Zástupný text pro profilový obrázek.
        - context['submit_button_text']: Popisek odesílacího tlačítka.
        - context['tab_names']: Popisek pro záložky stránky.
        - context['tab_url']: URL pro záložky stránky.
        '''
        context = super().get_context_data(**kwargs)

        context['page_title'] = 'Edit Author Profile'
        context['profile_form'] = AuthorProfileForm(instance=self.author)
        context['profile_picture_url'] = self.author.profile_picture.url
        context['profile_picture_alt'] = "Author Profile Picture"
        context['submit_button_name'] = "submit_author"
        context['submit_button_text'] = "Save Author Data"
        context['tab_names'] = {'user': "User", 'author': "Author"}
        context['tab_url'] = {'user': 'profile-update-user', 'author': 'profile-update-author'}

        return context

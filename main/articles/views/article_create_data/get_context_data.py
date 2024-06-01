from django.urls import reverse

from taggit.models import Tag


def get_context_data(self, context, **kwargs):
    '''
    Metoda pro vytvoření kontextu.

    Kontext poděděný z BaseView:
    - context['user']: Instance uživatele.
    - context['url_name']: URL jménu adresy z které požadavek přišel.
    - context['sidebar_search_form']: Formulář pro hledání (pro postranní panel).
    - context['published_categories']: Publikované kategorie (pro dropdown menu a postranní panel).
    - context['footer']: Data pro vykreslení patičky (na domácí stránce je již zahrnuto)
    - context['user_thumbnail']: Miniatura profilového obrázku (pro přihlášeného a nepřihlášeného uživatele).

    Kontext vytvořený tímto pohledem:
    - context['tab_urls']: Reverzní cesty na jednotlivé záložky.
    - context['current_tab']: Aktuální záložka stránky.
    - context['title']: Název stránky.
    - context['tags_name_str']: Řetězec tagů pro automatické doplňování tagů
        (používáno ve skriptu pro Tagify a vytváří se pouze pro sekci nastavení).
    '''

    # Vytvoření URL adres pro jednotlivé záložky stránky
    tab_urls = {
        'for_overview': reverse('article-create', kwargs={'current_tab': 'overview'}),
        'for_content': reverse('article-create', kwargs={'current_tab': 'content'}),
        'for_settings': reverse('article-create', kwargs={'current_tab': 'settings'}),
    }

    # Vytvoření seznamu existujících tagů a převedení na řetězec.
    all_tags =  list(Tag.objects.values_list('name', flat=True))
    tags_name_str = ','.join(all_tags)

    # Vytvoření proměné pro aktuální záložku
    current_tab = self.kwargs.get('current_tab')

    context['tab_urls'] = tab_urls
    context['current_tab'] = current_tab
    context['title'] = 'Create Your Article'
    if current_tab == 'settings':
        context['tags_name_str'] = tags_name_str

    return context

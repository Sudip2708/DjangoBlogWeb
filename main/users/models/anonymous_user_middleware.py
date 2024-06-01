from django.utils.deprecation import MiddlewareMixin

from .anonymous_user_data.anonymous_user_with_settings import AnonymousUserWithSettings

class AnonymousUserMiddleware(MiddlewareMixin):
    '''
    Middleware přidávající nepřihlášenému uživateli nastavení pro boční panel.

    Middleware nejprve ověří, zda se jedná o nepřihlášeného uživatele
    a pokud ano, vytvoří pro něj instanci s nastavením bočního panelu.
    '''

    def __init__(self, get_response):
        '''
        Konstruktor třídy, který je volán při vytvoření instance.

        Konstruktor přijímá parametr get_response,
        který slouží k odchycení a zpracování HTTP požadavku,
        v rámci řetězce middleware.

        Konstruktor vytváří pro tento požadavek atribut,
        aby byl dostupný pro další zpracování požadavků
        a odpovědí v rámci middleware.
        '''
        self.get_response = get_response

    def __call__(self, request):
        '''
        Metoda, která umožňuje objektu být volán jako funkce.

        Tato metoda slouží jako hlavní bod vstupu pro zpracování HTTP požadavku.

        Nejprve metoda zkontroluje, zda je uživatel přihlášen.
        Pokud není, vytvoří instanci třídy AnonymousUserWithSettings,
        která reprezentuje anonymního uživatele s dodatečným nastavením.
        Tato instance je pak uložena do atributu request.user.

        Pokud je uživatel přihlášen, atribut request.user zůstane nezměněn.

        Následně je volána funkce self.get_response(request),
        která předá aktuální požadavek dalšímu middleware v řetězci
        a vrátí odpověď.
        '''

        if not request.user.is_authenticated:
            request.user = AnonymousUserWithSettings(request)
        else:
            request.user = request.user

        response = self.get_response(request)
        return response

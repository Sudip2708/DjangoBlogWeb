from django.utils.deprecation import MiddlewareMixin


# Definice výchozích hodnot pro nastavení vzhledu bočního panelu pro nepřihlášeného uživatele
default_values = {
    "sidebar": True,
    "sidebar_search": {"value": True, "order": 1},
    "sidebar_search_options": False,
    "sidebar_category": {"value": True, "order": 2},
    "sidebar_category_options": True,
    "sidebar_category_navigation": True,
    "sidebar_tags": {"value": True, "order": 3},
    "sidebar_tags_options": True,
    "show_tab_for_similar": True,
}


class AnonymousUserWithSettings:
    '''Třída rozšiřující základní třídu Django pro anonymního uživatele.

    Tato třída poskytuje přístup k nastavení uživatele uloženému v session.
    '''


    def __init__(self, request):
        '''Inicializace instance třídy.

        :param request: HttpRequest objekt reprezentující aktuální požadavek.
        '''
        self.request = request
        self.session_settings = request.session.get('user_settings', default_values)

        # Dynamické vytvoření vlastností na základě defaultních hodnot
        for key, value in default_values.items():
            if isinstance(value, dict):
                setattr(self.__class__, key, property(lambda self, k=key: self.session_settings[k]["value"]))
                setattr(self.__class__, f"{key}_order", property(lambda self, k=key: self.session_settings[k]["order"]))
            else:
                setattr(self.__class__, key, property(lambda self, k=key: self.session_settings[k]))


    def __getattr__(self, name):
        '''Metoda pro přístup k atributům instance.

        Pokud je požadovaný atribut obsažen v session_settings, vrátí jeho hodnotu.

        :param name: Název požadovaného atributu.
        :return: Hodnota požadovaného atributu, pokud existuje, jinak vyvolá AttributeError.
        '''

        if name in self.session_settings:
            return self.session_settings[name]
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")


    def change_sidebar_value(self, field_key):
        """Metoda pro změnu hodnoty v nastavení bočního panelu pro nepřihlášeného uživatele."""

        # Získání session dat pro nepřihlášeného uživatele
        user_settings = self.request.session.get('user_settings', default_values)

        # Ověření, zda je hodnota přítomna jako klíč v session datech
        if field_key in user_settings:

            # Ověří, zda se jedná o bool hodnotu, pokud ano, změní ji
            if isinstance(user_settings[field_key], bool):
                user_settings[field_key] = not user_settings[field_key]

            # Ověří, zda se jedná o slovník, pokud ano, změní v něm hodnotu
            elif isinstance(user_settings[field_key], dict):
                user_settings[field_key]["value"] = not user_settings[field_key]["value"]

        # Uložení změn zpět do session
        self.request.session['user_settings'] = user_settings

    def print_current_user_settings(self, request):
        '''Metoda pro tisk aktuálního nastavení uživatele do konzole.'''

        # Pokud uživatel není přihlášený
        if not request.user.is_authenticated:

            # Získání unikátního identifikátoru uživatele
            user_id = request.session.session_key

            # Získání nastavení uživatele ze session dat nebo výchozích hodnot
            user_settings = request.session.get('user_settings', default_values)

            # Výpis aktuálního nastavení uživatele do konzole
            print(f"Current settings for user {user_id}:")
            for key, value in user_settings.items():
                print(f"{key}: {value}")
        else:
            # Pokud je uživatel přihlášený, není třeba tisknout nastavení anonymního uživatele
            print("User is authenticated. No need to print settings for anonymous user.")


    def find_sidebar_by_order(self, order):
        '''Metoda pro nalezení bočního panelu podle jeho pořadí v nastavení.'''

        # Projde všechny položky session nastavení
        for key, value in self.session_settings.items():

            # Ověří, zda je hodnota slovníkem a zda má správné pořadí
            if isinstance(value, dict) and value.get("order") == order:

                # Vrátí celý slovník reprezentující boční panel
                return value

        # Pokud boční panel s daným pořadím není nalezen, vrátí None
        return None


    def sidebar_move(self, hash):
        '''Metoda pro posunutí bočního panelu v nastavení.'''

        # Získání pohybu a názvu bočního panelu z hash
        movement = hash[0:7]
        sidebar = "sidebar" + hash[7:]

        # Pokud je boční panel v nastavení přítomen
        if sidebar in self.session_settings:

            # Získání informací o aktuálním bočním panelu
            actual_sidebar = self.session_settings[sidebar]
            actual_position = actual_sidebar["order"]

            # Pokud se jedná o pohyb nahoru
            if movement == '#MoveUp':

                # Získání pozice předchozího bočního panelu
                previous_position = actual_position - 1

                # Nalezení předchozího bočního panelu
                previous_sidebar = self.find_sidebar_by_order(previous_position)

                # Pokud je předchozí boční panel nalezen
                if previous_sidebar:

                    # Prohodí pořadí mezi aktuálním a předchozím bočním panelem
                    actual_sidebar["order"], previous_sidebar["order"] = previous_sidebar["order"], actual_sidebar[
                        "order"]

            # Pokud se jedná o pohyb dolů
            elif movement == '#MoveDn':

                # Získání pozice následujícího bočního panelu
                next_position = actual_position + 1

                # Nalezení následujícího bočního panelu
                next_sidebar = self.find_sidebar_by_order(next_position)

                # Pokud je následující boční panel nalezen
                if next_sidebar:

                    # Prohodí pořadí mezi aktuálním a následujícím bočním panelem
                    actual_sidebar["order"], next_sidebar["order"] = next_sidebar["order"], actual_sidebar["order"]

            # Aktualizace session dat po provedení posunu
            self.request.session['user_settings'] = self.session_settings

    @property
    def is_authenticated(self):
        '''Metoda pro určení, zda je uživatel přihlášen.'''
        return False


    @property
    def is_anonymous(self):
        '''Metoda pro určení, zda je uživatel anonymní.'''
        return True


    @property
    def is_staff(self):
        '''Metoda pro určení, zda je uživatel staff.'''
        return False


    @property
    def is_superuser(self):
        '''Metoda pro určení, zda je uživatel superuser.'''
        return False


    @property
    def is_active(self):
        '''Metoda pro určení, zda je uživatel aktive.'''
        return False



class AnonymousUserSettingsMiddleware(MiddlewareMixin):
    '''Middleware pro nastavení bočního panelu pro nepřihlášeného uživatele.'''


    def __init__(self, get_response):
        '''Inicializace instance middleware.

        :param get_response: Funkce pro získání odpovědi.
        '''
        self.get_response = get_response


    def __call__(self, request):
        '''Metoda pro zpracování požadavku.

        Pokud je uživatel nepřihlášený, nastaví request.user na instanci AnonymousUserWithSettings.

        :param request: HttpRequest objekt reprezentující aktuální požadavek.
        :return: HttpResponse objekt.
        '''
        if not request.user.is_authenticated:
            request.user = AnonymousUserWithSettings(request)
        else:
            request.user = request.user
        response = self.get_response(request)
        return response



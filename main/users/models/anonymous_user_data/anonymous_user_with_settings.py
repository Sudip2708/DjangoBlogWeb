from .mixin_property import AnonynousPropertyMixin
from ..common_data.change_bool_value import change_bool_value
from ..common_data.change_sidebar_order import change_sidebar_order
from ..common_data.get_sorted_sidebar_panels import get_sorted_sidebar_panels
from ..common_data.default_setting_values import (sidebar_setting_values,
                                                  sidebar_order_values,
                                                  additional_setting_values)


class AnonymousUserWithSettings(AnonynousPropertyMixin):
    '''
    Třída pro vytvoření instance pro anonymního uživatele s nastavením pro postranní panely.

    Tato třída je určena pro nastavení postranního panelu pro nepřihlášeného uživatele.
    Třída dědí z mixinu AnonynousPropertyMixin nastavení základních vlastností
    pro nepřihlášeného uživatele.

    Třída vytváří následující atributy:
    - username: Uživatelské jméno nepřihlášeného uživatele.
    - slug: Slug nepřihlášeného uživatele.

    Třída nejprve volá konstruktor a na základě requestu vytvoří instanci pro nepřihlášeného uživatele
    a vytvoří atributy pro slovníky hodnot pro vzhled a umístění bočních panelů,
    a dalších nastavení přístupných ze stránek pro uživatele.

    Třída obsahuje metody pro změnu hodnot těchto slovníků,
    které pro svůj výpočet používají funkce,
    které jsou společné i pro přihlášeného uživatele.
    '''

    username = 'Unregistered User'
    slug = 'anonymus'


    def __init__(self, request):
        '''
        Konstruktor třídy pro vytvoření instance.

        Konstruktor přijímá parametr request, objekt reprezentující aktuální HTTP požadavek.

        Konstruktor následně vytváří atributy:
        - self.request: Atribut pro objekt reprezentující aktuální HTTP požadavek
        - self.sidebar: Atribut pro slovník obsahující boolean hodnoty pro nastavení postranních panelů.
        - self.sidebar_order: Atribut pro slovník obsahující hodnoty pořadí postranních panelů.
        - self.settings: Atribut pro slovník obsahující boolean hodnoty pro další nastavení uživatele.

        Konstruktor ukládá hodnoty těchto dvou slovníků do aktuální session,
        pro nepřihlášeného uživatele.

        '''
        self.request = request
        self.sidebar = request.session.get('sidebar', sidebar_setting_values)
        self.sidebar_order = request.session.get('sidebar_order', sidebar_order_values)
        self.settings = request.session.get('settings', additional_setting_values)


    def change_sidebar_bool_value(self, field_key):
        '''
        Metoda pro změnu boolean hodnot pro nastavení bočního panelu.

        Metoda obdrží klíč pole, jehož hodnota má být změněna,
        po té volá metodu pro změnu boolean pole pro příslušný slovník a klíč,
        která změnu provede a navrací změněný slovník.
        Metoda navráceným slovníkem přepisuje slovník uložený v atributu třídy,
        a slovník uložený v session nepřihlášeného uživatele.

        '''
        self.sidebar = change_bool_value(self.sidebar, field_key)
        self.request.session['sidebar'] = self.sidebar

    def change_sidebar_order_value(self, hash):
        '''
        Metoda pro změnu pořadí bočních panelů.

        Metoda hash s informacemi o vybraném panelu a směru posunu,
        a po té volá metodu pro změnu pozice panelu pro příslušný slovník a hash,
        která změnu provede a navrací změněný slovník.
        Metoda navráceným slovníkem přepisuje slovník uložený v atributu třídy,
        a slovník uložený v session nepřihlášeného uživatele.

        '''
        self.sidebar_order = change_sidebar_order(self.sidebar_order, hash)
        self.request.session['sidebar_order'] = self.sidebar_order

    def change_settings_bool_value(self, field_key):
        '''
        Metoda pro změnu boolean hodnot pro dodatečná nastavení uživatele.

        Metoda obdrží klíč pole, jehož hodnota má být změněna,
        po té volá metodu pro změnu boolean pole pro příslušný slovník a klíč,
        která změnu provede a navrací změněný slovník.
        Metoda navráceným slovníkem přepisuje slovník uložený v atributu třídy,
        a slovník uložený v session nepřihlášeného uživatele.

        '''
        self.settings = change_bool_value(self.settings, field_key)
        self.request.session['settings'] = self.settings

    def get_sorted_sidebar_panels(self):
        ''' Metoda vrací data pro vykreslení postranních panelů v nastaveném pořadí. '''
        return get_sorted_sidebar_panels(self)


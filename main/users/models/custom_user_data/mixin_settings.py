from django.db import models
from django.db.models import JSONField

from .setting_values_check import setting_values_check
from ..common_data.change_bool_value import change_bool_value
from ..common_data.change_sidebar_order import change_sidebar_order
from ..common_data.get_sorted_sidebar_panels import get_sorted_sidebar_panels
from ..common_data.default_setting_values import (sidebar_setting_values,
                                                  sidebar_order_values,
                                                  additional_setting_values)


class UserSettingsMixin(models.Model):
    '''
    Mixin pro třídu CustomUser přidávající třídě nastavení postranního panelu.

    Mixin je abstraktní třídou a přidává třídě CustomUser tři nové JSON pole:
    - sidebar: Pole pro slovník s daty pro nastavení vzhledu bočního panelu.
    - sidebar_order: Pole pro slovník s daty pro nastavení pořadí bočních panelů.
    - settings: Pole pro slovník s daty pro další dodatečná nastavení.

    Mixin nejprve volá konstruktor pro vytvoření instance,
    ten pomocí funkce values_check zkontroluje jednotlivá pole,
    a dopíše případné nastavení dle defaultních hodnot.

    Třída dále obsahuje metody pro změnu hodnot těchto slovníků,
    které pro svůj výpočet používají funkce,
    které jsou společné i pro nepřihlášeného uživatele.
    '''

    sidebar = JSONField(default=dict)
    sidebar_order = JSONField(default=dict)
    settings = JSONField(default=dict)

    class Meta:
        abstract = True

    def change_sidebar_bool_value(self, field_key):
        '''
        Metoda pro změnu boolean hodnot pro nastavení bočního panelu.

        Metoda obdrží klíč pole, jehož hodnota má být změněna,
        poté volá metodu pro změnu boolean pole pro příslušný slovník a klíč,
        která změnu provede a navrací změněný slovník.
        Metoda navráceným slovníkem přepisuje slovník uložený v atributu třídy,
        a uloží změny.
        '''
        self.sidebar = change_bool_value(self.sidebar, field_key)
        self.save()

    def change_sidebar_order_value(self, hash):
        '''
        Metoda pro změnu pořadí bočních panelů.

        Metoda obdrží hash s informacemi o vybraném panelu a směru posunu,
        a poté volá metodu pro změnu pozice panelu pro příslušný slovník a hash,
        která změnu provede a navrací změněný slovník.
        Metoda navráceným slovníkem přepisuje slovník uložený v atributu třídy,
        a uloží změny.
        '''
        self.sidebar_order = change_sidebar_order(self.sidebar_order, hash)
        self.save()

    def change_settings_bool_value(self, field_key):
        '''
        Metoda pro změnu boolean hodnot pro dodatečná nastavení uživatele.

        Metoda obdrží klíč pole, jehož hodnota má být změněna,
        poté volá metodu pro změnu boolean pole pro příslušný slovník a klíč,
        která změnu provede a navrací změněný slovník.
        Metoda navráceným slovníkem přepisuje slovník uložený v atributu třídy,
        a uloží změny.
        '''
        self.settings = change_bool_value(self.settings, field_key)
        self.save()

    def get_sorted_sidebar_panels(self):
        ''' Metoda vrací data pro vykreslení postranních panelů v nastaveném pořadí. '''
        return get_sorted_sidebar_panels(self)

    def check_default_values(self):
        '''
        Metoda pro ověření, zda slovníky obsahují všechny hodnoty.

        Metoda postupně volá pro každé pole obsahující slovník s nastavením metodu,
        která porovná jeho klíče s klíči v defaultních hodnotách.
        Pokud některý není nalezen, pak jej doplní i s příslušnou defaultní hodnotou.

        Metoda je navázaná na zachycení signálu user_logged_in,
        takže se provádí při každém přihlášení uživatele.
        '''
        self.sidebar = setting_values_check(self.sidebar, sidebar_setting_values)
        self.sidebar_order = setting_values_check(self.sidebar_order, sidebar_order_values)
        self.settings = setting_values_check(self.settings, additional_setting_values)
        self.save()

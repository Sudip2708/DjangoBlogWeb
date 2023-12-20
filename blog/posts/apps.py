### Obsahuje konfiguraci pro aplikaci.


from django.apps import AppConfig
'''
[from]
django.apps: balíček, který poskytuje funkcionalitu pro práci s aplikacemi 
[import]
AppConfig: modul, který umožňuje definovat různá nastavení, která ovlivňují URL cesty, šablony, statické soubory, middleware a další
'''


class PostsConfig(AppConfig):
    '''
    Třída, sloužící k nastavení konfigurace pro Django aplikaci s názvem 'posts'

    Nápověda:
    default_auto_field = 'django.db.models.BigAutoField': nastavuje atribut default_auto_field na hodnotu 'django.db.models.BigAutoField'
    (Tímto způsobem je určeno, že pro automaticky generovaná primární klíčová pole (AutoField) bude použito BigAutoField. BigAutoField je vhodné pro PostgreSQL databáze a je navrženo pro práci s velkými množstvími dat.)
    name = 'posts': specifikuje název aplikace, pro kterou je tato konfigurační třída platná
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'

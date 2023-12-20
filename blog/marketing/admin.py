### Definuje konfiguraci pro administrátorské rozhraní Django.


from django.contrib import admin
from .models import Signup
'''
[from]
django.contrib: balíček, který obsahuje různé moduly a aplikace poskytující doplňkovou funkcionalitu pro Django projekty
.models: soubor v adresáři, který obsahuje definice modelů databázových tabulek 
[import]
admin: modul, který je zaměřen na administrátorské rozhraní Django, které umožňuje jednoduchou správu dat v aplikaci přes webové rozhraní
Signup: databázový model, pro tabulku pro email na odebírání novinek
'''


# Registrování tabulek v admin sekci:
admin.site.register(Signup)

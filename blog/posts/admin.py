### Definuje konfiguraci pro administrátorské rozhraní Django.


from django.contrib import admin
from .models import Author, Category, Post, Comment, PostView
'''
[from]
django.contrib: balíček, který obsahuje různé moduly a aplikace poskytující doplňkovou funkcionalitu pro Django projekty
.models: soubor v adresáři, který obsahuje definice modelů databázových tabulek 
[import]
admin: modul, který je zaměřen na administrátorské rozhraní Django, které umožňuje jednoduchou správu dat v aplikaci přes webové rozhraní
Author: databázový model, pro tabulku pro autory příspěvků
Category: databázový model, pro tabulku pro kategorie příspěvků
Post: databázový model, pro tabulku s příspěvky
Comment: databázový model, pro tabulku s komentáři příspěvků
PostView: databázový model, pro tabulku pro zobrazení jednoho příspěvku
'''


# Registrování tabulek v admin sekci
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)

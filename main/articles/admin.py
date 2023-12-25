### Definuje konfiguraci pro administrátorské rozhraní Django.


from django.contrib import admin
from .models.article import Article
from .models.article_author import ArticleAuthor
from .models.article_category import ArticleCategory
from .models.article_comment import ArticleComment
from .models.article_view import ArticleView
'''
[from]
django.contrib: balíček, který obsahuje různé moduly a aplikace poskytující doplňkovou funkcionalitu pro Django projekty
.models: soubor v adresáři, který obsahuje definice modelů databázových tabulek 
[import]
admin: modul, který je zaměřen na administrátorské rozhraní Django, které umožňuje jednoduchou správu dat v aplikaci přes webové rozhraní
Article: databázový model, pro tabulku s příspěvky
ArticleAuthor: databázový model, pro tabulku pro autory příspěvků
ArticleCategory: databázový model, pro tabulku pro kategorie příspěvků
ArticleComment: databázový model, pro tabulku s komentáři příspěvků
ArticleView: databázový model, pro tabulku pro zobrazení jednoho příspěvku
'''


# Registrování tabulek v admin sekci
admin.site.register(Article)
admin.site.register(ArticleAuthor)
admin.site.register(ArticleCategory)
admin.site.register(ArticleComment)
admin.site.register(ArticleView)

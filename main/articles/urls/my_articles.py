from django.urls import path

from ..views.my_articles import MyArticlesView


# Definování adres začínajících s prefixem 'my-articles/'
urlpatterns = [

    # Zobrazení článků přihlášeného uživatele (je-li i autora)
    path('<str:current_tab>/', MyArticlesView.as_view(), name='my-articles'),

]













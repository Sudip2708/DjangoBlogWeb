print("### main/main/urls.py")

from django.urls import path

from articles.views.my_articles import MyArticlesView

urlpatterns = [

    # Adresy začínající s 'my-articles/'
    # URL pro seznam článků od přihlášeného uživatele (autora)
    path('<str:current_tab>/', MyArticlesView.as_view(), name='my-articles'),


]













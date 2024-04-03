print("### main/main/urls.py")

### Definice URL patternů pro aplikaci

from django.urls import path, include
from allauth.account.views import LoginView, SignupView
from .views.profile_update_user import profile_update_user
from .views.profile_update_author import profile_update_author
from .views.user_sidebar_movements import user_sidebar_movements
from .views.user_sidebar_appearance import user_sidebar_appearance


urlpatterns = [

    # URL pro účet uživatele (registrace, přihlášení, atd.)
    path('', include('allauth.urls')),

    # URL pro přihlášení pomocí sociálních sítí
    path('social/', include('allauth.socialaccount.urls')),

    # URL pro stránku pro založení účtu
    path('login/', LoginView.as_view(), name='account_login'),

    # URL pro stránku pro řihlášení
    path('signup/', SignupView.as_view(), name='account_signup'),



    # URL pro nastavení uživatelského účtu
    path('update/user', profile_update_user, name='profile_update_user'),

    # URL pro nastavení účtu autora
    path('update/author', profile_update_author, name='profile_update_author'),



    # URL pro aktualizaci stavu otevřených postranních panelů (ajax)
    path('appearance/', user_sidebar_appearance, name='user_sidebar_appearance'),

    # URL pro aktualizaci otevřených postranních panelů
    path('movements/<str:hash>/', user_sidebar_movements, name='user_sidebar_movements'),

]


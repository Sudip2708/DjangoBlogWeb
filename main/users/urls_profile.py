print("### main/main/urls.py")

from django.urls import path

# Pohledy pro správu uživatelů
from users.views.profile_update_user import profile_update_user
from users.views.profile_update_author import profile_update_author


urlpatterns = [

    # Adresy začínající s 'profile/'
    # URL pro nastavení uživatelského účtu
    path('update/user', profile_update_user, name='profile_update_user'),
    # URL pro nastavení účtu autora
    path('update/author', profile_update_author, name='profile_update_author'),

]













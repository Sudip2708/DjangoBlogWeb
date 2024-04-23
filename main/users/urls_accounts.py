print("### main/main/urls.py")

from django.urls import path, include

# Pohledy pro správu uživatelů
from allauth.account.views import LoginView, SignupView


urlpatterns = [

    # Adresy začínající s 'accounts/'

    # URL pro účet uživatele (registrace, přihlášení, atd.)
    path('', include('allauth.urls')),

    # URL pro přihlášení pomocí sociálních sítí
    path('social/', include('allauth.socialaccount.urls')),

    # URL pro stránku pro založení účtu
    path('login/', LoginView.as_view(), name='account_login'),

    # URL pro stránku pro řihlášení
    path('signup/', SignupView.as_view(), name='account_signup'),

]













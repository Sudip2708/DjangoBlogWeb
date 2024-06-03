from django.urls import path, include

from allauth.account.views import LoginView, SignupView


# Definování adres začínajících s prefixem 'accounts/'
urlpatterns = [

    # URL pro účet uživatele (registrace, přihlášení, atd.).
    path('', include('allauth.urls'), name='account-allauth'),

    # URL pro přihlášení pomocí sociálních sítí.
    path('social/', include('allauth.socialaccount.urls'), name='account-allauth-social'),

    # Stránkapro přihlášení.
    path('login/', LoginView.as_view(), name='account-login'),

    # Stránkapro registraci.
    path('signup/', SignupView.as_view(), name='account-signup'),

]

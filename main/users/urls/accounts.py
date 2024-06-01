from django.urls import path, include

from allauth.account.views import LoginView, SignupView


# Definování adres začínajících s prefixem 'accounts/'
urlpatterns = [

    # URL pro účet uživatele (registrace, přihlášení, atd.)
    path('', include('allauth.urls')),

    # URL pro přihlášení pomocí sociálních sítí
    path('social/', include('allauth.socialaccount.urls')),

    # URL pro stránku pro přihlášení
    path('login/', LoginView.as_view(), name='account-login'),

    # URL pro stránku pro registraci
    path('signup/', SignupView.as_view(), name='account-signup'),

]

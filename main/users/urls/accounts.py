from django.urls import path, include

from allauth.account.views import LoginView, SignupView


# Defining URLs starting with the prefix 'accounts/'
urlpatterns = [

    # URL for user account (registration, login, etc.).
    path('', include('allauth.urls'), name='account-allauth'),

    # URL for logging in using social networks.
    path('social/', include('allauth.socialaccount.urls'), name='account-allauth-social'),

    # Page for logging in.
    path('login/', LoginView.as_view(), name='account-login'),

    # Page for signing up.
    path('signup/', SignupView.as_view(), name='account-signup'),

]

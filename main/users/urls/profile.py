from django.urls import path

from ..views.profile_update_user import UserProfileView
from ..views.profile_update_author import AuthorProfileView


# Definování adres začínajících s prefixem 'profile/'
urlpatterns = [

    # Editace uživatelského účtu.
    path('update/user', UserProfileView.as_view(), name='profile-update-user'),

    # Editace účtu autora.
    path('update/author', AuthorProfileView.as_view(), name='profile-update-author'),

]

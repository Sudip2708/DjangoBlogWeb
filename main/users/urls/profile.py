from django.urls import path

from ..views.profile_update_user import UserProfileView
from ..views.profile_update_author import AuthorProfileView


# Defining URLs starting with the prefix 'profile/'
urlpatterns = [

    # Editing user account.
    path('update/user', UserProfileView.as_view(), name='profile-update-user'),

    # Editing author account.
    path('update/author', AuthorProfileView.as_view(), name='profile-update-author'),

]

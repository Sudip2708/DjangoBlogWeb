from django.urls import path

from ..views.user_sidebar_movements import user_sidebar_movements
from ..views.user_sidebar_appearance import user_sidebar_appearance
from ..views.user_navigation_settings import user_navigation_settings


# Defining URLs starting with the prefix 'settings/'
urlpatterns = [

    # URL for changing the visibility of inner sidebar menus (ajax).
    path('sidebar_appearance/', user_sidebar_appearance, name='user_sidebar_appearance'),

    # URL for changing the order of sidebar panels.
    path('sidebar_movements/<str:hash>/', user_sidebar_movements, name='user_sidebar_movements'),

    # URL for setting the visibility of navigation panels and the sidebar.
    path('navigation/<str:hash>/', user_navigation_settings, name='user_navigation_settings'),

]

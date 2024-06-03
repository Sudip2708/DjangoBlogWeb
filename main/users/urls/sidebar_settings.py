from django.urls import path

from ..views.user_sidebar_movements import user_sidebar_movements
from ..views.user_sidebar_appearance import user_sidebar_appearance
from ..views.user_navigation_settings import user_navigation_settings


# Definování adres začínajících s prefixem 'settings/'
urlpatterns = [

    # URL pro změnu viditelnosti vnitřních nabídek postranních panelů (ajax).
    path('sidebar_appearance/', user_sidebar_appearance, name='user_sidebar_appearance'),

    # URL pro změnu pořadí postranních panelů.
    path('sidebar_movements/<str:hash>/', user_sidebar_movements, name='user_sidebar_movements'),

    # URL pro nastavení viditelnosti navigačních panelů a postranního panelu.
    path('navigation/<str:hash>/', user_navigation_settings, name='user_navigation_settings'),

]

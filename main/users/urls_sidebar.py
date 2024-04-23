print("### main/main/urls.py")

from django.urls import path

# Pohledy pro správu uživatelů
from users.views.user_sidebar_movements import user_sidebar_movements
from users.views.user_sidebar_appearance import user_sidebar_appearance

urlpatterns = [

    # Adresy začínající s 'user_sidebar/'
    # URL pro aktualizaci stavu otevřených postranních panelů (ajax)
    path('appearance/', user_sidebar_appearance, name='user_sidebar_appearance'),
    # URL pro aktualizaci otevřených postranních panelů
    path('movements/<str:hash>/', user_sidebar_movements, name='user_sidebar_movements'),

]













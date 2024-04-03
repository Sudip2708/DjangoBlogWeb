print("### main/main/urls.py")

### Definice URL patternů pro aplikaci

from django.urls import path
from .views.home_page import HomePageView
from .views.edit_hero_section import EditHeroSection

urlpatterns = [

    # URL pro domovskou stránku
    path('', HomePageView.as_view(), name='home'),
    path('edit/', HomePageView.as_view(), name='home-page-edit'),
    path('edit/hero/', EditHeroSection.as_view(), name='edit-hero-section'),

]
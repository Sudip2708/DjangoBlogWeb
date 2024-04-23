print("### main/main/urls.py")

from django.urls import path

# Pohledy pro domácí stránku
from homepage.views.home_page_view import HomePageView

urlpatterns = [
    # Adresy začínající s ''
    # URL's pro domácí stránku
    path('', HomePageView.as_view(), name='home'),
]













from django.urls import path

from ..views.home_page_view import HomePageView


# Defining URLs starting with prefix '' (displaying the homepage)
urlpatterns = [

    # Display the homepage.
    path('', HomePageView.as_view(), name='homepage'),

]

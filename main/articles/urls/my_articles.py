from django.urls import path

from ..views.my_articles import MyArticlesView


# Defining URLs starting with the prefix 'my-articles/'
urlpatterns = [

    # Display articles of the logged-in user (if they are also authors).
    path('<str:current_tab>/', MyArticlesView.as_view(), name='my-articles'),

]

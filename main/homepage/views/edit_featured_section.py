from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages

from ..forms.featured_section_form import FeaturedArticlesForm
from ..models.featured_section import HomePageFeaturedArticles


class EditFeaturedArticlesSection(View):
    '''
    View for processing the form data for the Featured Articles section on the Home Page.

    This class proceeds as follows:
    Upon receiving a POST request to process form data, it creates an instance of the FeaturedArticlesForm form.
    It checks if the form is valid. If yes, it proceeds.
    It retrieves or creates an instance of the HomePageFeaturedArticles model.
    It sets the values from the form to the corresponding fields of the model instance.
    It saves the changes to the database by calling the save() method on the model instance.
    Finally, it redirects to the homepage-edit page.
    '''

    def post(self, request, *args, **kwargs):
        '''
        Processing the HTTP POST request.

        This method processes the submitted form for editing HomePageFeaturedArticles on the homepage.
        If the form is valid, it updates the values in the database
        and redirects the user to the homepage editing page.
        If the form is not valid, it displays an error message
        and redirects the user back to the editing page with unsaved changes.
        '''

        # Load the form
        form = FeaturedArticlesForm(request.POST)

        # Check if the form is valid
        if form.is_valid():

            # Retrieve or create an instance of the HomePageFeaturedArticles model
            featured_articles = HomePageFeaturedArticles.singleton()

            # Set the values from the form to the model instance
            featured_articles.featured_article_1 = form.cleaned_data['featured_article_1']
            featured_articles.featured_article_2 = form.cleaned_data['featured_article_2']
            featured_articles.featured_article_3 = form.cleaned_data['featured_article_3']
            featured_articles.display_featured_section = form.cleaned_data['display_featured_section']

            # Save the changes to the database and redirect to the homepage-edit page
            featured_articles.save()
            return redirect('homepage-edit')

        # If the form is not valid
        else:
            # Return to the editing page and display an error message
            messages.error(request, "The changes made were not saved.")
            return redirect('homepage-edit')

    def get(self, request, *args, **kwargs):
        '''
        Processing the HTTP GET request.

        This method checks if the GET request contains the parameter 'show_featured_section'.
        If yes, it sets the value for displaying the footer section to True and redirects
        to the homepage editing page. Otherwise, it continues with normal behavior.
        '''

        # Check if the get request contains a request to show the section
        if 'show_featured_section' in request.GET:

            # If yes - change the value and return to the HomePage editing page
            featured_articles = HomePageFeaturedArticles.singleton()
            featured_articles.display_featured_section = True
            featured_articles.save()
            return redirect('homepage-edit')

        # If not, continue normally
        else:
            return super().get(request, *args, **kwargs)

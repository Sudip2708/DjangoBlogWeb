from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages

from ..forms.latest_section_form import LatestArticlesForm
from ..models.latest_section import HomePageLatestArticles


class EditLatestArticlesSection(View):
    '''
    View for processing the form data for the latest articles section on the Home Page.

    This class proceeds as follows:
    Upon receiving a POST request to process form data, it creates an instance of the LatestArticlesForm form.
    It checks if the form is valid. If yes, it proceeds.
    It retrieves or creates an instance of the HomePageLatestArticles model.
    It sets the values from the form to the respective fields of the model instance.
    It saves the changes to the database by calling the save() method on the model instance.
    Finally, it redirects to the homepage-edit page.
    '''

    def post(self, request, *args, **kwargs):
        '''
        Processing the HTTP POST request.

        This method processes the submitted form for editing HomePageLatestArticles on the home page.
        If the form is valid, it updates the values in the database
        and redirects the user to the page for editing the home page.
        If the form is not valid, it displays an error message
        and redirects the user back to the editing page with unsaved changes.
        '''

        # Load the form
        form = LatestArticlesForm(request.POST)

        # Check if the form is valid
        if form.is_valid():

            # Retrieve or create an instance of the HomePageLatestArticles model
            latest_articles_section, _ = HomePageLatestArticles.objects.get_or_create(pk=1)

            # Set the values from the form to the model instance
            latest_articles_section.latest_title = form.cleaned_data['latest_title']
            latest_articles_section.latest_description = form.cleaned_data['latest_description']
            latest_articles_section.latest_article_1 = form.cleaned_data['latest_article_1']
            latest_articles_section.latest_article_2 = form.cleaned_data['latest_article_2']
            latest_articles_section.latest_article_3 = form.cleaned_data['latest_article_3']
            latest_articles_section.display_latest_section = form.cleaned_data['display_latest_section']

            # Save the changes to the database and redirect to the homepage-edit page
            latest_articles_section.save()
            return redirect('homepage-edit')

        # If the form is not valid
        else:
            # Return to the editing page and display an error message
            messages.error(request, "The changes made were not saved.")
            return redirect('homepage-edit')

    def get(self, request, *args, **kwargs):
        '''
        Processing the HTTP GET request.

        This method checks if the GET request contains the parameter 'show_latest_section'.
        If yes, it sets the value for displaying the latest section to True and redirects
        to the homepage editing page. Otherwise, it continues with normal behavior.
        '''

        # Check if the get request contains a request to show the section
        if 'show_latest_section' in request.GET:

            # If yes - change the value and return to the HomePage editing page
            latest_articles_section, _ = HomePageLatestArticles.objects.get_or_create(pk=1)
            latest_articles_section.display_latest_section = True
            latest_articles_section.save()
            return redirect('homepage-edit')

        # If not, continue normally
        else:
            return super().get(request, *args, **kwargs)

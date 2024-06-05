from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages

from ..forms.gallery_section_form import GallerySectionForm
from ..models.gallery_section import HomePageGallerySection


class EditGallerySection(View):
    '''
    View for processing the form data for the article gallery section on the Home Page.

    This class proceeds as follows:
    Upon receiving a POST request to process form data, it creates an instance of the GallerySectionForm form.
    It checks if the form is valid. If yes, it proceeds.
    It retrieves or creates an instance of the HomePageGallerySection model.
    It sets the values from the form to the respective fields of the model instance.
    It saves the changes to the database by calling the save() method on the model instance.
    Finally, it redirects to the homepage-edit page.
    '''

    def post(self, request, *args, **kwargs):
        '''
        Processing the HTTP POST request.

        This method processes the submitted form for editing HomePageGallerySection on the home page.
        If the form is valid, it updates the values in the database
        and redirects the user to the page for editing the home page.
        If the form is not valid, it displays an error message
        and redirects the user back to the editing page with unsaved changes.
        '''

        # Load the form
        form = GallerySectionForm(request.POST)

        # Check if the form is valid
        if form.is_valid():

            # Retrieve or create an instance of the HomePageGallerySection model
            gallery_instance = HomePageGallerySection.singleton()

            # Set the values from the form to the model instance
            gallery_instance.gallery_article_1 = form.cleaned_data['gallery_article_1']
            gallery_instance.gallery_article_2 = form.cleaned_data['gallery_article_2']
            gallery_instance.gallery_article_3 = form.cleaned_data['gallery_article_3']
            gallery_instance.gallery_article_4 = form.cleaned_data['gallery_article_4']
            gallery_instance.display_gallery_section = form.cleaned_data['display_gallery_section']

            # Save the changes to the database and redirect to the homepage-edit page
            gallery_instance.save()
            return redirect('homepage-edit')

        # If the form is not valid
        else:
            # Return to the editing page and display an error message
            messages.error(request, "The changes made were not saved.")
            return redirect('homepage-edit')

    def get(self, request, *args, **kwargs):
        '''
        Processing the HTTP GET request.

        This method checks if the GET request contains the parameter 'show_gallery_section'.
        If yes, it sets the value for displaying the gallery section to True and redirects
        to the homepage editing page. Otherwise, it continues with normal behavior.
        '''

        # Check if the get request contains a request to show the section
        if 'show_gallery_section' in request.GET:

            # If yes - change the value and return to the HomePage editing page
            gallery_section = HomePageGallerySection.singleton()
            gallery_section.display_gallery_section = True
            gallery_section.save()
            return redirect('homepage-edit')

        # If not, continue normally
        else:
            return super().get(request, *args, **kwargs)

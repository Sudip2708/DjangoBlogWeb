from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages

from ..forms.newsletter_section_form import NewsletterSectionForm
from ..models.newsletter_section import HomePageNewsletterSection


class EditNewsletterSection(View):
    '''
    View for processing the form data for the newsletter section on the Home Page.

    This class proceeds as follows:
    Upon receiving a POST request to process form data, it creates an instance of the NewsletterSectionForm form.
    It checks if the form is valid. If yes, it proceeds.
    It retrieves or creates an instance of the HomePageNewsletterSection model.
    It sets the values from the form to the respective fields of the model instance.
    It saves the changes to the database by calling the save() method on the model instance.
    Finally, it redirects to the homepage-edit page.
    '''

    def post(self, request, *args, **kwargs):
        '''
        Processing the HTTP POST request.

        This method processes the submitted form for editing HomePageNewsletterSection on the home page.
        If the form is valid, it updates the values in the database
        and redirects the user to the page for editing the home page.
        If the form is not valid, it displays an error message
        and redirects the user back to the editing page with unsaved changes.
        '''

        # Load the form
        form = NewsletterSectionForm(request.POST)

        # Check if the form is valid
        if form.is_valid():

            # Retrieve or create an instance of the HomePageNewsletterSection model
            newsletter_section, _ = HomePageNewsletterSection.objects.get_or_create(pk=1)

            # Set the values from the form to the model instance
            newsletter_section.newsletter_title = form.cleaned_data['newsletter_title']
            newsletter_section.newsletter_description = form.cleaned_data['newsletter_description']
            newsletter_section.newsletter_subscribers = form.cleaned_data['newsletter_subscribers']
            newsletter_section.display_newsletter_section = form.cleaned_data['display_newsletter_section']

            # Save the changes to the database and redirect to the homepage-edit page
            newsletter_section.save()
            return redirect('homepage-edit')

        # If the form is not valid
        else:
            # Return to the editing page and display an error message
            messages.error(request, "The changes made were not saved.")
            return redirect('homepage-edit')

    def get(self, request, *args, **kwargs):
        '''
        Processing the HTTP GET request.

        This method checks if the GET request contains the parameter 'show_newsletter_section'.
        If yes, it sets the value for displaying the newsletter section to True and redirects
        to the homepage editing page. Otherwise, it continues with normal behavior.
        '''

        # Check if the get request contains a request to show the section
        if 'show_newsletter_section' in request.GET:

            # If yes - change the value and return to the HomePage editing page
            newsletter_section, _ = HomePageNewsletterSection.objects.get_or_create(pk=1)
            newsletter_section.display_newsletter_section = True
            newsletter_section.save()
            return redirect('homepage-edit')

        # If not, continue normally
        else:
            return super().get(request, *args, **kwargs)

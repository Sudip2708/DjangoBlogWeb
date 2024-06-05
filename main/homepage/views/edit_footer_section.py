from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages

from ..forms.footer_section_form import FooterSettingsForm
from ..models.footer_section import FooterSettings
from ..models.data.save_footer_data import save_footer_data

class EditFooterSection(View):
    '''
    View for processing the form data for the footer section on the Home Page.

    This class proceeds as follows:
    Upon receiving a POST request to process form data, it creates an instance of the FooterSettingsForm form.
    It checks if the form is valid. If yes, it proceeds.
    It saves the form data by calling the save_footer_data() function.
    Finally, it redirects to the homepage-edit page.
    '''

    def post(self, request, *args, **kwargs):
        '''
        Processing the HTTP POST request.

        This method processes the submitted form for editing FooterSettingsForm.
        If the form is valid, it calls the method to save the data
        and redirects the user to the homepage editing page.
        If the form is not valid, it displays an error message
        and redirects the user back to the editing page with unsaved changes.
        '''

        # Load the form
        form = FooterSettingsForm(request.POST)

        # Check if the form is valid
        if form.is_valid():

            # Call the method to save data to the database and redirect to the homepage-edit page
            save_footer_data(form)
            return redirect('homepage-edit')

        # If the form is not valid
        else:
            # Return to the editing page and display an error message
            messages.error(request, "The changes made were not saved.")
            return redirect('homepage-edit')

    def get(self, request, *args, **kwargs):
        '''
        Processing the HTTP GET request.

        This method checks if the GET request contains the parameter 'show_footer_section'.
        If yes, it sets the value for displaying the footer section to True and redirects
        to the homepage editing page. Otherwise, it continues with normal behavior.
        '''

        # Check if the get request contains a request to show the section
        if 'show_footer_section' in request.GET:

            # If yes - change the value and return to the HomePage editing page
            footer_settings = FooterSettings.singleton()
            footer_settings.display_footer_section = True
            footer_settings.save()
            return redirect('homepage-edit')

        # If not, continue normally
        else:
            return super().get(request, *args, **kwargs)

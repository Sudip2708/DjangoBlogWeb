from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect

from common_data.base_view import BaseView
from ..forms.user_profile_form import UserProfileForm
from ..models.custom_user import CustomUser


class UserProfileView(BaseView, FormView):
    '''
    View for editing and setting user data.

    This view handles the following URL:
    - profile-update-user: Page for editing the user account.

    Inherits from the FormView and BaseView classes.

    Attributes overridden from CreateView:
    - self.model: Specifies the model this view works with.
    - self.template_name: Specifies the path to the template used for displaying the results.
    - self.form_class: Specifies the form connected to this view.
    - self.success_url: Specifies the return address after successful data saving (the same page).

    Inherited attributes from BaseView:
    - self.user: Instance of the user (either CustomUser or AnonymousUserWithSettings).
    - self.url_name: URL address from which the request came.

    Methods defined in this view:
    - get_form_kwargs: Method for obtaining arguments for creating a form instance (here for adding a user instance).
    - form_valid: Method called after successful form validation (here for displaying a message about successful data saving).
    - get_context_data: Method that returns content for rendering the template.
    '''

    model = CustomUser
    template_name = '2_main/23__profile_update__.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('profile-update-user')

    def get_form_kwargs(self):
        '''
        Method for obtaining arguments for creating a form instance.

        This method first loads arguments from the parent class,
        then creates and adds an argument for the instance of the logged-in user
        and passes the data to the form.
        '''
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def form_valid(self, form):
        '''
        Method called after successful form validation.

        This method first saves the form data,
        then creates a message about successful data update
        and redirects to the user data editing page.
        '''
        form.save()
        messages.success(self.request, 'Your profile has been updated successfully.')
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        '''
        Method for obtaining data for the template context.

        This method first gets the context from the parent class
        and then creates and adds custom context for rendering the template.
        The method returns the context for rendering the template.

        Context inherited from BaseView:
        - context['user']: User instance.
        - context['url_name']: URL name of the address from which the request came.
        - context['sidebar_search_form']: Search form (for the sidebar).
        - context['published_categories']: Published categories (for dropdown menu and sidebar).
        - context['footer']: Data for rendering the footer (already included on the homepage).
        - context['user_thumbnail']: Profile picture thumbnail (for logged-in and anonymous users).

        Context added in this code:
        - context['page_title']: Page title.
        - context['profile_form']: Page form.
        - context['profile_picture_url']: Profile picture URL.
        - context['profile_picture_alt']: Alternative text for the profile picture.
        - context['submit_button_text']: Submit button label.
        - context['tab_names']: Tab labels for the page.
        - context['tab_url']: URL for page tabs.
        '''
        context = super().get_context_data(**kwargs)

        context['page_title'] = 'Edit User Profile'
        context['profile_form'] = UserProfileForm(instance=self.user)
        context['profile_picture_url'] = self.user.profile_picture.url
        context['profile_picture_alt'] = "User Profile Picture"
        context['submit_button_text'] = "Save User Data"
        context['tab_names'] = {'user': "User", 'author': "Author"}
        context['tab_url'] = {'user': 'profile-update-user', 'author': 'profile-update-author'}

        return context

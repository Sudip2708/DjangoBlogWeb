from .mixin_property import AnonymousPropertyMixin
from ..common_data.change_bool_value import change_bool_value
from ..common_data.change_sidebar_order import change_sidebar_order
from ..common_data.get_sorted_sidebar_panels import get_sorted_sidebar_panels
from ..common_data.default_setting_values import (sidebar_setting_values,
                                                  sidebar_order_values,
                                                  additional_setting_values)


class AnonymousUserWithSettings(AnonymousPropertyMixin):
    '''
    Class for creating an instance for an anonymous user with sidebar settings.

    This class is intended for setting the sidebar for unregistered users.
    The class inherits from the AnonymousPropertyMixin mixin, which sets basic properties
    for unregistered users.

    The class creates the following attributes:
    - username: The username of the unregistered user.
    - slug: The slug of the unregistered user.

    The class first calls the constructor and based on the request, creates an instance for an unregistered user
    and creates attributes for dictionaries of values for appearance and placement of sidebar panels,
    and other settings accessible from user pages.

    The class contains methods for changing the values of these dictionaries,
    which use functions for their calculation that are common even for registered users.
    '''

    username = 'Unregistered User'
    slug = 'anonymous'


    def __init__(self, request):
        '''
        Constructor of the class for creating an instance.

        The constructor accepts the request parameter, an object representing the current HTTP request.

        The constructor then creates attributes:
        - self.request: Attribute for the object representing the current HTTP request.
        - self.sidebar: Attribute for the dictionary containing boolean values for setting sidebar panels.
        - self.sidebar_order: Attribute for the dictionary containing values for the order of sidebar panels.
        - self.settings: Attribute for the dictionary containing boolean values for additional user settings.

        The constructor saves the values of these two dictionaries to the current session,
        for an unregistered user.

        '''
        self.request = request
        self.sidebar = request.session.get('sidebar', sidebar_setting_values)
        self.sidebar_order = request.session.get('sidebar_order', sidebar_order_values)
        self.settings = request.session.get('settings', additional_setting_values)


    def change_sidebar_bool_value(self, field_key):
        '''
        Method for changing boolean values for sidebar settings.

        The method receives the key of the field whose value is to be changed,
        then calls the method to change the boolean field for the corresponding dictionary and key,
        which performs the change and returns the modified dictionary.
        The method overwrites the dictionary stored in the class attribute,
        and the dictionary stored in the session for an unregistered user.

        '''
        self.sidebar = change_bool_value(self.sidebar, field_key)
        self.request.session['sidebar'] = self.sidebar

    def change_sidebar_order_value(self, hash):
        '''
        Method for changing the order of sidebar panels.

        The method receives a hash with information about the selected panel and the direction of movement,
        and then calls the method to change the position of the panel for the corresponding dictionary and hash,
        which performs the change and returns the modified dictionary.
        The method overwrites the dictionary stored in the class attribute,
        and the dictionary stored in the session for an unregistered user.

        '''
        self.sidebar_order = change_sidebar_order(self.sidebar_order, hash)
        self.request.session['sidebar_order'] = self.sidebar_order

    def change_settings_bool_value(self, field_key):
        '''
        Method for changing boolean values for additional user settings.

        The method receives the key of the field whose value is to be changed,
        then calls the method to change the boolean field for the corresponding dictionary and key,
        which performs the change and returns the modified dictionary.
        The method overwrites the dictionary stored in the class attribute,
        and the dictionary stored in the session for an unregistered user.

        '''
        self.settings = change_bool_value(self.settings, field_key)
        self.request.session['settings'] = self.settings

    def get_sorted_sidebar_panels(self):
        ''' Method returns data for rendering sidebar panels in the configured order. '''
        return get_sorted_sidebar_panels(self)

from django.db import models
from django.db.models import JSONField

from .setting_values_check import setting_values_check
from ..common_data.change_bool_value import change_bool_value
from ..common_data.change_sidebar_order import change_sidebar_order
from ..common_data.get_sorted_sidebar_panels import get_sorted_sidebar_panels
from ..common_data.default_setting_values import (sidebar_setting_values,
                                                  sidebar_order_values,
                                                  additional_setting_values)


class UserSettingsMixin(models.Model):
    '''
    Mixin for the CustomUser class adding settings for the sidebar.

    The mixin is an abstract class and adds three new JSON fields to the CustomUser class:
    - sidebar: Field for a dictionary with data for setting the sidebar appearance.
    - sidebar_order: Field for a dictionary with data for setting the order of sidebar panels.
    - settings: Field for a dictionary with data for additional user settings.

    The mixin first calls the constructor to create an instance,
    which uses the values_check function to check each field,
    and fills in any missing settings based on default values.

    The class also contains methods for changing the values of these dictionaries,
    which use functions common to unregistered users for their computation.
    '''

    sidebar = JSONField(default=dict)
    sidebar_order = JSONField(default=dict)
    settings = JSONField(default=dict)

    class Meta:
        abstract = True

    def change_sidebar_bool_value(self, field_key):
        '''
        Method for changing boolean values for sidebar settings.

        The method receives a field key whose value needs to be changed,
        then calls the method to change the boolean field for the corresponding dictionary and key,
        which makes the change and returns the modified dictionary.
        The dictionary returned by the method overwrites the dictionary stored in the class attribute,
        and saves the changes.
        '''
        self.sidebar = change_bool_value(self.sidebar, field_key)
        self.save()

    def change_sidebar_order_value(self, hash):
        '''
        Method for changing the order of sidebar panels.

        The method receives a hash with information about the selected panel and the direction of movement,
        then calls the method to change the panel position for the corresponding dictionary and hash,
        which makes the change and returns the modified dictionary.
        The dictionary returned by the method overwrites the dictionary stored in the class attribute,
        and saves the changes.
        '''
        self.sidebar_order = change_sidebar_order(self.sidebar_order, hash)
        self.save()

    def change_settings_bool_value(self, field_key):
        '''
        Method for changing boolean values for additional user settings.

        The method receives a field key whose value needs to be changed,
        then calls the method to change the boolean field for the corresponding dictionary and key,
        which makes the change and returns the modified dictionary.
        The dictionary returned by the method overwrites the dictionary stored in the class attribute,
        and saves the changes.
        '''
        self.settings = change_bool_value(self.settings, field_key)
        self.save()

    def get_sorted_sidebar_panels(self):
        ''' Method returns data for rendering sidebar panels in the specified order. '''
        return get_sorted_sidebar_panels(self)

    def check_default_values(self):
        '''
        Method for verifying that dictionaries contain all values.

        The method iteratively calls the method for each field containing a dictionary with settings,
        which compares its keys with the keys in the default values.
        If any key is not found, it adds it along with the corresponding default value.

        The method is tied to the user_logged_in signal capture,
        so it is executed each time a user logs in.
        '''
        self.sidebar = setting_values_check(self.sidebar, sidebar_setting_values)
        self.sidebar_order = setting_values_check(self.sidebar_order, sidebar_order_values)
        self.settings = setting_values_check(self.settings, additional_setting_values)
        self.save()

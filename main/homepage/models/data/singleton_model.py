from django.db import models

class SingletonModel(models.Model):
    '''
    Abstract class for implementing the Singleton design pattern in Django models.

    This abstract class provides basic functionality for implementing the Singleton.
    The class creates or retrieves a single instance of the model and ensures
    that there is only one instance of this model throughout the entire application.
    The abstract attribute indicates that this is an abstract class,
    which is not mapped to any table in the database.
    '''

    class Meta:
        abstract = True

    @classmethod
    def singleton(cls):
        '''
        Class method for getting the single instance of the model.

        This method returns the single instance of the model,
        and if this instance does not exist, it creates it.
        Returns the model instance and a Boolean value indicating
        whether it was created (True) or retrieved (False).
        '''

        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def save(self, *args, **kwargs):
        '''
        Overridden save method.

        This method overrides the standard method for saving the model instance
        to always set the primary key to the value 1, ensuring that there will
        be only one instance of this model in the database.
        '''

        self.pk = 1
        super().save(*args, **kwargs)

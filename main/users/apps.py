from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        ''' Registrace manipulátorů pro signály. '''
        import users.signals.user_signals # noqa
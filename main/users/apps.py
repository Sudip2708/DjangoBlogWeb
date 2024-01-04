from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # Import signálů z modulu users.signals
    def ready(self):
        import users.models.signals
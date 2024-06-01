from django.apps import AppConfig

class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'

    def ready(self):
        ''' Registrace manipulátorů pro signály. '''
        import articles.signals.article_signals # noqa
        import articles.signals.article_author_signals  # noqa
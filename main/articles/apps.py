from django.apps import AppConfig

class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'

    def ready(self):
        ''' Signal Handler Registration. '''
        import articles.signals.article_signals # noqa
        import articles.signals.article_author_signals  # noqa
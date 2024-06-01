from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save,
)

from ..models.article_author import ArticleAuthor
from .article_author_handlers import (
    default_values_handler,
    profile_picture_handler,
)


# Zpracování defaultních hodnot
@receiver(pre_save, sender=ArticleAuthor)
def handle_title_slug(sender, instance, **kwargs):
    default_values_handler.handle_default_values_pre_save(instance)


# Zpracování profilového obrázku
@receiver(post_save, sender=ArticleAuthor)
async def handle_picture_post_save(sender, instance, **kwargs):
    await profile_picture_handler.handle_picture_post_save(instance)




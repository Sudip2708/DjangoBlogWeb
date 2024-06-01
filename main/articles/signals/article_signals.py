from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save,
    pre_delete,
    post_delete
)

from ..models.article import Article
from .article_handlers import (
    default_values_handler,
    delete_unused_tags_handler,
    status_update_handler,
    main_picture_handler,
    delete_article_handler
)


# Zpracování defaultních hodnot
@receiver(pre_save, sender=Article)
def handle_default_values_pre_save(sender, instance, **kwargs):
    default_values_handler.handle_default_values_pre_save(instance)


# Smazání nepoužívaných tagů
@receiver(post_save, sender=Article)
def handle_delete_unused_tags_post_save(sender, instance, **kwargs):
    delete_unused_tags_handler.handle_delete_unused_tags_post_save(instance)


# Zpracování statusu publish
@receiver(pre_save, sender=Article)
def handle_status_pre_save(sender, instance, **kwargs):
    status_update_handler.handle_status_pre_save(instance)

@receiver(post_save, sender=Article)
async def handle_status_post_save(sender, instance, **kwargs):
    await status_update_handler.handle_status_post_save(instance)


# Zpracování hlavního obrázku
@receiver(post_save, sender=Article)
async def handle_picture_post_save(sender, instance, **kwargs):
    await main_picture_handler.handle_picture_post_save(instance)


# Smazání článku
@receiver(pre_delete, sender=Article)
def handle_article_pre_delete(sender, instance, **kwargs):
    delete_article_handler.handle_article_pre_delete(instance)

@receiver(post_delete, sender=Article)
def handle_article_post_delete(sender, instance, **kwargs):
    delete_article_handler.handle_article_post_delete(instance)

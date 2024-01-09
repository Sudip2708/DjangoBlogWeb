# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import CustomUser
# from gallery.utils import process_and_save_image
#
# @receiver(post_save, sender=CustomUser)
# def post_save_process_profile_image(sender, instance, created, **kwargs):
#     # Pokud byl vytvořen nový uživatel (instance), provede se konverze formátu a zmenšení obrázku
#     if created and instance.profile_image:
#         process_and_save_image(instance, instance.profile_image, (300, 300), "profile_picture_300")

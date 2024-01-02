# models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(User, related_name='favorites', symmetrical=False, blank=True)

    def add_favorite(self, user):
        self.favorites.add(user)

    def remove_favorite(self, user):
        self.favorites.remove(user)

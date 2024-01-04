from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class UserProfile(models.Model):

    # Jednočlenný vztah k modelu User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Mnoho k mnoha vztah k modelu User pro seznam oblíbenců
    favorites = models.ManyToManyField(User, related_name='favorites', symmetrical=False, blank=True)

    # Pole pro ukládání data a času poslední úpravy instance UserProfile
    date_modified = models.DateTimeField(auto_now=True)

    # Pole pro obrázek profilu, s výchozím obrázkem a cestou pro uložení
    image = models.ImageField(default='img/profile_pics/default.jpg', upload_to='img/profile_pics')

    # Metoda, která definuje, jak bude instance UserProfile reprezentována jako řetězec
    def __str__(self):
        return self.user.username

    # Přetížená metoda pro ukládání profilu
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Otevření obrázku pomocí knihovny Pillow (PIL)
        img = Image.open(self.image.path)

        # Kontrola velikosti obrázku a jeho případné zmenšení
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    # Metoda pro přidání uživatele do seznamu oblíbenců
    def add_favorite(self, user):
        self.favorites.add(user)

    # Metoda pro odebrání uživatele ze seznamu oblíbenců
    def remove_favorite(self, user):
        self.favorites.remove(user)

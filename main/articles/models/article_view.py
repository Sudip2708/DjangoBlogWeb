print("### 15 main/articles/models/article_view.py")

### Definuje modely (tabulky) pro aplikaci.

from django.db import models
from django.contrib.auth import get_user_model

# Získání modelu uživatele použitého ve vaší aplikaci
User = get_user_model()


class ArticleView(models.Model):
    # Cizí klíč na uživatele, který zobrazil článek
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Cizí klíč na článek, který byl zobrazen
    article = models.ForeignKey('Article', on_delete=models.CASCADE)

    # Datum a čas vytvoření instance (zobrazení článku)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Textová reprezentace instance (pro administrační rozhraní a výpisy)
        return self.user.username

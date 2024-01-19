
from PIL import Image
import os
from django.core.files.storage import default_storage

class ArticleImagesProcessingMixin:
    def save(self, *args, **kwargs):
        print("save")

        if not self.pk:
            # Ověří zda je vytvořené umístění pro soubory, pokud ne, pak ho vytvoří
            os.makedirs(Article.main_picture_path(), exist_ok=True)

        if self.main_picture_for_article_tracker.has_changed('main_picture_for_article'):
            print("if self.main_picture_for_article_tracker.has_changed")

            # Vytvoření kopíí obrázku
            with Image.open(self.main_picture_for_article.path) as img:
                # Pro vysoké rozlišení
                img.thumbnail((1920, 1920))
                img.save(self.get_main_picture_max_size_path, 'JPEG')
                self.main_picture_max_size = self.get_main_picture_max_size_path

                # Pro variantu pro článek
                img.thumbnail((800, 800))
                img.save(self.get_main_picture_for_article_path, 'JPEG')
                # Tato varianta bude přidělena poli až po smazání aktuálně zpracovávaného obrázku

                # Pro náhledovou varianu
                img.thumbnail((450, 450))
                img.save(self.get_main_picture_preview_path, 'JPEG')
                self.main_picture_preview = self.get_main_picture_preview_path

                # Pro miniaturu
                img.thumbnail((60, 60))
                img.save(self.get_main_picture_miniature_path, 'JPEG')
                self.main_picture_miniature = self.get_main_picture_miniature_path

        # Volání původní metody save
        super(Article, self).save(*args, **kwargs)

        # Pokud toto pole neobsahuje defaultní hodnotu
        if self.main_picture_for_article != self.get_main_picture_for_article_path:
            try:
                # Fyzické smazání souboru
                image_path = self.main_picture_for_article.path
                if default_storage.exists(image_path):
                    default_storage.delete(image_path)

                # Nahrazení cesty v databázy
                self.main_picture_for_article = self.get_main_picture_for_article_path

                print("Soubor byl smazán a cesta změněna.")
            except Exception as e:
                print("Chyba po uložení:", str(e))
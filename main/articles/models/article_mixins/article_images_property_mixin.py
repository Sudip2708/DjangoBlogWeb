
import os

class ArticleImagesPropertyMixin:

    @classmethod
    def main_picture_path(cls):
        """
        Vrátí cestu k hlavní složce pro obrázky článků.
        """
        return 'media/images/articles/main_picture/'


    @property
    def get_main_picture_miniature_path(self):
        """
        Vrátí cestu pro miniaturu obrázku.
        """
        main_picture_path = Article.main_picture_path()
        picture_name = f"{self.slug}_amp_mini_60px.jpg"
        return os.path.join(main_picture_path, picture_name)


    @property
    def get_main_picture_preview_path(self):
        """
        Vrátí cestu pro náhledovou velikost obrázku.
        """
        main_picture_path = Article.main_picture_path()
        picture_name = f"{self.slug}_amp_preview_450px.jpg"
        return os.path.join(main_picture_path, picture_name)


    @property
    def get_main_picture_for_article_path(self):
        """
        Vrátí cestu obrázku velikosti pro článek.
        """
        main_picture_path = Article.main_picture_path()
        picture_name = f"{self.slug}_amp_article_800px.jpg"
        return os.path.join(main_picture_path, picture_name)


    @property
    def get_main_picture_max_size_path(self):
        """
        Vrátí cestu pro obrázek v nejvyšším rozlišení.
        """
        main_picture_path = Article.main_picture_path()
        picture_name = f"{self.slug}_amp_max_1920px.jpg"
        return os.path.join(main_picture_path, picture_name)
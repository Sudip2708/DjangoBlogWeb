### Definuje modely (tabulky) pro aplikaci.

from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse
from django.utils import timezone
from .article_author import ArticleAuthor
from .article_category import ArticleCategory
from .article_comment import ArticleComment
from articles.models.article_view import ArticleView
from autoslug import AutoSlugField
from taggit.managers import TaggableManager


class Article(models.Model):
    '''
    Model pro databázovou tabulku pro příspěvky

    Nápověda:
    [definice pole]
    models.CharField(): pole, které představuje textový řetězec v databázi
    models.TextField(): pole, které představuje delší textový řetězec bez omezení délky
    DateTimeField(): pole, které představuje datum a čas
    HTMLField(): pole, pro ukládání obsahu v HTML formátu
    models.IntegerField(): pole, které představuje celé číslo
    models.ForeignKey(): pole, které vytváří vztah k jinému modelu v databázi (cizí klíč)
    models.ImageField(): pole, pro ukládání obrázku
    models.ManyToManyField(): pole, které vytváří relaci mnoho k mnoha (many-to-many) mezi dvěma modely
    models.BooleanField(): pole, které je určené pro ukládání hodnoty boolean (True/False)
    [parametry]
    max_length: parametr, který určuje maximální délku textového řetězce (počet znaků)
    auto_now_add=True: parametr, který automaticky nastavuje hodnotu na aktuální datum a čas při vytváření instance modelu
    default: parametr, který umožňuje nastavit výchozí hodnotu pro pole
    Author: Model pro databázovou tabulku pro autora příspěvku
    on_delete=models.CASCADE: parametr, který definuje chování při smazání záznamu odkazovaného modelu (smaže spojený záznam při smazání odkazovaného záznamu)
    Category: Model pro databázovou tabulku pro kategorie příspěvků
    default=False: parametr, který nově vytvořeným záznamům automaticky nastavuje hodnotu na False
    'self': Tato hodnota je odkazem na model sám
    related_name='': Toto nastavení umožňuje specifikovat jméno, které bude použito pro vytvoření převráceného odkazu (reverse relation)
    on_delete=models.SET_NULL: Tato volba určuje chování, když je položka, na kterou odkazuje ForeignKey, odstraněna. V tomto případě, když je položka odstraněna, hodnota ForeignKey (previous_article) bude nastavena na NULL
    blank=True: Toto umožňuje pole v modelu být prázdné (nevyplněné) při validaci formuláře.
    null=True: Tato volba umožňuje hodnotě v databázi být NULL. Pokud není nastavena, hodnota ForeignKey by nemohla být prázdná (NULL)

    '''

    author = models.ForeignKey(ArticleAuthor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True)
    overview = models.TextField()
    content = HTMLField()
    thumbnail = models.ImageField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tags = TaggableManager()

    categories = models.ManyToManyField(ArticleCategory)

    comment_count = models.PositiveIntegerField(default=0)

    # Pole pro učení příspěvku pro hlavní stránku:
    featured = models.BooleanField(default=False)
    # Pole pro zobrazení předešlého vybraného článku:
    previous_article = models.ForeignKey('self',
                                      related_name='previous',
                                      on_delete=models.SET_NULL,
                                      blank=True,
                                      null=True)
    # Pole pro zobrazení dalšího vybraného článku:
    next_article = models.ForeignKey('self',
                                  related_name='next',
                                  on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True)

    # Indexování slugu:
    class Meta:
        indexes = [
            models.Index(fields=['slug'])
        ]


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        '''
        Funkce vytváří URL adresu pro pohled s názvem 'article-detail' a předává hodnotu primárního klíče (self.id) jako parametr do této URL adresy
        :return: Zpětná adresa na objekt

        Nápověda:
        reverse:  funkce vytváří URL adresu na základě názvu pohledu
        article-detail: představuje název pohledu, pro který se snažíme vytvořit URL adresu
        kwargs={'id': self.id}: představuje klíčové argumenty, které jsou použity ve vzoru URL adresy
        (V tomto případě je očekáván parametr s názvem 'id' (primární klíč, často používaný pro identifikaci záznamů v databázi), a hodnota tohoto parametru je nastavena na hodnotu self.id, což předpokládá, že váš model má atribut id (primární klíč) a chcete použít jeho hodnotu v URL adrese)
        '''
        return reverse('article-detail', kwargs={'slug': self.slug})

    # funkce pro úpravu příspěvku
    def get_update_url(self):
        return reverse('article-update', kwargs={
            'slug': self.slug
        })

    # funkce pro smazání příspěvku
    def get_delete_url(self):
        return reverse('article-delete', kwargs={
            'slug': self.slug
        })

    @property
    def get_comments(self):
        '''
        Definování funkce, která je přístupná jako atributy instance modelu.
        :return: Všechny komentáře (comments), které jsou připojeny k danému příspěvku (self), a řadí je podle časového razítka (created) sestupně (od nejnovějších k nejstarším).

        Nápověda:
        self.comments.all().order_by('-created'): SQlite qvivqlen - SELECT * FROM comments WHERE article_id = <ID_příspěvku> ORDER BY created DESC;
        '''
        return self.comments.all().order_by('-created')

    #
    # def get_comment_count(self):
    #     '''
    #     Definování funkce, která je přístupná jako atributy instance modelu.
    #     :return: Počet komentářů, které jsou připojeny k danému příspěvku (self). Používá metodu filter na modelu Comment, aby vyfiltrovala komentáře, které mají odkaz na aktuální příspěvek, a následně používá count k získání celkového počtu komentářů.
    #
    #     Nápověda:
    #     Comment.objects.filter(article=self).count(): SQlite qvivqlen - SELECT COUNT(*) FROM comments WHERE article_id = <ID_příspěvku>;
    #     '''
    #     return ArticleComment.objects.filter(article=self).count()

    @property
    def view_count(self):
        '''
        Definování funkce, která je přístupná jako atributy instance modelu.
        :return: počet zobrazení příspěvku. Podobně jako předchozí vlastnost, používá metodu filter na modelu ArticleView k nalezení všech zobrazení, která odkazují na aktuální příspěvek (self), a následně používá count k získání celkového počtu zobrazení.

        Nápověda:
        ArticleView.objects.filter(article=self).count(): SQlite qvivqlen - SELECT COUNT(*) FROM article_views WHERE article_id = <ID_příspěvku>;
        '''
        return ArticleView.objects.filter(article=self).count()

    @property
    def get_tags(self):
        '''
        Definování funkce, která je přístupná jako atributy instance modelu.
        :return: Všechny komentáře (comments), které jsou připojeny k danému příspěvku (self), a řadí je podle časového razítka (created) sestupně (od nejnovějších k nejstarším).

        Nápověda:
        self.comments.all().order_by('-created'): SQlite qvivqlen - SELECT * FROM comments WHERE article_id = <ID_příspěvku> ORDER BY created DESC;
        '''
        return self.tags.all()


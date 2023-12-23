### Definuje modely (tabulky) pro aplikaci.

from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse
from .author import Author
from .category import Category
from .comment import Comment
from posts.models.post_view import PostView

class Post(models.Model):
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
    on_delete=models.SET_NULL: Tato volba určuje chování, když je položka, na kterou odkazuje ForeignKey, odstraněna. V tomto případě, když je položka odstraněna, hodnota ForeignKey (previous_post) bude nastavena na NULL
    blank=True: Toto umožňuje pole v modelu být prázdné (nevyplněné) při validaci formuláře.
    null=True: Tato volba umožňuje hodnotě v databázi být NULL. Pokud není nastavena, hodnota ForeignKey by nemohla být prázdná (NULL)

    '''
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    # Pole pro učení příspěvku pro hlavní stránku:
    featured = models.BooleanField(default=False)
    # Pole pro zobrazení předešlého vybraného článku:
    previous_post = models.ForeignKey('self',
                                      related_name='previous',
                                      on_delete=models.SET_NULL,
                                      blank=True,
                                      null=True)
    # Pole pro zobrazení dalšího vybraného článku:
    next_post = models.ForeignKey('self',
                                  related_name='next',
                                  on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        '''
        Funkce vytváří URL adresu pro pohled s názvem 'post-detail' a předává hodnotu primárního klíče (self.id) jako parametr do této URL adresy
        :return: Zpětná adresa na objekt

        Nápověda:
        reverse:  funkce vytváří URL adresu na základě názvu pohledu
        post-detail: představuje název pohledu, pro který se snažíme vytvořit URL adresu
        kwargs={'id': self.id}: představuje klíčové argumenty, které jsou použity ve vzoru URL adresy
        (V tomto případě je očekáván parametr s názvem 'id' (primární klíč, často používaný pro identifikaci záznamů v databázi), a hodnota tohoto parametru je nastavena na hodnotu self.id, což předpokládá, že váš model má atribut id (primární klíč) a chcete použít jeho hodnotu v URL adrese)
        '''
        return reverse('post-detail', kwargs={'pk': self.id})

    # funkce pro úpravu příspěvku
    def get_update_url(self):
        return reverse('post-update', kwargs={
            'id': self.id
        })

    # funkce pro smazání příspěvku
    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'id': self.id
        })

    @property
    def get_comments(self):
        '''
        Definování funkce, která je přístupná jako atributy instance modelu.
        :return: Všechny komentáře (comments), které jsou připojeny k danému příspěvku (self), a řadí je podle časového razítka (timestamp) sestupně (od nejnovějších k nejstarším).

        Nápověda:
        self.comments.all().order_by('-timestamp'): SQlite qvivqlen - SELECT * FROM comments WHERE post_id = <ID_příspěvku> ORDER BY timestamp DESC;
        '''
        return self.comments.all().order_by('-timestamp')

    @property
    def comment_count(self):
        '''
        Definování funkce, která je přístupná jako atributy instance modelu.
        :return: Počet komentářů, které jsou připojeny k danému příspěvku (self). Používá metodu filter na modelu Comment, aby vyfiltrovala komentáře, které mají odkaz na aktuální příspěvek, a následně používá count k získání celkového počtu komentářů.

        Nápověda:
        Comment.objects.filter(post=self).count(): SQlite qvivqlen - SELECT COUNT(*) FROM comments WHERE post_id = <ID_příspěvku>;
        '''
        return Comment.objects.filter(post=self).count()

    @property
    def view_count(self):
        '''
        Definování funkce, která je přístupná jako atributy instance modelu.
        :return: počet zobrazení příspěvku. Podobně jako předchozí vlastnost, používá metodu filter na modelu PostView k nalezení všech zobrazení, která odkazují na aktuální příspěvek (self), a následně používá count k získání celkového počtu zobrazení.

        Nápověda:
        PostView.objects.filter(post=self).count(): SQlite qvivqlen - SELECT COUNT(*) FROM post_views WHERE post_id = <ID_příspěvku>;
        '''
        return PostView.objects.filter(post=self).count()
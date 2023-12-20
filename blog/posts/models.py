### Definuje modely (tabulky) pro aplikaci.


from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
'''
[from]
django.db: balíček, který poskytuje nástroje pro definici a práci s modely databáze
django.contrib.auth: balíček, který poskytuje funkcionality pro autentizaci a správu uživatelů
tinymce: knihovna TinyMCE (Tiny Moxiecode Content Editor), poskytuje možnosti formátování a editace obsahu pro webové stránky
[import]
models: modul, který obsahuje různé třídy a pole k definování struktury databáze
get_user_model: modul, který vrací třídu modelu uživatele (místo přímočarého odkazování na User má výhody, protože umožňuje flexibilitu v případě změny modelu uživatele ve vaší aplikaci)
HTMLField: pole, které umožňuje jednoduché a pohodlné začlenění WYSIWYG (What You See Is What You Get) editoru do vaší aplikace Django pro zadávání obsahu v HTML formátu
'''


User = get_user_model()
'''
get_user_model(): funkce, která vrací třídu modelu uživatele použitou ve vaší aplikaci
'''


class Author(models.Model):
    '''
    Model pro databázovou tabulku pro autora příspěvku

    Nápověda:
    models.OneToOneField(): pole, které vytváří vztah "jeden k jednomu" mezi dvěma modely
    models.ImageField(): pole, pro ukládání obrázku

    on_delete=models.CASCADE: parametr, který definuje chování při smazání záznamu odkazovaného modelu (smaže spojený záznam při smazání odkazovaného záznamu)

    User: funkce, která vrací třídu modelu uživatele použitou ve vaší aplikaci

    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    '''
    Model pro databázovou tabulku pro kategorie příspěvku

    Nápověda:
    models.CharField(): pole, které představuje textový řetězec v databázi

    max_length: parametr, který určuje maximální délku textového řetězce (počet znaků)

    '''
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    '''
    Model pro databázovou tabulku pro příspěvky

    Nápověda:
    [pole]
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
    on_delete=models.CASCADE: parametr, který definuje chování při smazání záznamu odkazovaného modelu (smaže spojený záznam při smazání odkazovaného záznamu)
    default=False: parametr, který nově vytvořeným záznamům automaticky nastavuje hodnotu na False
    [ostatní]
    Author: Model pro databázovou tabulku pro autora příspěvku
    Category: Model pro databázovou tabulku pro kategorie příspěvků

    '''
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    # comment_count = models.IntegerField(default = 0)
    # view_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False) # Pole pro učení příspěvku pro hlavní stránku

    def __str__(self):
        return self.title
### Definuje modely (tabulky) pro aplikaci.


from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.urls import reverse
'''
[from]
django.db: balíček, který poskytuje nástroje pro definici a práci s modely databáze
django.contrib.auth: balíček, který poskytuje funkcionality pro autentizaci a správu uživatelů
tinymce: knihovna TinyMCE (Tiny Moxiecode Content Editor), poskytuje možnosti formátování a editace obsahu pro webové stránky
django.urls: balíček, který poskytuje nástroje pro efektivní správu URL adres
[import]
models: modul, který obsahuje různé třídy a pole k definování struktury databáze
get_user_model: modul, který vrací třídu modelu uživatele (místo přímočarého odkazování na User má výhody, protože umožňuje flexibilitu v případě změny modelu uživatele ve vaší aplikaci)
HTMLField: pole, které umožňuje jednoduché a pohodlné začlenění WYSIWYG (What You See Is What You Get) editoru do vaší aplikace Django pro zadávání obsahu v HTML formátu
reverse: pole, které umožňuje získat odpovídající URL adresu pro daný pohled a oddělit definici URL adres od samotného kódu, což usnadňuje údržbu a změny URL struktury bez přímého zásahu do kódu
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
        Funkce vytváří URL adresu pro pohled s názvem 'post-detail' a předává hodnotu primárního klíče (self.pk) jako parametr do této URL adresy
        :return: Zpětná adresa na objekt

        Nápověda:
        reverse:  funkce vytváří URL adresu na základě názvu pohledu
        post-detail: představuje název pohledu, pro který se snažíme vytvořit URL adresu
        kwargs={'pk': self.pk}: představuje klíčové argumenty, které jsou použity ve vzoru URL adresy
        (V tomto případě je očekáván parametr s názvem 'pk' (primární klíč, často používaný pro identifikaci záznamů v databázi), a hodnota tohoto parametru je nastavena na hodnotu self.pk, což předpokládá, že váš model má atribut pk (primární klíč) a chcete použít jeho hodnotu v URL adrese)
        '''
        return reverse('post-detail', kwargs={'pk': self.pk})
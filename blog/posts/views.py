### Definuje pohledy (views), které obsluhují HTTP požadavky


from django.shortcuts import render
from .models import Post
from marketing.models import Signup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
'''
[from]
django.shortcuts: balíček, který obsahuje různé funkce zjednodušující vývoj webových aplikací.
.models: balíček, který se nachází ve stejném adresáři a slouží k definici modelů databázových tabulek
marketing.models: balíček, který se nachází v adresáři marketing a slouží k definici modelů databázových tabulek
django.core.paginator: balíček, který obsahuje nástroje a třídy související s paginací
django.db.models: balíček, který obsahuje různé nástroje a třídy pro definování modelů, dotazů a dalších součástí, které se používají při práci s databází
[import]
render: funkce, která se používá v pohledech (views) k renderování HTML šablon a generování HTTP odpovědí
Post: třída, modelu databázové tabulky pro příspěvky
Signup: třída, modelu databázové tabulky pro zápis k odebírání novinek
Paginator: třída, která slouží k rozdělování velkého seznamu objektů na stránky (části)
EmptyPage: výjimka, která se vyvolá, pokud uživatel požádá o stránku, která neexistuje.
PageNotAnInteger:  výjimka, která se vyvolá, pokud uživatel nezadá do URL celé číslo jako číslo stránky
Count:  třída, která reprezentuje agregační funkci pro počítání počtu prvků v sadě záznamů v databázi
'''

def get_category_count():
    '''
    Funkce používá Django ORM (Object-Relational Mapping) k získání agregovaných informací z modelu Post
    :return:
    Nápověda: Výpis kategorií s počtem výskytu jednotlivých kategorií
    Post.objects: Toto je manager objektu Post, který umožňuje provádět dotazy na databázi pro model Post.
    .values('categories__title'): Metoda values se používá k určení polí, která budou vybrána v dotazu. V tomto případě se vybírá pole title z připojených kategorií (categories) přes dvojité podtržítko (__). To znamená, že se vybírá název kategorie pro každý příspěvek.
    .annotate(Count('categories__title')): Metoda annotate se používá k agregaci dat. V tomto případě se používá funkce Count, aby se spočítal počet výskytů každého jedinečného názvu kategorie ve vybraných příspěvcích.
    '''
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset

def index(request):
    '''
    Definice pohledu pro úvodní stránku
    :param request: objekt reprezentující HTTP požadavek, který přichází od klienta (například webový prohlížeč)
    :return: HTTP odpověď obsahující obsah vygenerovaný z HTML šablony a může také obsahovat data předaná šabloně

    Nápověda:
    Post.objects.filter(featured=True): vytažení článků z databáze, které mají pole featured nastaveno na True (SELECT * FROM Post WHERE featured=True)
    Post.objects.order_by('-timestamp')[0:3]: vytažení posledních 3 článků z databáze (SELECT * FROM Post ORDER BY timestamp DESC LIMIT 3;)

    '''
    article_featured = Post.objects.filter(featured=True)
    article_latest = Post.objects.order_by('-timestamp')[0:3]

    context = {
        'article_featured': article_featured,
        'article_latest': article_latest,
    }

    if request.method == "POST":
        # doplnit validaci
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    return render(request, 'index.html', context)


def blog(request):
    '''
    Definice pohledu pro stránku se všemi příspěvky
    :param request: objekt reprezentující HTTP požadavek, který přichází od klienta (například webový prohlížeč)
    :return: HTTP odpověď obsahující obsah vygenerovaný z HTML šablony a může také obsahovat data předaná šabloně

    Nápověda:
    Post.objects.all(): vytažení všech článků z databáze (SELECT * FROM Post;)
    Paginator(articles, 4): vytvoření instance paginator a nastavení stránkování na 4 články na stránku
    request.GET.get(page_request_var): extrakce hodnoty 'page' z URL požadavku a přiřazení této hodnoty do proměnné page
    paginator.page(page): kód k získání konkrétní stránky z objektu Paginator
    PageNotAnInteger: výjimka, která se vyvolá, pokud uživatel nezadá do URL celé číslo jako číslo stránky
    paginator.page(1): kód získá první stránku z objektu Paginator
    EmptyPage: výjimka, která se vyvolá, pokud uživatel požádá o stránku, která neexistuje
    paginator.page(paginator.num_pages):  kód získá poslední stránku z objektu

    '''

    # Články s paginací pro hlavní obsah stránky
    articles = Post.objects.all().order_by('timestamp') # natažení dat z databáze
    paginator = Paginator(articles, 4) # vytvoření instance pro stránkování s nastavením počtu stránek
    page_request_var = 'page' # extrakce hodnoty 'page' z URL požadavku a přiřazení této hodnoty do proměnné page
    page = request.GET.get(page_request_var) # vyvtoření proměnné s číslem stránky
    try:
        paginated_articles = paginator.page(page) # přiřazení dávky článků
    except PageNotAnInteger:
        paginated_articles = paginator.page(1) # vyjímka zachytávající chybu, která se vyvolá, pokud uživatel nezadá do URL celé číslo jako číslo stránky (dojde k přesměrování na první stránku)
    except EmptyPage:
        paginated_articles = paginator.page(paginator.num_pages) # vyjímka zachytávající chybu, která se vyvolá, pokud uživatel požádá o stránku, která neexistuje (dojde na přesměrování na poslední stránku)

    # Seznam 3 nejnovějších článků pro boční panel
    most_recent_articles = Post.objects.order_by('-timestamp')[:3]

    # Seznam kategorií s počtem výskytu pro boční panel
    category_count = get_category_count()

    context = {
        'paginated_articles': paginated_articles,
        'page_request_var': page_request_var,
        'most_recent_articles': most_recent_articles,
        'category_count': category_count,
    }

    return render(request, 'blog.html', context)


def post(request, id):
    '''
    Definice pohledu pro stránku s jedním příspěvkem
    :param request: objekt reprezentující HTTP požadavek, který přichází od klienta (například webový prohlížeč)
    :param id:
    :return: HTTP odpověď obsahující obsah vygenerovaný z HTML šablony a může také obsahovat data předaná šabloně
    '''
    return render(request, 'post.html', {})
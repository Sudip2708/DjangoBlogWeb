### Definuje pohledy (views), které obsluhují HTTP požadavky


from django.shortcuts import render
from .models import Post
from marketing.models import Signup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
'''
[from]
django.shortcuts: balíček, který obsahuje různé funkce zjednodušující vývoj webových aplikací.
.models: balíček, který se nachází ve stejném adresáři a slouží k definici modelů databázových tabulek
marketing.models: balíček, který se nachází v adresáři marketing a slouží k definici modelů databázových tabulek
django.core.paginator: balíček, který obsahuje nástroje a třídy související s paginací
[import]
render: funkce, která se používá v pohledech (views) k renderování HTML šablon a generování HTTP odpovědí
Post: třída, modelu databázové tabulky pro příspěvky
Signup: třída, modelu databázové tabulky pro zápis k odebírání novinek
Paginator: třída, která slouží k rozdělování velkého seznamu objektů na stránky (části)
EmptyPage: výjimka, která se vyvolá, pokud uživatel požádá o stránku, která neexistuje.
PageNotAnInteger:  výjimka, která se vyvolá, pokud uživatel nezadá do URL celé číslo jako číslo stránky
'''


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
    Paginator(articles, 4): nastavení stránkování na 4 články na stránku
    request.GET.get(page_request_var): extrakce hodnoty 'page' z URL požadavku a přiřazení této hodnoty do proměnné page
    paginator.page(page): kód k získání konkrétní stránky z objektu Paginator
    paginator.page(1):  kód získá první stránku z objektu Paginator
    paginator.page(paginator.num_pages):  kód získá poslední stránku z objektu

    '''
    articles = Post.objects.all()
    paginator = Paginator(articles, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_articles = paginator.page(page)
    except PageNotAnInteger:
        paginated_articles = paginator.page(1)
    except EmptyPage:
        paginated_articles = paginator.page(paginator.num_pages)

    context = {
        'paginated_articles': paginated_articles,
        'page_request_var': page_request_var,
    }

    return render(request, 'blog.html', context)


def post(request):
    '''
    Definice pohledu pro stránku s jedním příspěvkem
    :param request: objekt reprezentující HTTP požadavek, který přichází od klienta (například webový prohlížeč)
    :return: HTTP odpověď obsahující obsah vygenerovaný z HTML šablony a může také obsahovat data předaná šabloně
    '''
    return render(request, 'post.html', {})
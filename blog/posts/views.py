### Definuje pohledy (views), které obsluhují HTTP požadavky


from django.shortcuts import render
from .models import Post
from marketing.models import Signup
'''
[from]
django.shortcuts: balíček, který obsahuje různé funkce zjednodušující vývoj webových aplikací.
.models: balíček, který se nachází ve stejném adresáři a slouží k definici modelů databázových tabulek
marketing.models: balíček, který se nachází v adresáři marketing a slouží k definici modelů databázových tabulek
[import]
render: funkce, která se používá v pohledech (views) k renderování HTML šablon a generování HTTP odpovědí
Post: třída, modelu databázové tabulky pro příspěvky
Signup: třída, modelu databázové tabulky pro zápis k odebírání novinek
'''


def index(request):
    '''
    Definice pohledu pro úvodní stránku
    :param request: objekt reprezentující HTTP požadavek, který přichází od klienta (například webový prohlížeč)
    :return: HTTP odpověď obsahující obsah vygenerovaný z HTML šablony a může také obsahovat data předaná šabloně

    Nápověda:

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
    '''
    return render(request, 'blog.html', {})


def post(request):
    '''
    Definice pohledu pro stránku s jedním příspěvkem
    :param request: objekt reprezentující HTTP požadavek, který přichází od klienta (například webový prohlížeč)
    :return: HTTP odpověď obsahující obsah vygenerovaný z HTML šablony a může také obsahovat data předaná šabloně
    '''
    return render(request, 'post.html', {})
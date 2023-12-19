### Definuje pohledy (views), které obsluhují HTTP požadavky


from django.shortcuts import render
'''
django.shortcuts: balíček, který obsahuje různé funkce zjednodušující vývoj webových aplikací.
render: funkce, která se používá v pohledech (views) k renderování HTML šablon a generování HTTP odpovědí
'''


def index(request):
    '''
    Definice pohledu pro úvodní stránku
    :param request: objekt reprezentující HTTP požadavek, který přichází od klienta (například webový prohlížeč)
    :return: HTTP odpověď obsahující obsah vygenerovaný z HTML šablony a může také obsahovat data předaná šabloně
    '''
    return render(request, 'index.html', {})


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
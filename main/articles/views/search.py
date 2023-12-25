### Definuje pohledy (views), které obsluhují HTTP požadavky


from django.shortcuts import render
from django.db.models import Q
from django.views.generic import View
from articles.models.article import Article
from marketing.forms import EmailSignupForm


form = EmailSignupForm()


class SearchView(View):
    '''
    Tento kód definuje pohled (SearchView) v rámci frameworku Django, který zdědil od třídy View.
    Pohled zpracovává HTTP GET požadavek na vyhledávání článků podle zadaného dotazu.
    Tento kód v podstatě umožňuje uživateli vyhledávat články podle zadaného dotazu a zobrazit výsledky na stránce 'search_results.html'.
    Klíčové body kódu:
    queryset = Article.objects.all(): Na začátku pohledu se vytvoří queryset obsahující všechny články z databáze.
    query = request.GET.get('q'): Získání hodnoty z parametru 'q' ve GET požadavku, což je dotaz zadaný uživatelem při vyhledávání.
    Podmíněné filtrování: Pokud je zadán dotaz (if query:), provede se filtrování článků podle titulu nebo přehledu, které obsahuje zadaný dotaz. Používá se Q objekt pro vytvoření složené podmínky (logické OR).
    distinct(): etoda distinct() slouží k odstranění duplicitních výsledků, pokud existují.
    Příprava kontextu: Vytváření slovníku context, který obsahuje výsledky vyhledávání.
    render(): Vykreslení šablony 'search_results.html' s předaným kontextem, který obsahuje výsledky vyhledávání.
    '''
    def get(self, request, *args, **kwargs):
        # Získání všech článků z databáze
        queryset = Article.objects.all()

        # Získání hodnoty z parametru 'q' ve GET požadavku (dotaz vyhledávání)
        query = request.GET.get('q')

        # Pokud je zadán dotaz, provede se filtrování článků podle titulu nebo přehledu
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |  # Hledání podle titulu (ignoruje velikost písmen)
                Q(overview__icontains=query)  # Hledání podle přehledu (ignoruje velikost písmen)
            ).distinct()  # Odstranění duplicitních výsledků

        # Příprava kontextu pro šablonu
        context = {
            'queryset': queryset  # Předání výsledků do šablony
        }

        # Vykreslení šablony s výsledky vyhledávání
        return render(request, 'search_results.html', context)

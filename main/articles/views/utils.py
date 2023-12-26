### Definuje pohledy (views), které obsluhují HTTP požadavky


from django.db.models import Count
from articles.models.article import Article
from marketing.forms import EmailSignupForm
from taggit.models import Tag


form = EmailSignupForm()

def get_category_count():
    '''
    Funkce používá Django ORM (Object-Relational Mapping) k získání agregovaných informací z modelu Article
    :return:
    Nápověda: Výpis kategorií s počtem výskytu jednotlivých kategorií
    Article.objects: Toto je manager objektu Article, který umožňuje provádět dotazy na databázi pro model Article.
    .values('categories__title'): Metoda values se používá k určení polí, která budou vybrána v dotazu. V tomto případě se vybírá pole title z připojených kategorií (categories) přes dvojité podtržítko (__). To znamená, že se vybírá název kategorie pro každý příspěvek.
    .annotate(Count('categories__title')): Metoda annotate se používá k agregaci dat. V tomto případě se používá funkce Count, aby se spočítal počet výskytů každého jedinečného názvu kategorie ve vybraných příspěvcích.
    .order_by('-categories__title__count'): Metoda pro řazení výsledků, zde podle počtu výskytů a sestupně
    '''
    queryset = Article.objects.values('categories__title').annotate(Count('categories__title')).order_by('-categories__title__count')

    return queryset



def get_author(user):
    qs = ArticleAuthor.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


# Definice filtrování podle tagu
def list_of_articles(request, tag_slug = None):
    articles = Article.publishedArticles.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        articles = articles.filter(tags__in=[tag])

    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page', 1)
    try:
        articles = paginator.page(page_number)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        articles = paginator.page(1)

    return render(request, 'blog/list.html', {'articles': articles, 'tag': tag})
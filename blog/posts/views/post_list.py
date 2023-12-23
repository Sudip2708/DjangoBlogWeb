### Definuje pohledy (views), které obsluhují HTTP požadavky


from django.views.generic import ListView
from posts.models.post import Post
from marketing.forms import EmailSignupForm
from .utils import get_category_count


form = EmailSignupForm()


class PostListView(ListView):
    '''
    Tento kód definuje pohled (PostListView) v rámci frameworku Django, který zdědil od třídy ListView.
    Tento pohled zobrazuje seznam článků v šabloně blog.html a zahrnuje také další informace, jako je nejnovější články, počet článků v každé kategorii a formulář pro přihlášení k odběru e-mailových aktualit.
    Celkově pohled PostListView představuje seznam článků s možností stránkování, a zároveň poskytuje další informace, které jsou přínosné pro šablonu.
    Klíčové body kódu:
    form = EmailSignupForm(): Tento řádek vytváří instanci formuláře pro přihlášení k odběru (EmailSignupForm) jako atribut třídy. Stejně jako v předchozím případě, tato instance formuláře je sdílena mezi všemi instancemi pohledu.
    model = Post: Tímto se určuje model, který bude použit pro získání dat pro pohled. V tomto případě se používá model Post.
    template_name = 'blog.html': Specifikuje název šablony, která bude použita pro vykreslení tohoto pohledu.
    context_object_name = 'queryset': Nastavuje název proměnné v kontextu šablony, která bude obsahovat seznam objektů získaných z databáze.
    paginate_by = 1: Určuje, kolik položek bude zobrazeno na jedné stránce. V tomto případě je nastaveno na 1, což znamená, že bude použit systém stránkování a každá stránka bude obsahovat jednu položku.
    get_context_data: Přetěžená metoda, která rozšiřuje kontext o další informace, jako jsou nejnovější články, počet článků v každé kategorii a formulář pro přihlášení k odběru e-mailových aktualit.
    '''
    form = EmailSignupForm()
    model = Post
    template_name = 'blog.html'
    # context_object_name = 'paginated_posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):

        # Získání informací o kategoriích a počtu článků v každé kategorii
        category_count = get_category_count()

        # Získání tří nejnovějších článků
        most_recent = Post.objects.order_by('-timestamp')[:3]

        # Příprava kontextu pro šablonu
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        context['category_count'] = category_count
        context['form'] = self.form

        return context

### Definice třídy pohledu pro hledání v článcích

from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse

from articles.models.article import Article
from articles.views.article_common_contex import CommonContextMixin


class SearchView(CommonContextMixin, ListView):
    # Použitý model pro zobrazení výsledků vyhledávání
    model = Article

    # Cesta k šabloně pro zobrazení výsledků vyhledávání
    template_name = '30_articles.html'

    # Počet výsledků na stránku
    paginate_by = 4

    def get(self, request, *args, **kwargs):
        # Získání vyhledávacího dotazu z URL nebo GET parametru
        query = self.request.GET.get('q')
        if query:
            # Přesměrování na stránku s výsledky vyhledávání
            return redirect(reverse('article-search-results', kwargs={'query': query}))
        else:
            # Pokud není zadán vyhledávací dotaz, pokračuj standardním získáním dat
            return super().get(request, *args, **kwargs)

    def get_queryset(self):
        # Získání vyhledávacího dotazu z URL nebo GET parametru
        query = self.kwargs.get('query') or self.request.GET.get('q')
        if query:
            # Filtrace článků podle titulu nebo přehledu obsahujícího vyhledávací dotaz
            queryset = Article.objects.filter(
                Q(title__icontains=query) | Q(overview__icontains=query)
            ).distinct()
            return queryset.order_by('-created')
        else:
            # Pokud není zadán vyhledávací dotaz, vrátit prázdnou množinu
            return Article.objects.none()

    def get_context_data(self, **kwargs):
        # Získání běžného kontextu a přidání vyhledávacího dotazu
        context = super().get_context_data(**kwargs)
        context['query'] = self.kwargs.get('query') or self.request.GET.get('q')
        return context


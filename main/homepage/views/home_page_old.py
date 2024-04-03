print("### main/articles/views/home_page.py")

### Definice třídy pohledu pro hlavní stránku

from django.shortcuts import render
from django.views.generic import View
from django.db.models import Count

from articles.models.article import Article

from homepage.forms.hero_section_form import HomePageHeroSectionForm
from homepage.models.hero_section import HomePageHeroSection


class HomePageView(View):




    def get(self, request, *args, **kwargs):
        # Získání featured článků, nejnovějších článků a nejčastěji zobrazených článků
        featured = Article.objects.filter(featured=True)
        latest = Article.objects.filter(status='publish').order_by('-created')[0:3]
        most_viewed = (
            Article.objects
            .annotate(views_count=Count('articleview'))
            .filter(status='publish')
            .order_by('-views_count')[:4]
        )

        # Určení zda je uživatel Super User
        superuser = False
        if request.user.is_superuser:
            superuser = True

        # Předání dat do kontextu pro zobrazení na domovské stránce
        context = {
            'superuser': superuser,
            'object_list': featured,
            'latest': latest,
            'most_viewed': most_viewed,

        }
        return render(request, '1_home/10__base__.html', context)

    def post(self, request, *args, **kwargs):

        pass


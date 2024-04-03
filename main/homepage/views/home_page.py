from django.shortcuts import render, redirect
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

        # Získání instance modelu HomePageHeroSection nebo vytvoření nové
        hero_instance, created = HomePageHeroSection.objects.get_or_create()

        # Inicializace formuláře s aktuálními hodnotami
        hero_form = HomePageHeroSectionForm(instance=hero_instance)

        # Určení zda je uživatel Super User
        superuser = request.user.is_superuser

        # Předání dat do kontextu pro zobrazení na domovské stránce
        context = {
            'superuser': superuser,
            'object_list': featured,
            'latest': latest,
            'most_viewed': most_viewed,
            'hero_form': hero_form,
        }

        # Pokud je adresa URL '/edit/', zobrazíme předvyplněné hodnoty v formuláři
        if request.path == '/edit/':
            return render(request, '1_home/10__base__.html', context)

        # Jinak zobrazíme normální domovskou stránku
        return render(request, '1_home/10__base__.html', context)


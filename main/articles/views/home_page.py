### Definice třídy pohledu pro hlavní stránku

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View
from django.db.models import Count

from articles.models.article import Article



class HomePageView(View):


    def get(self, request, *args, **kwargs):
        # Získání featured článků, nejnovějších článků a nejčastěji zobrazených článků
        featured = Article.objects.filter(featured=True)
        latest = Article.objects.order_by('-created')[0:3]
        most_viewed = (
            Article.objects
            .annotate(views_count=Count('articleview'))
            .order_by('-views_count')[:4]
        )

        # Předání dat do kontextu pro zobrazení na domovské stránce
        context = {
            'object_list': featured,
            'latest': latest,
            'most_viewed': most_viewed,

        }
        return render(request, '10_home.html', context)

    def post(self, request, *args, **kwargs):
        # # Zpracování odeslaného formuláře pro přihlášení k odběru e-mailů
        # email = request.POST.get("email")
        # new_signup = Signup()
        # new_signup.email = email
        # new_signup.save()
        #
        # # Zobrazení informační zprávy po úspěšném přihlášení k odběru
        # messages.info(request, "Successfully subscribed")
        # return redirect("home")
        pass


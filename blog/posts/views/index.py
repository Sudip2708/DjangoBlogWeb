### Definuje pohledy (views), které obsluhují HTTP požadavky


from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View
from posts.models.post import Post
from marketing.forms import EmailSignupForm
from marketing.models import Signup


form = EmailSignupForm()


class IndexView(View):
    '''
    Tento kód definuje pohled (IndexView) v rámci frameworku Django, který zdědil od základní třídy View.
    Tento pohled zpracovává dvě HTTP metody - GET a POST - a renderuje šablonu s informacemi o článcích, kde je k dispozici formulář pro přihlášení k odběru e-mailových aktualit.
    Tento kód předpokládá existenci modelu Post a Signup, formuláře EmailSignupForm a šablony index.html.
    Mějte na paměti, že v tomto kódu je formulář vytvořen jako atribut třídy (form = EmailSignupForm()), což znamená, že stejná instance formuláře bude sdílena mezi všechny instance pohledu.
    Klíčové body kódu:
    V get metodě se získávají dva seznamy článků: featured (označené jako "featured") a latest (tři nejnovější články). Tyto seznamy jsou součástí kontextu, který se předává do šablony pro zobrazení.
    V post metodě se získává e-mail z POST dat formuláře (request.POST.get("email")). Následně se vytváří nový záznam v databázi pro přihlášení k odběru (Signup model).
    Po uložení záznamu se zobrazí informační zpráva pomocí messages.info, a následně je uživatel přesměrován na domovskou stránku (redirect("home")).
    '''
    form = EmailSignupForm()

    def get(self, request, *args, **kwargs):

        # Získání článků označených jako "featured"
        featured = Post.objects.filter(featured=True)
        print(featured)

        # Získání tří nejnovějších článků
        latest = Post.objects.order_by('-timestamp')[0:3]
        print(latest)

        # Příprava kontextu pro šablonu
        context = {
            'object_list': featured,
            'latest': latest,
            'form': self.form
        }

        # Vykreslení šablony
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        # Získání e-mailu z POST dat formuláře
        email = request.POST.get("email")

        # Vytvoření nového záznamu v databázi pro přihlášení k odběru
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

        # Zobrazení informační zprávy
        messages.info(request, "Successfully subscribed")

        # Přesměrování na domovskou stránku
        return redirect("home")

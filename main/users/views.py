from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .utils.get_author_form import get_author_form
from .utils.prepare_profile_image import prepare_image
from articles.models.article_author import ArticleAuthor



# Definice pohledu pro stránku pro úpravu uživatelského účtu
@login_required
def profile_update(request):

    # Získání instance uživatele
    user = request.user



    # Nastavení pro zpracování dat vložených uživatelem
    if request.method == 'POST':

        # Načtení formuláře pro data uživatele
        user_form = UserProfileForm(request.POST, request.FILES, instance=user)

        # Načtení formuláře pro data autora
        author_form = get_author_form(request, user)



        # Kontrola, zda jsou formuláře pro uživatele a autora validní.
        if user_form.is_valid() and (author_form is None or author_form.is_valid()):

            # Kontrola, zda došlo ke změně profilového obrázku
            if user.tracker.has_changed('profile_image'):

                # Zpracování profilového obrázku a odstranění starého
                prepare_image(request, user_form, user)

            # Uložení formuláře užvatele
            user_form.save()



            # Ověření zda existuje i formulář pro autora
            if author_form:
                print("### author_form")
                print()

                # Získání instance autora
                author = ArticleAuthor.objects.get(user=user)

                print(author.tracker.previous('author_profile_picture').path)
                print(author.author_profile_picture.path)

                # Kontrola, zda došlo ke změně profilového obrázku
                if author.tracker.has_changed('author_profile_picture'):
                    print("### uthor.tracker.has_changed('author_profile_picture')")
                    print()

                    # Zpracování profilového obrázku a odstranění starého
                    prepare_image(request, author_form, author)

                # Uložení formuláře autora
                author_form.save()
                print("### author_form.save")
                print()



            # Zpráva o úspěšném uložení a přesměrování zpátky na stránku
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile_update')



    # Nastavení základního pohledu stránky
    else:

        # Načtení formuláře Uživatele
        user_form = UserProfileForm(instance=user)

        # Načtení formuláře autora
        author_form = get_author_form(request, user)



    # Příprava obsahu pro šablonu
    content = {
        'user_form': user_form,
        'author_form': author_form,
    }



    # Zobrazení stránky s formuláři
    return render(request, 'profile_update.html', content)



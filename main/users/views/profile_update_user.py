from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserProfileForm
from users.utils.change_profile_picture import change_profile_picture
from articles.models.article_author import ArticleAuthor
from users.forms import AuthorProfileForm


# Definice pohledu pro stránku pro úpravu uživatelského účtu
@login_required
def profile_update_user(request):

    # Načtení uživatele
    user = request.user

    # Nastavení pro zpracování dat vložených uživatelem
    if request.method == 'POST':

        # Načtení formuláře pro data uživatele
        user_form = UserProfileForm(request.POST, request.FILES, instance=user)

        # Kontrola, zda formulář obsahuje validní data
        if user_form.is_valid():

            # Název databázového pole
            field_name = 'profile_image'

            # Návratová adresa
            return_url = 'profile_update_user'

            # Kontrola, zda došlo ke změně profilového obrázku
            if user.profile_image_tracker.has_changed(field_name):

                # Zpracování profilového obrázku a odstranění starého
                change_profile_picture(request, user_form, user, field_name, return_url)

            # Uložení formuláře užvatele
            user_form.save()

            # Zpráva o úspěšném uložení a přesměrování zpátky na stránku
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect(return_url)


    # Nastavení základního pohledu stránky
    else:

        # Načtení formuláře Uživatele
        user_form = UserProfileForm(instance=user)


    author_form = None

    # Kontrola, zda má uživatel i účet autora
    if ArticleAuthor.user_is_author(user):

        # Načtení atura
        author = ArticleAuthor.objects.get(user=user)
        # author = ArticleAuthor.objects.get(user_id=user.id)

        # Načtení formuláře autora
        author_form = AuthorProfileForm(instance=author)


    # Příprava obsahu pro šablonu
    content = {
        'user_form': user_form,
        'author_form': author_form,
    }

    # Zobrazení stránky s formuláři
    return render(request, 'profile_update_user.html', content)




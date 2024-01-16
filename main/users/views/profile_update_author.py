from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from articles.models.article_author import ArticleAuthor
from users.forms.author_profile_form import AuthorProfileForm
from users.views.utils.change_profile_picture import change_profile_picture





# Definice pohledu pro stránku pro úpravu účtu autora
@login_required
def profile_update_author(request):

    # Načtení uživatele
    user = request.user

    # Načtení atura
    author = ArticleAuthor.objects.get(user=user)
    # author = ArticleAuthor.objects.get(user_id=user.id)

    # Nastavení pro zpracování dat vložených uživatelem
    if request.method == 'POST':

        # Načtení formuláře pro data uživatele
        author_form = AuthorProfileForm(request.POST, request.FILES, instance=author)

        # Kontrola, zda formulář obsahuje validní data
        if author_form.is_valid():

            # Název databázového pole
            field_name = 'author_profile_picture'

            # Návratová adresa
            return_url = 'profile_update_author'

            # Kontrola, zda došlo ke změně profilového obrázku
            if author.profile_picture_tracker.has_changed(field_name):

                # Zpracování profilového obrázku a odstranění starého
                change_profile_picture(request, author_form, author, field_name, return_url)

            # Uložení formuláře užvatele
            author_form.save()

            # Zpráva o úspěšném uložení a přesměrování zpátky na stránku
            messages.success(request, 'Your author profile has been updated successfully.')
            return redirect(return_url)

    # Nastavení základního pohledu stránky
    else:

        # Načtení formuláře Uživatele
        author_form = AuthorProfileForm(instance=author)

    # Příprava obsahu pro šablonu
    content = {
        'user_form': None,
        'author_form': author_form,
    }

    return render(request, '63_profile_update_author.html', content)

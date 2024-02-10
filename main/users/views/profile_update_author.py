from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from articles.models.article_author import ArticleAuthor
from users.forms.author_profile_form import AuthorProfileForm
from utilities.for_users.clean_profile_picture import clean_profile_picture


@login_required
def profile_update_author(request):
    '''
    Definice pohledu pro stránku pro správu účtu autora.

    :param request: Formulářový požadavek.
    :return: Stránka pro správu uživatelského účtu.
    '''

    # Načtení autora
    user = request.user
    author = ArticleAuthor.objects.get(user=user)


    # Nastavení pro POST
    if request.method == 'POST':

        # Načtení formuláře pro data uživatele
        author_form = AuthorProfileForm(request.POST, request.FILES, instance=author)

        # Kontrola, zda formulář obsahuje validní data
        if author_form.is_valid():

            # Validace a změna formátu obrázku
            if author.profile_picture_tracker.has_changed('profile_picture'):
                author_form = clean_profile_picture(author_form)

            # Uložení formuláře užvatele
            author_form.save()

            # Zpráva o úspěšném uložení a přesměrování zpátky na stránku
            messages.success(request, 'Your author profile has been updated successfully.')
            return redirect('profile_update_author')

    # Nastavení pro GET
    else:

        # Načtení formuláře Uživatele
        author_form = AuthorProfileForm(instance=author)

    # Příprava obsahu pro šablonu
    content = {
        'user_form': None,
        'author_form': author_form,
        'user_author': author,
    }

    # Vytvoření stránky
    return render(request, '6_profile_update/4___author__.html', content)

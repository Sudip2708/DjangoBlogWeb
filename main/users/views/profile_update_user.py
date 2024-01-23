from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from articles.models.article_author import ArticleAuthor
from users.forms.user_profile_form import UserProfileForm
from users.forms.author_profile_form import AuthorProfileForm
from utilities.for_users.clean_profile_picture import clean_profile_picture


@login_required
def profile_update_user(request):
    '''
    Definice pohledu pro stránku pro správu uživatelského účtu.

    :param request: Formulářový požadavek.
    :return: Stránka pro správu uživatelského účtu.
    '''

    # Načtení uživatele
    user = request.user


    # Nastavení pro POST
    if request.method == 'POST':

        # Načtení formuláře pro data uživatele
        user_form = UserProfileForm(request.POST, request.FILES, instance=user)

        # Kontrola, zda formulář obsahuje validní data
        if user_form.is_valid():

            # Validace a změna formátu obrázku
            if user.profile_picture_tracker.has_changed('profile_picture'):
                user_form = clean_profile_picture(user_form)

            # Uložení formuláře užvatele
            user_form.save()

            # Zpráva o úspěšném uložení a přesměrování zpátky na stránku
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile_update_user')

    # Nastavení pro GET
    else:

        # Načtení formuláře Uživatele
        user_form = UserProfileForm(instance=user)



    # Kontrola, zda má uživatel i účet autora
    if ArticleAuthor.user_is_author(user):

        # Načtení atura
        author = ArticleAuthor.objects.get(user=user)

        # Načtení formuláře autora
        author_form = AuthorProfileForm(instance=author)

    else:
        # Vrácení hodnoty None, v případě, že uživatel nemá i účet autora
        author_form = None



    # Příprava obsahu pro šablonu
    content = {
        'user_form': user_form,
        'author_form': author_form,
    }

    # Vytvoření stránky
    return render(request, '62_profile_update_user.html', content)




from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, AuthorProfileForm

@login_required
def profile_update(request):
    user = request.user

    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, request.FILES, instance=user)

        # Kontrola existence instance ArticleAuthor
        if hasattr(user, 'articleauthor'):

            # Vytvoření formuláře pro autora, pokud existuje
            author_form = AuthorProfileForm(request.POST, request.FILES, instance=user.articleauthor)
        else:
            author_form = None

        if user_form.is_valid() and (author_form is None or author_form.is_valid()):
            user_form.save()

            # Uložení informací o autorovi pouze v případě, že formulář existuje
            if author_form:
                author_form.save()

            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile_update')
    else:
        user_form = UserProfileForm(instance=user)

        # Kontrola existence instance ArticleAuthor
        if hasattr(user, 'articleauthor'):
            # Vytvoření formuláře pro autora, pokud existuje
            author_form = AuthorProfileForm(instance=user.articleauthor)
        else:
            author_form = None

    # Příprava obsahu pro šablonu
    content = {
        'user_form': user_form,
        'author_form': author_form,
    }

    # Zobrazení stránky s formuláři
    return render(request, 'profile_update.html', content)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.forms.profile_update_form import ProfileUpdateForm
from users.forms.user_update_form import UserUpdateForm
from users.models.user_profile_model import UserProfile

@login_required
def profile_update(request):

    #  Kontrola, zda byl odeslán HTTP požadavek typu POST.
    if request.method == 'POST':

        # Vytvoření formulářů pro aktualizaci uživatelských a profilových informací
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

        # Ověření, zda jsou data formulářů platná
        if u_form.is_valid() and p_form.is_valid():

            # Uložení aktualizovaných informací do databáze
            u_form.save()
            p_form.save()

            # Zobrazení zprávy o úspěšné aktualizaci účtu
            messages.success(request, f'Your account has been updated!')

            # Přesměrování na stránku s profilem
            return redirect('profile_update')

    else:
        # Vytvoření formulářů s aktuálními informacemi uživatele pro zobrazení
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    # Získání oblíbených autorů
    favorite_authors = request.user.userprofile.favorites.all()

    # Příprava kontextu pro zobrazení profilové stránky
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'favorite_authors': favorite_authors,
    }

    # Zobrazení profilové stránky s formulářem
    return render(request, 'profile_update.html', context)

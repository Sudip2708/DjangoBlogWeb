# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import FavoriteUserForm

@login_required
def manage_favorites(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = FavoriteUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            favorite_user = User.objects.get(username=username)

            if favorite_user != request.user:
                if request.user.userprofile.favorites.filter(username=username).exists():
                    user_profile.remove_favorite(favorite_user)
                else:
                    user_profile.add_favorite(favorite_user)

    form = FavoriteUserForm()
    favorites = user_profile.favorites.all()

    return render(request, 'manage_favorites.html', {'form': form, 'favorites': favorites})
from django.shortcuts import render

# Create your views here.

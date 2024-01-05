from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

@login_required
def profile_update(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile_update')
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'profile_update.html', {'form': form})
from django.shortcuts import render

# Create your views here.

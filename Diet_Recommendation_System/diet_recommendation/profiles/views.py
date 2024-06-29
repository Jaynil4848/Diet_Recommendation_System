# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

def homepage(request):
    return render(request, 'profiles/homepage.html')

@login_required
def view_profile(request):
    profile = request.user.userprofile
    if request.method=='GET':
        return render(request, 'profiles/profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'profiles/edit_profile.html', {'form': form})

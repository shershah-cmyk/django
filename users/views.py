from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# from .models import Profile
from .forms import ProfileForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created successfully!')
            return redirect('users:login')  # Redirect after successful registration
        else:
            # Add a message for invalid form
            messages.error(request, 'Registration failed. Please check the errors below.')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profilePage(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'users/profile.html', {'form': form})
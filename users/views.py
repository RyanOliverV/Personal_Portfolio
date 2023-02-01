from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        #uses a ready made template form for registering users
        form = UserRegistration(request.POST)
        #checks whether the submitted form is valid
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #outputs a flash message to let users know they have registered
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login') #after a user is registered it takes them to the login page
    else:
        form = UserRegistration()
    return render(request, 'users/register.html', {'form': form})

#This function creates a profile
#@login_required redirects a user to the login page if they aren't logged in
@login_required
def profile(request):
    if request.method == 'POST':
        #uses a ready made template form for updating profile information and image
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        #checks whether the submitted form is valid
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            #outputs a flash message to let users know they have updated their account
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
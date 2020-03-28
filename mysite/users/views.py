from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid() and form.cleaned_data.get('email')[10:] == 'iitd.ac.in':
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')

        if form.cleaned_data.get('email')[10:] != 'iitd.ac.in':
            context = {
                'form': form,
                'is_error': True,
                'error': 'Use XXXXXXXXX@iitd.ac.in email id!'
            }
            return render(request, 'users/register.html', context)
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form, 'is_error': False})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')


@login_required()
def update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Details updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/update.html', context)

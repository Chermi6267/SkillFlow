from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfilePlus
from . import forms
from django.contrib.auth import login, logout, authenticate
from .forms import UserProfilePlusForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Registration page
def registration_view(request):
    form = forms.CreateUserForm()
    form2 = forms.UserProfilePlusForm()
    context = {'form': form, "form2": form2}
    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)
        form2 = forms.UserProfilePlusForm(request.POST)
        if form.is_valid():
            form.save()
            user_id = User.objects.get(username=request.POST['username']).id
            UserProfilePlus.objects.filter(user=user_id).update(user_cat=request.POST['user_cat'])
            messages.success(
                request, 'Регистрация прошла успешно. Теперь вы можете войти в систему.')
            return redirect('login')
        else:
            context = {'form': form, 'errors': form.errors}
    context = {'form': form, "form2": form2}
    return render(request, 'register.html', context)


# Home page, UserProfilePlus
@login_required(login_url='login')
def home_page(request):
    try:
        profile = UserProfilePlus.objects.get(user=request.user)
    except UserProfilePlus.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = UserProfilePlusForm(
            request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            form = UserProfilePlusForm(instance=profile)
            return redirect('profile')
    else:
        form = UserProfilePlusForm(instance=profile)

    try:
        user_avatar = UserProfilePlus.objects.get(user=request.user).avatar.url
        context = {'form': form, 'user_avatar': user_avatar}
    except Exception:
        context = {'form': form}

    return render(request, 'profile.html', context)


# Login page
def login_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')

        else:
            messages.info(request, 'Неверный логин или пароль')
            return redirect('login')

    return render(request, 'login.html')


# Logout
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')

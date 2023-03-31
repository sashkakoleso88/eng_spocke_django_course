from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistratonForm, UserProfileForm
from django.contrib import auth, messages


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request=request, user=user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request=request, template_name='users/login.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistratonForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request, message='Поздравляем, регистрация успешна!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistratonForm()
    context = {'form': form}
    return render(request=request, template_name='users/register.html', context=context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title': 'Store - профиль', 'form': form}
    return render(request=request, template_name='users/profile.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


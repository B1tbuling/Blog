from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.views import View
from users.forms import *
from django.http import HttpResponse


def register_user(request):
    if request.method == 'GET':
        reg_form = UserCreationForm()
        return render(request, 'register_user.html', context={'form': reg_form})

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login_user_url'))
        else:
            return render(request, 'register_user.html', context={'form': form})


def login_user(request):
    if request.method == 'GET':
        log_form = AuthenticationForm()
        return render(request, 'login_user.html', context={'form': log_form})
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        form = AuthenticationForm(request.POST)
        if user:
            login(request, user)
            return redirect(reverse('main_page_url'))
        else:
            return render(request, 'login_user.html', context={'form': form})

        # if form.is_valid():
        #     authenticate()
        # else:
        #     return render(request, 'login_user.html', context={'form': form})


# class LoginUser(LoginView):
#     def get(self, request):
#         log_form = AuthenticationForm()
#         return render(request, 'login_user.html', context={'form': log_form})
#
#     def post(self, request):
#         AuthenticationForm(request.POST)
#         return redirect('main_page_url')




def logout_user(request):
    logout(request)
    return redirect('login_user_url')


def get_profile_user(request):
    profile_data = request.user
    return render(request, 'profile_user.html', context={'profile_data': profile_data})


from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.views import View
from users.forms import *
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import uuid


def register_user(request):
    if request.method == 'GET':
        reg_form = RegisterUserForm()
        return render(request, 'register_user.html', context={'form': reg_form})

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        print(request.POST)
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
    profile_data_form = ProfileDataUserForm(instance=request.user)
    profile_photo_form = ProfilePhotoUserForm()

    return render(request,
        'profile_user.html',
        context={
            'profile_data': profile_data,
            'profile_data_form': profile_data_form,
            'profile_photo_form': profile_photo_form
        }
    )


class UpdateProfilePhoto(View):

    def post(self, request):
        image = request.FILES['profile_image']
        image_name = f'profile_images/{uuid.uuid4()}'
        FileSystemStorage().save(image_name, image)
        request.user.profile_image = image_name
        request.user.save()
        return redirect('get_profile_user_url')


class UpdateProfileData(View):

    def post(self, request):
        print(request.POST)
        profile_data_form = ProfileDataUserForm(request.POST, instance=request.user)
        if profile_data_form.is_valid():
            profile_data_form.save()
            return redirect('get_profile_user_url')
        return redirect('get_profile_user_url')





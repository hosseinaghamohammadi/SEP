from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User



def sign_in(request):
    username = request.POST['username']

    # except (KeyError, uuser.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'website/first_page.html', {
    #         'error_message': "This username or password does not exists",
    #     })
    if username == "":
        return render(request, 'website/global_homepage.html', {
            'error_message': "You have not Entered a password",
        })

    print(username)
    try:
        user = get_object_or_404(User, pk=username)
    except:
        return render(request, 'website/global_homepage.html', {
            'error_message': "This username or password does not exists user error",
        })

    password = request.POST['password']
    if user.password != password:
        return render(request, 'website/global_homepage.html', {
            'error_message': "This username or password does not exists",
        })

    return HttpResponseRedirect(reverse('workseeker page'))


def employee(request):
    return render(request, 'website/employee_profile.html')


def edit_profile(request):
    return render(request, 'website/edit_profile.html')


def global_homepage(request):
    return render(request, 'website/global_homepage.html')
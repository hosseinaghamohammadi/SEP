from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import WorkSeeker, Employer, User


def first_page(request):
    return render(request, 'website/firstPage.html')


def sign_in(request):


    username = request.POST['username']

    # except (KeyError, uuser.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'website/firstPage.html', {
    #         'error_message': "This username or password does not exists",
    #     })
    if username == "":
        return render(request, 'website/firstPage.html', {
                    'error_message': "You have not Entered a password",
                })

    print(username)
    try:
        user = get_object_or_404(User, pk=username)
    except:
        return render(request, 'website/firstPage.html', {
                'error_message': "This username or password does not exists user error",
            })


    password = request.POST['password']
    if user.password != password:
        return render(request, 'website/firstPage.html', {
            'error_message': "This username or password does not exists",
        })



    return HttpResponseRedirect(reverse('workseeker page'))


def work_seeker(request):
    return HttpResponse("Workseeker fucking page")




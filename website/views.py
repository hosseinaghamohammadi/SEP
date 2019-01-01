from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import WorkSeeker, Employer, User




def first_page(request):
    return render(request, 'website/firstPage.html')


def sign_in(request):

    try:
        uusername = request.post['username']
        uuser = get_object_or_404(WorkSeeker, pk=uusername)
    # except (KeyError, uuser.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'website/firstPage.html', {
    #         'error_message': "This username or password does not exists",
    #     })
    except:
        return render(request, 'website/firstPage.html', {
            'error_message': "This username or password does not exists",
        })


    password = request.post['password']
    if uuser.password != password:
        return render(request, 'website/firstPage.html', {
            'error_message': "This username or password does not exists",
        })



    return HttpResponseRedirect(reverse('workseekerPage', args=(uuser)))
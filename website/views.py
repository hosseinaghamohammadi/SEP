from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import WorkSeeker, Employer, User


def first_page(request):
    return render(request, 'website/firstPage.html')


def sign_in_workseeker(request):
    type = "Work Seeker"
    attr = "workseeker"
    page = 'workseeker page'

    return sign_in(request, type, attr, page)


def sign_in_employer(request):
    type = "Employer"
    attr = "employer"
    page = 'employer page'

    return sign_in(request, type, attr, page)


def sign_in(request, type, attr, page):
    username = request.POST['username']
    try:
        user = get_object_or_404(User, pk=username)
    except:
        return render(request, 'website/firstPage.html', {
                'error_message': "{} with this username or password does not exists".format(type),
            })

    password = request.POST['password']
    if user.password != password:
        return render(request, 'website/firstPage.html', {
            'error_message': "{} with this username or password does not exists".format(type),
        })

    if not hasattr(user, attr):
        return render(request, 'website/firstPage.html', {
            'error_message': "{} with this username or password does not exists".format(type),
        })
    object = getattr(user, attr)
    return HttpResponseRedirect(reverse(page ,args=(object.id,)))


def work_seeker(request, workseeker_id):
    return HttpResponse("Workseeker fucking page")


def employer(request, employer_id):
    return HttpResponse("Employer fucking page")


def sign_up(request, type, attr, page):
    username = request.POST['username']
    try:
        user = get_object_or_404(User, pk=username)
    except:
        return render(request, 'website/firstPage.html', {
                'error_message': "{} with this username or password does not exists".format(type),
            })

    password = request.POST['password']
    if user.password != password:
        return render(request, 'website/firstPage.html', {
            'error_message': "{} with this username or password does not exists".format(type),
        })

    if not hasattr(user, attr):
        return render(request, 'website/firstPage.html', {
            'error_message': "{} with this username or password does not exists".format(type),
        })
    object = getattr(user, attr)
    return HttpResponseRedirect(reverse(page ,args=(object.id,)))

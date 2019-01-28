from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User


def sign_in_employee(request):
    type = "Employee"
    attr = "employee"
    page = 'employee page'

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
    return HttpResponseRedirect(reverse(page, args=(object.id,)))



def sign_up(request, type, attr, page):
    username = request.POST['username']
    try:
        user = get_object_or_404(User, pk=username)
    except:
        return render(request, 'website/global_homepage.html', {
            'error_message': "{} with this username or password does not exists".format(type),
        })

    password = request.POST['password']
    if user.password != password:
        return render(request, 'website/global_homepage.html', {
            'error_message': "{} with this username or password does not exists".format(type), })

    if not hasattr(user, attr):
        return render(request, 'website/firstPage.html', {
            'error_message': "{} with this username or password does not exists".format(type),
        })
    object = getattr(user, attr)
    return HttpResponseRedirect(reverse(page ,args=(object.id,)))


def employee(request):
    return render(request, 'website/employee_profile.html')


def edit_profile(request):
    return render(request, 'website/edit_profile.html')


def global_homepage(request):
    return render(request, 'website/global_homepage.html')


def employer(request):
    return render(request, 'website/employer_profile.html')


def employee_home(request):
    return render(request, 'website/employee_home.html')

from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import User, Employer, Employee



def get_mail(request, type):
    print(type)
    return render(request, 'website/getEmail.html', {"type":type})


def verify_mail(request, type):
    mail = request.POST['mail']

    user = User.objects.filter(mail= mail)
    if user.count() > 0:
        return render(request, 'website/getEmail.html', {
            'error_message': "This mail Already Exists".format(type),
            'type':type,
        })

    if type == 2:
        return redirect('fill form employee', mail)
    else:
        return redirect('fill form employer', mail)


def fill_form_employee(request, mail):
    return render(request, 'website/fillFormEmployee.html', {"mail":mail})


def fill_form_employer(request, mail):
    return render(request, 'website/fillFormEmployer.html', {"mail":mail})


def verify_form_employee(request, mail):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password 2']
    phone = request.POST['phone number']
    address = request.POST['address']
    dateOfBirth = request.POST['date of birth']
    user = User.objects.filter(username = username)
    if user.count() > 0:
        return render(request, 'website/fillFormEmployee.html', {
            'error_message': "Username Already Exists",
            'mail':mail,
        })
    data_user = {"mail":mail, "username":username, "password":password}
    data_employee = {"address":address, "birth_date":dateOfBirth}

    u = User(*data_user)
    u.save()
    w = Employee(address= address, birth_date=dateOfBirth, user=u, studentID=1222123282)
    w.save()
    # try:
    #     f = Phone(phoneNumber=phone, User = u)
    #     f.save()
    # except:
    #
    #     return render(request, 'website/fillFormEmployee.html', {
    #         'error_message': "Invalid phone number",
    #         'mail': mail,
    #     })

    return HttpResponseRedirect(reverse('employee page'))


def verify_form_employer(request,mail):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password 2']
    phone = request.POST['phone number']
    companyName = request.POST['companyName']
    companyAddress = request.POST['companyAddress']
    companyWebsite = request.POST.get('companyWebsite')


    user = User.objects.filter(username = username)

    if user.count() > 0:
        return render(request, 'website/fillFormEmployee.html', {
            'error_message': "Username Already Exists",
            'mail':mail,
        })
    data_user = {"mail":mail, "username":username, "password":password}
    data_employer = {"companyAddress":companyAddress, "companyName":companyName}

    u = User(*data_user)
    u.save()

    e = Employer(companyAddress=companyAddress, companyName = companyName, companyWebsite=companyWebsite, user=user)
    e.save()
    # try:
    #
    #     f = Phone(phoneNumber=phone, User=u)
    #     f.save()
    # except:
    #     return render(request, 'website/fillFormEmployer.html', {
    #         'error_message': "Invalid phone number",
    #         'mail': mail,
    #     })

    return HttpResponseRedirect(reverse('employer page', data_user))



def sign_up_employee(request):
    stdid = request.POST['stdid']

    try:
        employee = get_object_or_404(Employee, studentID=stdid)
    except:
        return render(request, 'website/global_homepage.html', {
            'error_message': "This studentID does not exists".format(type),
        })

    return HttpResponseRedirect(reverse('get mail', 2))


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

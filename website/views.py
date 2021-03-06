from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse
# from weasyprint import HTML
from .models import  Employer, Employee, Phone, EEExperience
from django.views.generic import CreateView
from weasyprint import HTML
from .forms import *
from .models import *
from .apps import WebsiteConfig
from sep.settings import BASE_DIR
from django.core.files.storage import FileSystemStorage
from django.db.models import Q

from website.models import EEExperience


def get_mail(request, type, stdid):
    return render(request, 'website/getEmail.html', {"type":type, "stdid":stdid})


def verify_mail(request, type, stdid):
    mail = request.POST['mail']

    user = MyUser.objects.filter(mail=mail)
    if user.count() > 0:
        return render(request, 'website/getEmail.html', {
            'error_message': "This mail Already Exists".format(type),
            'type':type,
            "stdid": stdid,
        })

    if type == 2:
        return redirect('fill form employee', mail, stdid)
    else:
        return redirect('fill form employer', mail)


def fill_form_employee(request, mail, stdid):
    return render(request, 'website/fillFormEmployee.html', {"mail":mail, "stdid":stdid})


def fill_form_employer(request, mail):
    return render(request, 'website/fillFormEmployer.html', {"mail": mail})


def verify_form_employee(request, mail, stdid):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password 2']
    phone = request.POST['phone number']
    address = request.POST['address']
    dateOfBirth = request.POST['date of birth']
    user = MyUser.objects.filter(username=username)
    if user.count() > 0:
        return render(request, 'website/fillFormEmployee.html', {
            'error_message': "Username Already Exists",
            'mail':mail,
            "stdid":stdid,
        })
    data_user = {"mail": mail, "username": username, "password": password}
    data_employee = {"address": address, "birth_date": dateOfBirth}

    MyUser.objects.create(**data_user)

    user = MyUser.objects.get(username=username)
    data_employee["user"] = user
    Employee.objects.create(**data_employee)

    try:
        Phone.objects.create(phoneNumber=phone, User = user)

    except:

        return render(request, 'website/fillFormEmployee.html', {
            'error_message': "Invalid phone number",
            'mail': mail,
        })

    return HttpResponseRedirect(reverse('employee page'))


def verify_form_employer(request, mail):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password 2']
    phone = request.POST['phone number']
    companyName = request.POST['companyName']
    companyAddress = request.POST['companyAddress']
    companyWebsite = request.POST.get('companyWebsite')

    user = MyUser.objects.filter(username=username)

    if user.count() > 0:
        return render(request, 'website/fillFormEmployee.html', {
            'error_message': "Username Already Exists",
            'mail': mail,
        })
    data_user = {"mail":mail, "username":username, "password":password}
    data_employer = {"companyAddress":companyAddress, "companyName":companyName, "companyWebsite":companyWebsite}


    # User.objects.create(mail = mail, username = username, password = password)

    user = MyUser(mail = mail, username = username, password = password)
    e = Employee(companyAddress = companyAddress, companyName = companyName, companyWebsite = companyWebsite)
    user.employer_set.add(e)
    e.user = user
    user.save()

    try:
        Phone.objects.create(phoneNumber=phone, User=user)

    except:

        return render(request, 'website/fillFormEmployee.html', {
            'error_message': "Invalid phone number",
            'mail': mail,
        })

    return HttpResponseRedirect(reverse('employer page'))



def sign_up_employee(request):
    stdid = request.POST['stdid']

    try:
        employee = get_object_or_404(Employee, studentID=stdid)
    except:
        return render(request, 'website/global_homepage.html', {
            'error_message': "This studentID does not exists".format(type),
        })

    return HttpResponseRedirect(reverse('get mail', 2, stdid))


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
        user = get_object_or_404(MyUser, pk=username)
    except:
        return render(request, 'website/global_homepage.html', {
            'error_message': "{} with this username or password does not exists".format(type),
        })

    password = request.POST['password']
    if user.password != password:
        return render(request, 'website/global_homepage.html', {
            'error_message': "{} with this username or password does not exists".format(type),
        })

    if not hasattr(user, attr):
        return render(request, 'website/global_homepage.html', {
            'error_message': "{} with this username or password does not exists".format(type),
        })
    object = getattr(user, attr)
    return HttpResponseRedirect(reverse(page, args=(object.id,)))


def sign_up(request, type, attr, page):
    username = request.POST['username']
    try:
        user = get_object_or_404(MyUser, pk=username)
    except:
        return render(request, 'website/global_homepage.html', {
            'error_message': "{} with this username or password does not exists".format(type),
        })

    password = request.POST['password']
    if user.password != password:
        return render(request, 'website/global_homepage.html', {
            'error_message': "{} with this username or password does not exists".format(type), })

    if not hasattr(user, attr):
        return render(request, 'website/global_homepage.html', {
            'error_message': "{} with this username or password does not exists".format(type),
        })
    object = getattr(user, attr)
    return HttpResponseRedirect(reverse(page, args=(object.id,)))


def employee_temp(request):
    ee = get_object_or_404(Employee, name = "saas")
    print(ee.family_name)
    return render(request, 'website/employee_profile_temp.html',  {'app_name':WebsiteConfig.name,'employee': ee})


def edit_profile(request):
    return render(request, 'website/edit_profile.html')


def global_homepage(request):
    # return render(request,'website/global_homepage.html')
    return employer(request, 1)
    # return render(request, 'website/search_page.html', {})


def employer_temp(request):
    return render(request, 'website/employer_profile_temp.html')


def employee_home(request):
    return render(request, 'website/employee_home.html')


def employee(request, employee_id):
    ee = get_object_or_404(Employee, id = employee_id)
    return render(request, 'website/employee_profile.html', {'employee': ee, 'employee_id': employee_id})


def get_pdf(request, employee_id):
    ee = get_object_or_404(Employee, id=employee_id)
    html_string = render_to_string('website/employee_profile.html', {'employee': ee, 'employee_id': employee_id})
    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/resume.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('resume.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
        return response


def delete_experience(request, employee_id, experience_pk):
    experience = get_object_or_404(EEExperience, pk=experience_pk)
    experience.delete()
    return HttpResponseRedirect(reverse('employee page', args=(employee_id,)))


def edit_experience(request, employee_id, experience_pk):
    experience = get_object_or_404(EEExperience, pk=experience_pk)
    if request.method == "POST":
        print(request.POST)
        experience.text = request.POST['text']
        experience.save()

    return HttpResponseRedirect(reverse('employee page', args=(employee_id,)))


def add_experience(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == "POST":
        EEExperience.objects.create(employee=get_object_or_404(Employee, id=employee_id), text=request.POST['text'])
    return HttpResponseRedirect(reverse('employee page', args=(employee_id,)))


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            return redirect('/website')
    else:
        form = SignUpForm()
    return render(request, 'website/signup.html', {'form': form})


def employee_profile_temp(request, employee_name):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        print(myfile)
        ee = get_object_or_404(Employee, name = employee_name)
        # result = urllib.urlretrieve(image_url)
        ee.image = myfile
        print(ee.image.url)
        print(ee.image)

        ee.save()
        return render(request, 'website/employee_profile_temp.html', {'app_name':WebsiteConfig.name,'employee': ee})
    return render(request, 'website/employee_profile_temp.html')

def search_page(request, employer_id):
    keyword = request.POST['search keyword']
    employee_list = Employee.objects.filter(Q(eeskill__name__contains=keyword) | Q(eeeducation__text__contains=keyword)
                            | Q(eeactivity__text__contains=keyword) | Q(eeexperience__text__contains=keyword)
                            | Q(eeinterest__text__contains=keyword))

    er = get_object_or_404(Employer, id=employer_id)
    return render(request, 'website/employer_profile.html', {'employee_list':employee_list, 'employer': er, 'employer_id': employer_id})



def employer(request, employer_id):
    er = get_object_or_404(Employer, id = employer_id)
    return render(request, 'website/employer_profile.html', {'employer': er, 'employer_id': employer_id})


class EmployerSignUpView(CreateView):
    model = MyUser
    form_class = EmployerSignUpForm
    template_name = 'website/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class EmployeeSignUpView(CreateView):
    model = MyUser
    form_class = EmployeeSignUpForm
    template_name = 'website/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')



def employer(request, employer_id):
    er = get_object_or_404(Employer, id = employer_id)
    return render(request, 'website/employer_profile.html', {'employer': er, 'employer_id': employer_id})


class EmployerSignUpView(CreateView):
    model = MyUser
    form_class = EmployerSignUpForm
    template_name = 'website/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class EmployeeSignUpView(CreateView):
    model = MyUser
    form_class = EmployeeSignUpForm
    template_name = 'website/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def delete_off(request, employer_id, empoff_pk):
    empoff = get_object_or_404(EmpOff, pk=empoff_pk)
    empoff.delete()
    return HttpResponseRedirect(reverse('employer page', args=(employer_id,)))


def edit_off(request, employer_id, empoff_pk):
    empoff = get_object_or_404(EmpOff, pk=empoff_pk)
    if request.method == "POST":
        print(request.POST)
        empoff.title = request.POST['title']
        empoff.position = request.POST['position']
        empoff.short_description = request.POST['short_description']
        empoff.long_description = request.POST['long_description']
        empoff.save()

    return HttpResponseRedirect(reverse('employer page', args=(employer_id,)))


def add_off(request, employer_id):
    if request.method == "POST":
        EmpOff.objects.create(employer=get_object_or_404(Employer, id=employer_id),
                              title=request.POST['title'], position=request.POST['position'],
                              short_description=request.POST['short_description'],
                              long_description=request.POST['long_description'])
    return HttpResponseRedirect(reverse('employer page', args=(employer_id,)))

def rate_off(request, employer_id, empoff_pk):
    empoff = get_object_or_404(EmpOff, pk=empoff_pk)
    if request.method == "POST":
        print(request.POST)
        empoff.rate = ((empoff.rate * empoff.vote_count) + request.POST['num'])
        empoff.vote_count = empoff.vote_count + 1
        empoff.save()

    return HttpResponseRedirect(reverse('employer page', args=(employer_id,)))

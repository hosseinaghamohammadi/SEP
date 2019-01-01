from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    username = models.CharField(max_length=20, default="dummy")
    password = models.CharField(max_length=20, default="dummy")
    mail = models.EmailField(default="fmansouri@gmail.com")

    def __str__(self):
        return self.username


class WorkSeeker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200,default="dummy")
    family_name = models.CharField(max_length=200,default="dummy")
    studentID = models.CharField(max_length=8, primary_key=True,default="95109253")
    nationalID = models.CharField(max_length=10,default="1234567891")
    address = models.CharField(max_length=400,default="dummy")
    sex = models.BooleanField(default=0)
    birth_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name + " " + self.family_name


class Phone(models.Model):
    workSeeker = models.ForeignKey(WorkSeeker, on_delete=models.CASCADE)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phoneNumber = models.CharField(validators=[phone_regex], max_length=17, blank=True,default="+98912988888")


class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    companyName = models.CharField(max_length=200,default="dummy")
    companyAddress = models.CharField(max_length=400,default="dummy")
    companyWebsite = models.URLField(default="google.com")
    rate = models.FloatField(default=1.1)

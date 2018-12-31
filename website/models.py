from django.db import models
from django.core.validators import RegexValidator


class WorkSeeker(models.Model):
    name = models.CharField(max_length=200)
    family_name = models.CharField(max_length=200)
    studentID = models.CharField(max_length=8, primary_key= True)
    nationalID = models.CharField(max_length=10)
    address = models.CharField(max_length=400)
    sex = models.BooleanField(default=0)
    birth_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name + " " + self.family_name


class Phone(models.Model):
    workSeeker = models.ForeignKey(WorkSeeker, on_delete=models.CASCADE)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phoneNumber = models.CharField(validators=[phone_regex], max_length=17, blank=True)


class User(models.Model):



class Employer(models.Model):
    companyName = models.CharField(max_length=200)
    companyAddress = models.CharField(max_length=400)
    companyWebsite = models.URLField()
    rate = models.FloatField(default=0)

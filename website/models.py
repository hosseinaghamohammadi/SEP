from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    username = models.CharField(max_length=20, default="dummy", primary_key= True)
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

    sex_Choices = [("1", "MALE"), ("2","FEMALE")]
    sex = models.CharField(max_length=9, choices=sex_Choices, default="FEMALE")

    birth_date = models.DateField()

    def __str__(self):
        return self.name + " " + self.family_name


class Phone(models.Model):
    workSeeker = models.ForeignKey(WorkSeeker, on_delete=models.CASCADE)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phoneNumber = models.CharField(validators=[phone_regex], max_length=17, blank=True,default="+98912988888")


class CV(models.Model):
    workSeeker = models.ForeignKey(WorkSeeker, on_delete=models.CASCADE)
    CV_text = models.FileField()
    picture = models.FileField()


class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    companyName = models.CharField(max_length=200,default="dummy")
    companyAddress = models.CharField(max_length=400,default="dummy")
    companyWebsite = models.URLField(default="google.com")
    rate = models.FloatField(default=1.1)


class JobOffer(models.Model):
    employer =  models.ForeignKey(Employer, on_delete=models.CASCADE)

    description = models.CharField(max_length=200,default="dummy")

    status_Choices = [("1","AVAILABLE"), ("2","NOT AVAILABLE")]
    status = models.CharField(max_length=20, choices=status_Choices, default="AVAILABLE")

    salary = models.IntegerField(default= 1000)


class Requirement(models.Model):
    jobOffer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)

    text = models.CharField(max_length=200,default="dummy")


class JobRequest(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    workSeeker = models.ForeignKey(WorkSeeker, on_delete=models.CASCADE)

    date = models.DateField()

    status_Choices = [("1", "AVAILABLE"), ("2", "NOT AVAILABLE")]
    status = models.CharField(max_length=20, choices=status_Choices, default="AVAILABLE")


class SystemAdmin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)




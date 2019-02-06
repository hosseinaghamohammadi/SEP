from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class MyUser(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Employee(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200, default="dummy")
    family_name = models.CharField(max_length=200, default="dummy")
    studentID = models.CharField(max_length=8, default="95109253")
    nationalID = models.CharField(max_length=10, default="1234567891")
    address = models.CharField(max_length=400, default="dummy")
    gender_choices = [("1", "MALE"), ("2", "FEMALE")]
    gender = models.CharField(max_length=9, choices=gender_choices, default="FEMALE")
    birth_date = models.DateField()
    image = models.ImageField(upload_to="profiles" , blank= True, null= True)

    def __str__(self):
        return self.name + " " + self.family_name


class Phone(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, default="+98912988888")


class Employer(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    employer_name = models.CharField(max_length=200, default="dummy")
    employer_address = models.CharField(max_length=400, default="dummy")
    employer_website = models.URLField(default="google.com")
    short_description = models.CharField(max_length=200, default="nothing")
    long_description = models.CharField(max_length=800, default="nothing")
    rate = models.FloatField(default=1.1)


class EmpOff(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default="Title")
    position = models.CharField(max_length=100, default="At witch position?")
    short_description = models.CharField(max_length=200, default="dummy")
    long_description = models.CharField(max_length=400, default="Enter your details.")
    rate = models.FloatField(default=10.0)
    vote_count = models.IntegerField(default=0)


class Requirement(models.Model):
    employment_offer = models.ForeignKey(EmpOff, on_delete=models.CASCADE)

    text = models.CharField(max_length=200, default="dummy")


class JobRequest(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    date = models.DateField()

    status_choices = [("1", "AVAILABLE"), ("2", "NOT AVAILABLE")]
    status = models.CharField(max_length=20, choices=status_choices, default="AVAILABLE")


class SystemAdmin(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)


class EEExperience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, default="")


class EEEducation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, default="")


class EECourse(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="")
    master = models.CharField(max_length=50, default="")
    grade = models.DecimalField(max_digits=4, decimal_places=2)


class EEHonor(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, default="")


class EESkill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="")
    level = models.CharField(max_length=30, default="")


class EEActivity(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, default="")


class EEInterest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    text = models.CharField(max_length=30, default="")

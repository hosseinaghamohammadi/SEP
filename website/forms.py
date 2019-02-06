from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import RadioSelect
from .models import *

class EmployerForm(forms.ModelForm):

    class Meta:
        model = Employer
        fields='__all__'

class EmployerSignUpForm(UserCreationForm):
    website_address=forms.URLField(required=True,label='input your website address ')
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )

    class Meta(UserCreationForm.Meta):
        model = MyUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employer = True
        user.save()
        employer = Employer.objects.create(user=user,)
        return user


class EmployeeSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employee = True
        if commit:
            user.save()
        return user

from django.forms import fields
from users.models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    bio = forms.CharField(max_length=10000)
    phone_number = forms.IntegerField()
    age = forms.IntegerField()


    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "age", "password1", "password2")


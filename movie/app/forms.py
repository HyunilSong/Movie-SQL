from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.db.models.base import Model

from .models import CustomerUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ['username', 'password1', 'password2', 'rank', 'phone_number']
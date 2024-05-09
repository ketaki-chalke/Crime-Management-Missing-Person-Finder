# forms.py
# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import GeneralPublic

class GeneralPublicForm(forms.ModelForm):
    class Meta:
        model = GeneralPublic
        fields = '__all__'

class UserAuthenticationForm(AuthenticationForm):
    pass
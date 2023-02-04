from django import forms
from .models import User_param
from django.contrib.auth.models import User


class User_param_form(forms.ModelForm):
    class Meta:
        model = User_param
        fields = ['gender','weight','height','age','activity','lactose','vegan']

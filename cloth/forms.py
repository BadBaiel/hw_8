from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class OrderClForm(forms.ModelForm):
    class Meta:
        model = models.OrderCl
        fields = '__all__'
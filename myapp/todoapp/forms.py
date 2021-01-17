from django import forms 
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    model= Task
    fields= '__all__'

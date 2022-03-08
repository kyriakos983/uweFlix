from django.forms import ModelForm
from .models import *



class StudentForm(ModelForm):
    class Meta:
        model = CinemaManager
        fields = ['username','password','student_name','student_email']


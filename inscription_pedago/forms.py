from django import forms

from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'surname', 'email', 'date_of_birth' ) #'date_of_birth',
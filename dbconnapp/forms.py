from django import forms
from dbconnapp.models import Student
class Student_form(forms.ModelForm):
    class Meta:
        model = Student
        fields='__all__'
from django.shortcuts import render,redirect
from dbconnapp.models import Student
from dbconnapp.forms import Student_form
# Create your views here.
def home(request):
    return render(request,'dbconnapp/home.html')

def display(request):
    student=Student.objects.all()
    return render(request,'dbconnapp/display.html',{'student':student})
def student_form(request):
    if request.method=="POST":
        ff=Student_form(request.POST)
        if ff.is_valid():
            ff.save()
            return redirect('display')
    else:    
      f=Student_form()
      return render(request,'dbconnapp/form.html',{'form':f})   


def Delete(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('display')
def Update(request,id):
    student=Student.objects.get(id=id)
    if request.method=="POST":
        ff=Student_form(request.POST,instance=student)
        if ff.is_valid():
            ff.save()
            return redirect('display')
    else:
        return render(request,'dbconnapp/Update.html',{'student':student})
from django.shortcuts import render
from django. http import HttpResponse
from .models import Student

# Create your views here.

def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')




def add_student(request):
    student = Student(name="Ravi", age=22, email="ravi@gmail.com")
    student.save()
    return HttpResponse("Student Saved Successfully")
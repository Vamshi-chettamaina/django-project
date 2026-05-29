from django.shortcuts import render
from app1.models import student
# Create your views here.
def display(request):
    data=student.objects.all()

    return render(request,'details.html',{'data':data})
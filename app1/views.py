from django.shortcuts import render,redirect
from app1.models import student
from app1.form import student_form
# Create your views here.
def display(request):
    data=student.objects.all()

    return render(request,'details.html',{'data':data})


def std_form(request):
    if request.method=='POST':
        form=student_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data')

    else:
        form =student_form()

     

    return render(request,'students.html',{'form':form})
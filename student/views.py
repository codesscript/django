from django.shortcuts import render, redirect
from .models import students
from django.http import HttpResponse
# Create your views here.
def student_form(request):
    return render(request,'index.html')
def student_info(request):
    if request.method=='POST':
        user_name=request.POST['username']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        contact=request.POST['mob']
        a=students(username=user_name,first_name=first_name,last_name=last_name,mob_no=contact)
        a.save()
        student = students.objects.all()
        return render(request, "show.html", {'student': student})
def show(request):
    student = students.objects.all()
    return render(request,"show.html",{'student':student})
def edit(request, id):
    stud = students.objects.get(id=id)
    return render(request,'edit.html', {'stud':stud})

def update(request, id):
    if request.method=='POST':
        user_name=request.POST['username']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        contact=request.POST['mob']
        students.objects.filter(id=id).update(username=user_name,first_name=first_name,last_name=last_name,mob_no=contact)
        return redirect("/show")
def delete(request,id):
    stud=students.objects.get(id=id)
    stud.delete()
    return redirect('/show')
from django.shortcuts import render, redirect

from cokotable1.models import Member


# Create your views here.

def Index(request):

     members = Member.objects.all()
     return render(request,"index.html",{"members":members})

def create(request):
     if request.method == "POST":
          f_name = request.POST['fname']
          l_name = request.POST['lname']
          new = Member.objects.create(first_name=f_name,last_name=l_name)
          new.save()
          return redirect('/')

def delete(request,id):
     mems = Member.objects.get(id=id)
     mems.delete()
     return redirect('/')

def edit(request,id):
     mem = Member.objects.get(id=id)
     return render(request,'about.html',{'member':mem})

def update(request,id):
     member = Member.objects.get(id=id)
     member.first_name = request.POST['fname']
     member.last_name = request.POST['lname']
     member.save()
     return redirect('/')







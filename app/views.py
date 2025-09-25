from django.shortcuts import redirect, render
from django.http import HttpResponse
from app.models import App

# Create your views here.

def index(request):
    person = App.objects.all().values()
    return render(request,'index.html',{'person':person})
    # return HttpResponse("Hello World")

def details(request,id):
    person_details = App.objects.get(id=id)
    return render(request,'details.html',{'person':person_details})

def main(request):
    return render(request,'main.html')

def testing(request):
    context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
    return render(request,'testing.html',context)

def add(request):
    return render(request,'add.html')

def add_record(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    new_member = App(firstname=fname, lastname=lname)
    new_member.save()
    return redirect('home')

def update(request,id):
    person = App.objects.get(id=id)
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        person.firstname = fname
        person.lastname = lname
        person.save()
        return redirect('home')
    return render(request,'update.html', {'person' : person})

def delete(request,id):
    person = App.objects.get(id=id)
    person.delete()
    return redirect('home')

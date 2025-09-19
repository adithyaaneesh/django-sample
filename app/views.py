from django.shortcuts import render
from django.http import HttpResponse
from app.models import App

# Create your views here.

def index(request):
    person = App.objects.all().values()
    return render(request,'home.html',{'person':person})
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
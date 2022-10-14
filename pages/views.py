from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pages/index.html',{"data":10})

def about (request):
    return render(request,'pages/about.html')

def homePage(request):
    return render(request,'index.html')
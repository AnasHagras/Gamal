from django.shortcuts import render
from .models import Login, Product
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import LoginForm
# Create your views here.
def index (request):
    ret = {
        "products" : Product.objects.all()
    }
    return render(request,'products/index.html',ret)

def about (request):
    if request.method == 'POST':
        userX = request.POST['username']
        password = request.POST['password']
        try :
            login = Login.objects.get(username=userX)
            if(login.password==password):
                print("Login")
            else :
                print("Invalid")
        except :
            print("Exception")
   
    return render(request,'products/about.html',{'lf':LoginForm})


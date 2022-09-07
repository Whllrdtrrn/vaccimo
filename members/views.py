
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

# def login_page(request):
#     template = loader.get_template('login_page.html')
#     return HttpResponse(template.render())
def login_page(request):
    
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username']  ,password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('information')
        else:
            return render (request,'login_page.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login_page.html')


# def register_page(request):
#     template = loader.get_template('register_page.html')
#     return HttpResponse(template.render())   
def register_page(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password_confirmation']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'register_page.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password'])
                auth.login(request,user)
                return redirect('loginpage')
        else:
            return render (request,'register_page.html', {'error':'Password does not match!'})
    else:
        return render(request,'register_page.html')
        
# def information_page(request):
#     template = loader.get_template('information.html')
#     return HttpResponse(template.render()) 
def information_page(request):
    if request.method == "POST":
        return redirect('sideeffect')      
    else:
        return render(request,'information.html')

# def sideeffect_page(request):
#     template = loader.get_template('sideeffect.html')
#     return HttpResponse(template.render()) 
def sideeffect_page(request):
    if request.method == "POST":
        return redirect('success')      
    else:
        return render(request,'sideeffect.html')

def success_page(request):
    template = loader.get_template('success.html')
    return HttpResponse(template.render()) 
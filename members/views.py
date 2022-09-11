from django.contrib.auth import authenticate
from django.contrib import messages

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
                return render (request,'login_page.html', {'error':'Invalid Username or Password'})
        
    else:
        return render(request,'login_page.html')
            


# def register_page(request):
#     template = loader.get_template('register_page.html')
#     return HttpResponse(template.render())   
def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password_confirmation']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register_page)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register_page)
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email)
                user.save()
                
                return redirect('loginpage')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register_page)
            

    else:
        return render(request, 'register_page.html')
    # if request.method == "POST":
    #     if request.POST['password'] == request.POST['password_confirmation']:
    #         try:
    #             User.objects.get(username = request.POST['username'])
    #             return render (request,'register_page.html', {'error':'Username is already taken!'})
    #         except User.DoesNotExist:
    #             user = User.objects.create_user(request.POST['username'],password=request.POST['password'])
    #             auth.login(request,user)
    #             return redirect('loginpage')
    #     else:
    #         return render (request,'register_page.html', {'error':'Password does not match!'})
    # else:
    #     return render(request,'register_page.html')
        
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

def dashboard (request):
    template = loader.get_template('system/dashboard.html')
    return HttpResponse(template.render()) 

def logout_user(request):
    auth.logout(request)
    return redirect('homepage')

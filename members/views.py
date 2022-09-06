from django.template import loader
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def login_page(request):
    template = loader.get_template('login_page.html')
    return HttpResponse(template.render())

def register_page(request):
    template = loader.get_template('register_page.html')
    return HttpResponse(template.render())   

def information_page(request):
    template = loader.get_template('information.html')
    return HttpResponse(template.render()) 

def sideeffect_page(request):
    template = loader.get_template('sideeffect.html')
    return HttpResponse(template.render()) 

def success_page(request):
    template = loader.get_template('success.html')
    return HttpResponse(template.render()) 
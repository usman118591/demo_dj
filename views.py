from django.shortcuts import render
from django.http import    HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
#Implmenting Loging and user autherthication using Forms
#Important implementation for auth.
from django.shortcuts import render_to_response #gives http back to browser
from django.http import HttpResponseRedirect #redirectionto browser
from django.contrib import auth #checking authentication
from django.core.context_processors import csrf #forgery request tokens prevention. Embedding a token with in your website.

# Create your views here.
def hello(request):
    name='Usman Siddiqui'
    html="<html><body>Hi %s .This seems to be working fine!</body></html>"%name
    return HttpResponse(html) # url(r'^accounts/signin.html/','blog.views.hello_template'),
#def hello_template(request):
   
 #   return render_to_response(request,'signin.html')
    
def home(request):
    return render(request,'airbnb.html')
#Auth views functions 
def login(request):
    c={}
    c.update(csrf(request)) #passing csrf token in our html doc
    return render_to_response('signin.html')

def auth_view(request):
    email=request.POST.get('email','')
    password=request.POST.get('password','')
    user=auth.authenticate(email=email,password=password)
    
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('success')
    else:
        return HttpResponseRedirect('invalid_login.html')

def loggedin(request):
    return render_to_response('loggedin.html')
def success(request):
    return render_to_response('success.html')
def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('/templates/airbnb.html')
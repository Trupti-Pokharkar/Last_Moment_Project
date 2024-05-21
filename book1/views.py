from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Course, Publication
# Create your views here.

def web(request):
    return render(request , 'web.htm')

def login(request):
    if request.method == 'POST':
        username =request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username , password = password,email=email)
        if user is not None:
            auth.login(request, user)
            print("Redirecting to web page")  # Add this line for debugging
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login.htm')
    else:
        return render(request, 'login.htm')

def sem21(request):
    return render(request ,'sem21.htm')

def sem22(request):
    return render(request,'sem22.htm')

def sem31(request):
    return render(request,'sem31.htm')

def sem32(request):
    return render(request,'sem32.htm')

def sem41(request):
    return render(request,'sem41.htm')

def sem42(request):
    return render(request,'sem42.htm')

def semi21(request):
    return render(request ,'semi21.htm')

def semi22(request):
    return render(request ,'semi22.htm')

def semi31(request):
    return render(request ,'semi31.htm')

def semi32(request):
    return render(request ,'semi32.htm')

def semi41(request):
    return render(request ,'semi41.htm')

def semi42(request):
    return render(request ,'semi42.htm')

def seme21(request):
    return render(request ,'seme21.htm')

def seme22(request):
    return render(request ,'seme22.htm')

def seme31(request):
    return render(request ,'seme31.htm')

def seme32(request):
    return render(request ,'seme32.htm')

def seme41(request):
    return render(request ,'seme41.htm')

def seme42(request):
    return render(request ,'seme42.htm')

def logout(request):
    auth.logout(request)
    return redirect('/')

def about(request):
    return render(request,'about.htm')

def first(request):
    return render(request,'first.htm')


        


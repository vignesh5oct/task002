from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .models import Otp
from django.http import JsonResponse
from .utils import generate_otp,verify_otp


def home(request):

    return render(request,'blog/home.html')

def login_user(request):

    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            userObj = User.objects.get(email=email)
            username = userObj.username
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
        except Exception as e:
            print(e,"eroorroor")
        
    return render(request,'blog/login.html')


@login_required
def dashboard(request):

    return render(request,'blog/dashboard.html')


def register(request):

    return render(request,'blog/register.html')


def generated_otp(request):

    generated_otp = generate_otp()
    
    return JsonResponse({"generated_otp":generated_otp})

def verify_generated_otp(request):

    context={}

    if request.method =='POST':
        otp = request.POST.get('otp')
        is_otp_valid = verify_otp(otp)

        print("verify_otp",is_otp_valid)

        context ={"otp":otp,"is_otp_valid":is_otp_valid}

    return JsonResponse(context)

def logout_user(request):
    logout(request)
    return redirect('login_user')  

def image_preview(request):

    return render(request,'blog/image_preview.html')

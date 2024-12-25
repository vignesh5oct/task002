from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .models import Otp,Proposal
from django.http import JsonResponse
from .utils import generate_otp,verify_otp
import json
from django.views.decorators.csrf import csrf_exempt

from .forms import UserRegistrationForm
from django.contrib import messages

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
                messages.info(request,"log in.")
                return redirect('dashboard')
        except Exception as e:
            print(e,"eroorroor")
        
    return render(request,'blog/login.html')


@login_required
def dashboard(request):

    return render(request,'blog/dashboard.html')


def register(request):

    if request.method == "POST":
        registerForm = UserRegistrationForm(request.POST)

        if registerForm.is_valid():

            registerForm.save()
            messages.info(request,"Your account has been created! You can now log in.")
            return redirect("login_user")
        else: #invalid case
            print (registerForm.is_valid())  #form contains data and errors
            # op=registerForm.errors

            messages.info(request,"Email Already Exists")
    # else:
    #     registerForm = UserRegistrationForm()

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

    return render(request,'blog/image_preview_2.html')

@login_required
def add_proposals(request):

    user = User.objects.get(id = request.user.id)
 
    if request.method =='POST':
        title = request.POST.get('title')
        proposal = request.POST.get('proposal')
        option_one = request.POST.get('option_one')
        option_two = request.POST.get('option_two')
        option_three = request.POST.get('option_three')

        if option_one == '' and option_two == '' and option_three == '':
            Proposal.objects.create(title=title,proposal=proposal,user_id=user.id)
            print("newProposal added without options")
            return redirect('dashboard')

        else:
            Proposal.objects.create(title=title,proposal=proposal,option_one=option_one,option_two=option_two,option_three=option_three,user_id=user.id)
            print("newProposal added")
            return redirect('dashboard')
   

    return render(request,'blog/add_proposals.html')

@login_required
def proposals(request):

    proposals = Proposal.objects.all()

    context = {"proposals":proposals}

    return render(request,'blog/proposals.html',context)


@login_required
def vote_proposals(request,id):

    proposals = Proposal.objects.all()
    context = {"proposals":proposals}

    proposals = Proposal.objects.get(id=id)
    if request.method =='POST':
        voted = request.POST.get('voted')
        print(voted)
        if voted == proposals.option_one:
            proposals.option_one_votes = proposals.option_one_votes + 1
            print(proposals.option_one)
            print(proposals.option_one_votes)

        elif voted == proposals.option_two:
            proposals.option_two_votes = proposals.option_two_votes + 1
            print(proposals.option_two)
            print(proposals.option_two_votes)

        elif voted == proposals.option_three:
            proposals.option_three_votes = proposals.option_three_votes + 1
            print(proposals.option_three)
            print(proposals.option_three_votes)


    print('pro',proposals.title)
 
 
    return render(request,'blog/proposals.html',context)

def update_choice(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        selected_option = data.get('choice')

        # Process the selected option (e.g., save to database)
        print(f"Selected Option: {selected_option}")

        return JsonResponse({'status': 'success', 'message': 'Option saved!', 'selected_option': selected_option})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
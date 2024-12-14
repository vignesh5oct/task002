from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .models import Otp,Proposal,Choice
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

@login_required
def add_proposals(request):

    user = User.objects.get(id = request.user.id)
 
    if request.method =='POST':
        title = request.POST.get('title')
        proposal = request.POST.get('proposal')
        newProposal = Proposal.objects.create(title=title,proposal=proposal,user_id=user.id)
        Choice.objects.create(proposal_id=newProposal.id)
        print("added")
        return redirect('dashboard')
   

    return render(request,'blog/add_proposals.html')

@login_required
def proposals(request):
    user = User.objects.get(id = request.user.id)
    proposals = Proposal.objects.all()

    choices = Choice.objects.all()
 
    context = {"proposals":proposals,"choices":choices}
 
    if request.method =='POST':
        vote_proposal_id = request.POST.get('vote')

        selected_proposal = Proposal.objects.get(id = vote_proposal_id)

        print(selected_proposal.title)
        print(selected_proposal.proposal)

        if vote_proposal_id:
            print(vote_proposal_id)
            # Choice.objects.create(vote=vote)

   

    return render(request,'blog/proposals.html',context)
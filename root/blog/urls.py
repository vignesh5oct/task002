from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login_user/',views.login_user,name='login_user'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('generated-otp/',views.generated_otp,name='generated_otp'),
    path('verify-generated-otp/',views.verify_generated_otp,name='verify_generated_otp'),

    path('image-preview/',views.image_preview,name='image_preview'),

    path('add_proposals/',views.add_proposals,name='add_proposals'),
    path('proposals/',views.proposals,name='proposals'),
    path('vote-proposals/<int:id>/',views.vote_proposals,name='vote_proposals'),

    path('update_choice/',views.update_choice,name='update_choice'),


    
]
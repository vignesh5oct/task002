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

    
]
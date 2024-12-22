from django.db import models
from django.contrib.auth.models import User


class Otp(models.Model):
    otp=models.IntegerField(default=None,null=True)
    
class Proposal(models.Model):
    title = models.CharField(max_length=255,default=None,null=True)
    proposal = models.CharField(max_length=255,default=None,null=True)
    option_one = models.CharField(max_length=255,default="Good Proposal",null=True)
    option_two = models.CharField(max_length=255,default="Bad Proposal",null=True)
    option_three = models.CharField(max_length=255,default="Not an valid Proposal",null=True)
    option_one_votes = models.IntegerField(default=0,null=True)
    option_two_votes = models.IntegerField(default=0,null=True)
    option_three_votes = models.IntegerField(default=0,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    


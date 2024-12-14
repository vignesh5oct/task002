from django.db import models
from django.contrib.auth.models import User


class Otp(models.Model):
    otp=models.IntegerField(default=None,null=True)
    
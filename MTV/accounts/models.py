from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nickname=models.CharField(max_length=100)
    university=models.CharField(max_length=50)
    location=models.CharField(max_length=200)
    #토이프로젝트하다가 뭔가 추가하고싶으면 자유롭게 추가
    #성별이나 권한..?
# Create your models here.

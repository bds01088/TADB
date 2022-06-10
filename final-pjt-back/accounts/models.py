from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser) :
    image = models.ImageField(upload_to='images/', default='defaultProfile.png')
    overview = models.TextField(default="회원님의 선호를 반영한 배우 추천입니다.")

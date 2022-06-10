from movies.models import Movie
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator 

class Actor(models.Model):
    birthday = models.TextField(null=True)
    deathday = models.TextField(null=True)
    actor_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    place_of_birth = models.TextField(null=True)
    profile_path = models.TextField(null=True)
    overview = models.TextField(null=True)
    score = models.FloatField(default=0, blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='actors') 
    movie = models.ManyToManyField(Movie, through='Character')

class Character(models.Model):
    charactername = models.CharField(max_length=100, null=True)
    score = models.FloatField(default=0, blank=True)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='comments')
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)]) 
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)


from django.db import models

# Create your models here.
class Movie(models.Model): 
    movie_id = models.IntegerField(unique=True)
    overview = models.TextField()
    popularity =  models.FloatField()
    poster_path = models.TextField(null=True)
    release_date = models.TextField(default="", null=True)
    title = models.CharField(max_length=50)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    genre = models.TextField(null=True)
    tagline = models.TextField(null=True)
    runtime = models.IntegerField(null=True)
    trailer_key = models.TextField(null=True)
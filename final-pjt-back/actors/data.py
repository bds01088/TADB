from django.db import models

from movies.models import Movie
from actors.models import Character, Actor
from django.shortcuts import get_list_or_404, render, get_object_or_404
import requests

for k in range(8266, 10001):
    movie = get_object_or_404(Movie, pk=k)
    id = movie.movie_id
    url = f"https://api.themoviedb.org/3/movie/{id}/credits?api_key=0b9bf42f647ecf2055be8ac552db3a0d&language=ko-kr"
    character = requests.get(url).json()
    l = min(len(character['cast']), 5)
    for i in range(l):
        print(movie.movie_id) 
        actorid = character['cast'][i]['id']
        if not Actor.objects.filter(actor_id = actorid).exists() :
            act = Actor()
            actordetailURL = f"https://api.themoviedb.org/3/person/{actorid}?api_key=0b9bf42f647ecf2055be8ac552db3a0d&language=ko-kr"
            detail = requests.get(actordetailURL).json()
            act.actor_id = actorid
            act.name = detail['name']
            act.profile_path = detail['profile_path']
            act.birthday = detail['birthday']
            act.deathday = detail['deathday']
            act.place_of_birth = detail['place_of_birth']
            act.save()

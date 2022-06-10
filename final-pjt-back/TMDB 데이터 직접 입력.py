from asyncio.windows_events import NULL
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finalpjt.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from movies.models import Movie
from actors.models import Actor, Character
from django.shortcuts import get_list_or_404, get_object_or_404
import requests

def movie():
# Popular 요청    
    url = "https://api.themoviedb.org/3/movie/popular?api_key=0b9bf42f647ecf2055be8ac552db3a0d&language=ko-kr&page="   
    for i in range(1, 501): # 1~23, 23~
        URL = url+str(i)
        movies = requests.get(URL).json()
        for movie in movies['results'] :
            if not Movie.objects.filter(movie_id = movie['id']).exists() :
                data = Movie()
                data.title = movie['title']
                data.overview = movie['overview']
                data.popularity = movie['popularity']
                data.poster_path = movie['poster_path']
                data.vote_average = movie['vote_average']
                data.vote_count = movie['vote_count']
                data.movie_id = movie['id']
                if movie.get('release_date'): # get은 에러 발생x, []은 값이 없으면 key error
                    data.release_date = movie['release_date']
                data.save()
# Nulll값 탐색
    # movies = Movie.objects.filter(runtime__isnull = True)
    # for movie in movies:
    #     print(movie.movie_id)
# Detail 요청    
    # for i in range(1, 9987): 
    #     data = get_object_or_404(Movie, pk=i)
    #     detail_url = 'https://api.themoviedb.org/3/movie/'+ str(data.movie_id) + '?api_key=0b9bf42f647ecf2055be8ac552db3a0d&language=ko-kr'
    #     detail = requests.get(detail_url).json()
    #     for genre in detail['genres']:
    #         if data.genres:
    #             data.genres += ' ' + genre['name']
    #         else:
    #             data.genres = genre['name']
    #     data.runtime = detail['runtime']70429	위치 헌트		171.629	/vHKlIci8f38GaAd361EW0VSx91k.jpg	7.0	186	판타지 공포 스릴러 드라마	92		NULL	2021-10-01
    #     data.tagline = detail['tagline']
# Viedos 요청 226 3082 4723 4923    
    # for i in range(4923, 9987): 
    #     data = get_object_or_404(Movie, pk=i)
    #     video_url = "https://api.themoviedb.org/3/movie/"+ str(data.movie_id) + "/videos?api_key=0b9bf42f647ecf2055be8ac552db3a0d&language=ko-kr"
    #     video = requests.get(video_url).json()
    #     if len(video['results']) :
    #         data.trailer_key = video['results'][0]['key']
    #     data.save()
    #     print(i)

# 2294 movie_id 959901는 credit 요청 결과가 없음
# 2372 movie_id 960613는 credit 요청 결과가 없음
# 5216 부터 다시 8105 8494 8822x 8823 9004부터
def actor():
    for k in range(8823, 9987):
        movie = get_object_or_404(Movie, pk=k)
        id = movie.movie_id
        url = f"https://api.themoviedb.org/3/movie/{id}/credits?api_key=0b9bf42f647ecf2055be8ac552db3a0d&language=ko-kr"
        character = requests.get(url).json()
        l = min(len(character['cast']), 5)
        print(k)
        for i in range(l):
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
# 884 movie_id 350499는 cast가 없음
# 2294 movie_id 959901는 credit 요청 결과가 없음
# 2372 movie_id 960613는 credit 요청 결과가 없음
# 1186
# 1273 매칭되는 actor X
# 1311
def character():
    for k in range(1312, 9987):
        movie = get_object_or_404(Movie, pk=k)
        id = movie.movie_id
        url = f"https://api.themoviedb.org/3/movie/{id}/credits?api_key=0b9bf42f647ecf2055be8ac552db3a0d&language=ko-kr"
        character = requests.get(url).json()
        l = min(len(character['cast']), 5)
        for i in range(l):
            actorid = character['cast'][i]['id']
            if not Character.objects.filter(actor_id = actorid, movie_id=id).exists() :
                act = Actor.objects.get(actor_id=actorid) 
                char = Character()
                char.movie = movie
                char.actor = act
                char.charactername = character['cast'][i]['character']
                char.save()

# 중복 검사 함수
def find():
    pass
    # for i in range(1,9987):
    #     movie = Movie.objects.get(pk=i)
    #     if len(Movie.objects.filter(movie_id = movie.movie_id)) > 1:
    #         print(movie.pk)
    # print('movie 끝')
    # for i in range(1, 21102):
    #     actor = Actor.objects.get(pk=i)
    #     if len(Actor.objects.filter(actor_id = actor.actor_id)) > 1:
    #         print(actor.pk)
    # print('actor 끝')
    # for i in range(1, 48401):
    #     character = Character.objects.get(pk=i)
    #     if len(character.objects.filter(movie_id = character.movie_id, actor_id = character.actor_id)) > 1:
    #         print(character.pk)
    # print('character 끝')
def change():
    for i in range(1, 21102):
        actor = get_object_or_404(Actor, id=i)
        if i == 75:
            print(actor.profile_path)
        if actor.profile_path:
            pass
        else:
            actor.profile_path = 'defaultProfile.png'
            actor.save()
 

if __name__ == '__main__':
    # movie()
    # actor()
#    character()
#     find()
    change()
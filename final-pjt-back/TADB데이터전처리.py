import pandas as pd
import requests

# movies = []
# url = "https://api.themoviedb.org/3/movie/popular?api_key=0b9bf42f647ecf2055be8ac552db3a0d&language=ko-kr&page="

# for i in range(1, 26):
#     URL = url+str(i)
#     data = requests.get(URL).json()['results']
#     for j in range(20) :
#         movies.append(data[j])
# df = pd.DataFrame(movies)
# df.drop(['adult', 'backdrop_path', 'original_language', 'original_title', 'video'], axis=1, inplace = True)
# print(df.head())
# df.to_csv('C:/Users/Com/Desktop/movies_500.csv', index=False, encoding='utf-8-sig')
# print(df.info())

# df = pd.read_csv('C:/Users/Com/Desktop/movies_500.csv')
# i=0
# xx = []
# yy = []
# zz = []
# for id in df['id'].values :
#     detail_url = f'https://api.themoviedb.org/3/movie/{id}?api_key=0b9bf42f647ecf2055be8ac552db3a0d&language=ko-kr'
#     data = requests.get(detail_url).json()
#     # print(data)
#     g = ''
#     for genre in data['genres'] :
#         g += genre['name'] + ' '
#     xx.append(g)
#     yy.append(data['tagline'])
#     zz.append(data['runtime'])
#     print(i)
#     i += 1

# print(xx, yy, zz)   
# df['genre'] = xx
# df['tagline'] = yy
# df['runtime'] = zz
# print(df.head())

# df_222 = df
# df_222.to_csv('C:/Users/Com/Desktop/movies_500_add_detail.csv', index=False, encoding='utf-8-sig')

# df = pd.read_csv('C:/Users/Com/Desktop/movies_500_add_detail.csv')
# keys = []
# for id in df['id'].values :
#     video_url = f'https://api.themoviedb.org/3/movie/{id}/videos?api_key=0b9bf42f647ecf2055be8ac552db3a0d&language=ko-kr'
#     data = requests.get(video_url).json()['results']
#     if len(data) >= 1 :
#         keys.append(data[0]['key'])
#     else :
#         keys.append('')
#     print(len(keys))
# df['trailer_key'] = keys

# df.drop(['genre_ids'], axis=1, inplace = True)
# df.to_csv('C:/Users/Com/Desktop/movies_500_add_detail_add_trailer_key.csv', index=False, encoding='utf-8-sig')



# df = pd.read_csv('C:/Users/Com/Desktop/movies_500_add_detail_add_trailer_key.csv')

# characters = []
# movie_id = []
# i = 0
# for id in df['id'].values :
#     url = f"https://api.themoviedb.org/3/movie/{id}/credits?api_key=0b9bf42f647ecf2055be8ac552db3a0d&language=ko-kr"
#     data = requests.get(url).json()['cast'][:5]
#     for character in data :
#         if character['known_for_department'] == "Acting" :
#             characters.append(character)
#             movie_id.append(id)
#     print(i)
#     i += 1

# df2 = pd.DataFrame(characters)
# df2['movie_id'] = movie_id
# df2.drop(['adult', 'gender', 'known_for_department', 'name', 'original_name' ,'popularity', 'profile_path', 'cast_id', 'credit_id', 'order'], axis=1, inplace = True)
# df2.rename(columns={'id' :'actor_id', 'character' : 'charactername'}, inplace=True)

# df2.to_csv('C:/Users/Com/Desktop/characters_500_new.csv', index=False, encoding='utf-8-sig')

# df = pd.read_csv('C:/Users/Com/Desktop/actors_500.csv')

# actors = []
# i = 0
# for id in df['actor_id'].values :
#     url = f"https://api.themoviedb.org/3/person/{id}?api_key=0b9bf42f647ecf2055be8ac552db3a0d&language=ko-kr"
#     data = requests.get(url).json()
#     actors.append(data)
#     print(i)
#     i += 1

# df2 = pd.DataFrame(actors)
# df2.to_csv('C:/Users/Com/Desktop/actors_500.csv', index=False, encoding='utf-8-sig')

# df = pd.read_csv('C:/Users/Com/Desktop/actors_500.csv')
# df.drop(['adult', 'also_known_as', 'biography', 'gender', 'homepage' , 'imdb_id', 'known_for_department', 'popularity'], axis=1, inplace = True)
# df['overview'] = ''
# df['score'] = 0
# df.rename(columns={'id' :'actor_id'}, inplace=True)
# df['id'] = list(range(1, len(df)+1))
# df = df[['id','birthday', 'deathday', 'actor_id', 'name', 'place_of_birth', 'profile_path', 'overview', 'score']]
# df.to_csv('C:/Users/Com/Desktop/actors_500_real_new_edit.csv', index=False, encoding='utf-8-sig')






# df2 = pd.read_csv('C:/Users/Com/Desktop/movies_500_add_detail.csv')
# df = pd.read_csv('C:/Users/Com/Desktop/movies_500_add_detail_add_trailer_key.csv')
# df['id'] = list(range(1, len(df)+1))
# df['movie_id'] = df2['id'].values
# df = df[['id', 'movie_id', 'overview', 'popularity', 'poster_path', 'release_date', 'title', 'vote_average', 'vote_count', 'genre', 'tagline', 'runtime', 'trailer_key']]
# print(df.head())
# df.to_csv('C:/Users/Com/Desktop/movies_500_add_detail_add_trailer_key.csv', index=False, encoding='utf-8-sig')


# df = pd.read_csv('C:/Users/Com/Desktop/characters_500_new_id.csv')
# df['id'] = list(range(1, len(df)+1))
# df['score'] = 0
# df = df[['id', 'charactername', 'score', 'actor_id', 'movie_id']]

# df.to_csv('C:/Users/Com/Desktop/characters_500_new_id.csv', index=False, encoding='utf-8-sig')


df = pd.read_csv('C:/Users/Com/Desktop/actors_500_real_new_edit.csv')

df.drop(['id'], axis=1, inplace = True)

df.drop_duplicates(inplace=True)

df['id'] = list(range(1, len(df)+1))

df = df[['id','birthday', 'deathday', 'actor_id', 'name', 'place_of_birth', 'profile_path', 'overview', 'score']]

df.to_csv('C:/Users/Com/Desktop/actors_500_no_dup.csv', index=False, encoding='utf-8-sig')

# df.drop_duplicates(['actor_id'])
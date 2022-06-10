from rest_framework import serializers
from .models import Actor, Character, Comment
from movies.models import Movie
from django.contrib.auth import get_user_model

class ActorSerializer(serializers.ModelSerializer):

    class MovieForActorSerializer(serializers.ModelSerializer):
        class Meta :
            model = Movie
            fields = ('title',)

    class CharacterForActorSerializer(serializers.ModelSerializer) :
        class Meta :
            model = Character
            fields = ('charactername', 'score',)

    movie = MovieForActorSerializer(many=True, read_only=True)
    character_set = CharacterForActorSerializer(many=True, read_only=True)

    class Meta :
        model = Actor
        fields = '__all__'

class CharacterSerializer(serializers.ModelSerializer):
    class CharacterMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk', 'title', 'movie_id', 'vote_average', 'poster_path') 
    class CharacterActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('pk', 'actor_id', 'name', 'profile_path', 'score')
    actor = CharacterActorSerializer(read_only=True)
    movie = CharacterMovieSerializer(read_only=True)
    class Meta:
        model = Character
        fields = '__all__'
               

class ActorDetailSerializer(serializers.ModelSerializer):
    class LikedActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')
    class ActorCharacterSerializer(serializers.ModelSerializer):
        class Meta:
            model = Character
            fields = '__all__'

    class ActorMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk', 'title', 'movie_id', 'vote_average', 'poster_path')
    
    like_users = LikedActorSerializer(many=True, read_only=True)
    character_set = ActorCharacterSerializer(many=True, read_only=True)
    movie = ActorMovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('character', 'user')


# 정보를 가져가는 용도
class CommentsSerializer(serializers.ModelSerializer):
    class CommentsUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username')
    user = CommentsUserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class ActorLikeSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')
    like_users = UserSerializer(many=True, read_only= True)
    class Meta:
        model = Actor
        fields = '__all__'



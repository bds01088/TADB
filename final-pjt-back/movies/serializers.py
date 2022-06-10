from rest_framework import serializers
from .models import Movie
from actors.models import Actor

class MovieSerializer(serializers.ModelSerializer):
    
    class ActorForMovieSerializer(serializers.ModelSerializer):
        class Meta :
            model = Actor
            fields = ('name',)

    actor_set = ActorForMovieSerializer(many=True, read_only=True)
    
    class Meta :
        model = Movie
        fields = '__all__'

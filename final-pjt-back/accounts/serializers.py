from rest_framework import serializers
from django.contrib.auth import get_user_model
from actors.models import Actor, Comment, Character

class UserProfileSerializer(serializers.ModelSerializer):
    class UserActorsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('pk', 'name','profile_path', 'score')
    class UserCommentsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'
    actors = UserActorsSerializer(many=True, read_only=True)
    comment_set = UserCommentsSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'date_joined', 'image', 'overview' , 'actors', 'comment_set')
    
class UserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('actors',)
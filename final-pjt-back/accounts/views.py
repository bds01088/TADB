from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from actors.models import Actor, Character
from movies.models import Movie
from .serializers import UserProfileSerializer, UserLikeSerializer 
from django.contrib.auth import get_user_model
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like(request,username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserLikeSerializer(user)
    return Response(serializer.data)



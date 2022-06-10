from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Actor, Character, Comment
from movies.models import Movie
from .serializers import ActorSerializer, ActorDetailSerializer, CommentSerializer, CommentsSerializer, ActorLikeSerializer, CharacterSerializer
from rest_framework import status

from django.db.models import Sum

from actors import serializers
# Create your views here.


@api_view(['GET'])
def actors(request) :
    actors = Actor.objects.all().order_by('-score')
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def popular(request):
    actors = Actor.objects.all().order_by('-score')[:20]
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pick(request, actorPK):
    characters = Character.objects.filter(actor_id=actorPK).order_by('-score')[:3]
    serializer = CharacterSerializer(characters, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def actor(request, actorPK):
    actor = get_object_or_404(Actor, pk=actorPK)
    serializer = ActorDetailSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comments(request, actorPK):
    actor = get_object_or_404(Actor, pk=actorPK)
    characters = Character.objects.filter(actor_id=actor.pk)
    cha_id = []
    for cha in characters:
        cha_id += [cha.id]
    comments = Comment.objects.filter(character_id__in= cha_id).order_by('-score')
    serializer = CommentsSerializer(comments, many=True)
    return Response(serializer.data)

# 변수 정리
# comment 해당 댓글 객체, character 해당 등장인물 객체, actor 해당 배우 객체, serializer 입력 데이터 값 객체
# character.comments.all().count() 해당 배역의 댓글 수
# actor.character_set.all().count() 해당 인물의 배역 수
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, characterPK):
    character = get_object_or_404(Character, pk=characterPK)
    # 평점 재계산
    actor = get_object_or_404(Actor, pk = character.actor_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, character=character)
        character.score = character.comments.aggregate(Sum('score'))['score__sum']/character.comments.all().count()
        character.save()
        actor.score = actor.character_set.aggregate(Sum('score'))['score__sum']/actor.movie.all().count()
        actor.save()
        return Response(status=status.HTTP_201_CREATED)

# 변수 정리
# comment 해당 댓글 객체, character 해당 등장인물 객체, actor 해당 배우 객체, serializer 입력 데이터 값 객체
# character.comments.all().count() 해당 배역의 댓글 수
# actor.character_set.all().count() 해당 인물의 배역 수
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment(request, commentPK):
    comment = get_object_or_404(Comment, pk=commentPK)
    character = get_object_or_404(Character, pk=comment.character_id)
    actor = get_object_or_404(Actor, pk=character.actor_id)
    serializer = CommentSerializer(instance=comment, data=request.data)
    print()
    if request.user == comment.user:
        if request.method == 'PUT':
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                character.score = character.comments.aggregate(Sum('score'))['score__sum']/character.comments.all().count()
                character.save()
                actor.score = actor.character_set.aggregate(Sum('score'))['score__sum']/actor.movie.all().count()
                actor.save()
            return Response(status=status.HTTP_201_CREATED)
        elif request.method == 'DELETE':
            comment.delete()
            # character = get_object_or_404(Character, pk=comment.character_id)
            if character.comments.all().count():
                character.score = character.comments.aggregate(Sum('score'))['score__sum']/character.comments.all().count()
            else :
                character.score = 0
            character.save()
            actor.score = actor.character_set.aggregate(Sum('score'))['score__sum']/actor.movie.all().count()
            actor.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_actor(request, actorPK):
    actor = get_object_or_404(Actor, pk=actorPK)
    user = request.user
    if actor.like_users.filter(pk=user.pk).exists():
        actor.like_users.remove(user)
        serializer = ActorLikeSerializer(actor)
        return Response(serializer.data)
    else:
        actor.like_users.add(user)
        serializer = ActorLikeSerializer(actor)
        return Response(serializer.data)
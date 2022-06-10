from django.urls import path
from . import views

app_name = 'actors'

urlpatterns = [
    path('', views.actors, name = 'actors'),
    path('home/', views.popular,),
    path('<int:actorPK>/pick/', views.pick),
    path('<int:actorPK>/', views.actor),
    path('<int:actorPK>/comment/', views.comments),
    path('<int:characterPK>/comments/', views.comment_create),
    path('comment/<int:commentPK>/', views.comment),
    path('<int:actorPK>/like/', views.like_actor),
]

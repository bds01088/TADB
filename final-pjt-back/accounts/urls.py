from django.urls import path
from . import views
urlpatterns = [
    path('<username>/like/', views.like),
    path('<username>/', views.profile),
]
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/Schedule', views.Schedule, name='Schedule'),
    path('members/Resources', views.Resources, name='Resources'),
    path('members/Budget', views.Budget, name='Budget'),
]
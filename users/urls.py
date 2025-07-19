from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name ='users'),
    path('user_details/<int:id>/', views.details, name='details'),
]
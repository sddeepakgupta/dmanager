from django.urls import path
from taskmanager import views

urlpatterns = [
    path('', views.signup, name='signup'),
]
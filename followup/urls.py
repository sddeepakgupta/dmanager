from django.urls import path
from followup import views

urlpatterns = [
    path('', views.index, name='home'),
]
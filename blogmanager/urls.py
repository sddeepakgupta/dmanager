
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blogmanager import views

urlpatterns = [
    path('tutorials/', views.tutorialList.as_view()),
    path('tutorials/<int:pk>/', views.tutorialDetail.as_view()),
]
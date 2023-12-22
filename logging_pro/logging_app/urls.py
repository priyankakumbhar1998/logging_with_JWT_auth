from django.urls import path
from .views import StudentAPI, StudentDetailsAPI

urlpatterns = [
    path('student/', StudentAPI.as_view()),
    path('student/<int:pk>/', StudentDetailsAPI.as_view()),
]
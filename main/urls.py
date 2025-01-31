from django.urls import path
from .views import *

urlpatterns = [
    path('task/create', TaskListApi.as_view()),
    path('task/crud<int:pk>',Taskapi.as_view()),
]

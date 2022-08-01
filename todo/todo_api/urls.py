from django.conf.urls import url
from django.urls import re_path as path, include
from .views import (
    TodoListApiView,
    TodoDetailApiView
)

urlpatterns = [
    path('api', TodoListApiView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path ("todos/", views.todos, name="Todos"),
    path ('createtask/', views.create_task, name='crttask')
]
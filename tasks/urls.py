# tasks/urls.py

from django.urls import path
from . import views

# This url configuration is designed to work with the event-driven views.
# Note that there is no 'task-detail' URL, as it's no longer needed.
# The task list is updated via the 'taskAdded' event triggered from the backend.

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/create/', views.task_create, name='task-create'),
    path('tasks/<int:pk>/update/', views.task_update, name='task-update'),
    path('tasks/<int:pk>/toggle/', views.task_toggle, name='task-toggle'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task-delete'),
]

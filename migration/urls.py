from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.addTask, name='add_task'),
    path('done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]

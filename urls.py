from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('add/', views.add_song, name='add_song'),
    path('edit/<int:pk>/', views.edit_song, name='edit_song'),
    path('delete/<int:pk>/', views.delete_song, name='delete_song'),
]

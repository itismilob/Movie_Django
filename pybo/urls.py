from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),    # edit to 'index/'
    path('single/', views.single_view),
    path('gallery/', views.gallery_view),
    path('list/', views.list_view),
    path('genre/', views.genre_view),
    path('add_movie/', views.add_movie_view),
]
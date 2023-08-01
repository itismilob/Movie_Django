from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),    # edit to 'index/'
    path('single/', views.single_view),
    path('gallery/', views.gallery_view),
    path('list/', views.list_view),
    path('genre/', views.genre_view),
    path('add_movie/', views.add_movie_view, name='add_movie'),
    path('add_movie/submit', views.add_movie_submit, name='add_movie_submit'),
]
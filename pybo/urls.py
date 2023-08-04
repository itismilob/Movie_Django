from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('index_view/', views.index_view, name='index_view'),
    path('single_view/', views.single_view, name='single_view'),
    path('gallery_view/', views.gallery_view, name='gallery_view'),
    path('list_view/', views.list_view, name='list_view'),
    path('add_movie_view/', views.add_movie_view, name='add_movie_view'),
    path('add_movie_submit', views.add_movie_submit, name='add_movie_submit'),
    path('specific/<int:movie_id>/', views.specific, name='specific'),
    path('tag/<str:tag_name>', views.tag, name='tag'),
]
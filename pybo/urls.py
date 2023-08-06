from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('specific/<int:movie_id>/', views.specific_view, name='specific_view'),
    path('single_view/', views.single_view, name='single_view'),
    path('gallery_view/', views.gallery_view, name='gallery_view'),
    path('list_view/', views.list_view, name='list_view'),
    path('list_tag/<str:tag_name>/', views.list_tag, name='list_tag'),
    path('list_order/', views.list_order, name='list_order'),

    path('add_movie_view/', views.add_movie_view, name='add_movie_view'),
    path('add_movie_submit/', views.add_movie_submit, name='add_movie_submit'),
    path('edit_movie_view/<int:movie_id>/', views.edit_movie_view, name='edit_movie_view'),
    path('edit_movie_submit/<int:movie_id>/', views.edit_movie_submit, name='edit_movie_submit'),
    path('delete_movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),

    path('search/', views.search, name='search'),
]
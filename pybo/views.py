from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie_info

# Create your views here.
def index(request):
    """
    main page
    :param request:
    :return:
    """
    movie_info = Movie_info.objects.order_by('-id')
    context = {'context': movie_info}
    return render(request, "base.html", context)

def single_view(request):
    """
    Single View page
    :return:
    """
    return render(request, "pybo/single_view.html")

def gallery_view(request):
    """
    Gallery View page
    :return:
    """
    return render(request, "pybo/gallery_view.html")

def list_view(request):
    """
    List View page
    :return:
    """
    return render(request, "pybo/list_view.html")

def genre_view(request):
    """
    Genre View page
    :return:
    """
    return render(request, "pybo/genre_view.html")

def add_movie_view(request):
    """
    Add Movie View page
    :return:
    """
    return render(request, "pybo/add_movie_view.html")

def add_movie(request):
    """
    Add Movie to db
    :param request:
    :return:
    """
    movie = Movie_info(title=request.POST.get('title'),
                       year=request.POST.get('year'),
                       poster=request.POST.get('poster'),
                       tags=request.POST.get('tags'))
    print(request.POST.get('title'),
          request.POST.get('year'),
          request.POST.get('poster'),
          request.POST.get('tags'))
    movie.save()
    return render(request, "pybo/add_movie_view.html")
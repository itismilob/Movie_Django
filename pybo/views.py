from django.shortcuts import render
from django.shortcuts import render
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
    return

def list_view(request):
    """
    List View page
    :return:
    """
    return

def genre_view(request):
    """
    Genre View page
    :return:
    """
    return

def add_movie_view(request):
    """
    Add Movie View page
    :return:
    """
    return
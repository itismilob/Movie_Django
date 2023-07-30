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
    return render(request, "base.html")

def single_view(request):
    """
    Single View page
    :return:
    """
    movie_info = Movie_info.objects.order_by('id')
    this_tags = []
    for i in movie_info:
        text = ""
        text_arr = []
        for t in i.tags:
            if t == ',':

                text_arr.append(text)
                text = ""
            else:
                text += t
        text_arr.append(text)
        this_tags.append(text_arr)

    print("!!! ", this_tags)

    moviessss = zip(movie_info, this_tags)

    context = {'movie_info': moviessss}
    return render(request, "pybo/single_view.html", context)

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
    this_title = request.POST.get('title')
    this_year = request.POST.get('year')
    this_poster = request.POST.get('poster')
    this_tags = request.POST.get('tags')

    movie = Movie_info(title=this_title, year=this_year, poster=this_poster, tags=this_tags)
    check_registered = Movie_info.objects.filter(title=this_title)

    print("!!! Input: ", this_title, this_year, this_poster, this_tags)
    print("!!! check: ", check_registered.count())

    if not check_registered.count():
        print("!!! add completed")
        movie.save()
    else:
        print("!!! this movie already registered")

    return render(request, "pybo/add_movie_view.html")
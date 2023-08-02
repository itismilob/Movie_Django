from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie_info, Movie_tags
from .forms import add_movie_Form


# functions
def to_list(obj):
    this_list = []
    value = ''
    for i in obj:
        if i == ',':
            this_list.append(value)
            value = ''
        else:
            value += i
    this_list.append(value)

    return this_list


# pybo
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
        this_tags.append(to_list(i.tags))

    cont = zip(movie_info, this_tags)
    context = {'movie_info': cont}
    return render(request, "pybo/single_view.html", context)


def gallery_view(request):
    """
    Gallery View page
    :return:
    """
    movie_info = Movie_info.objects.order_by('id')
    this_tags = []
    for i in movie_info:
        this_tags.append(to_list(i.tags))

    cont = zip(movie_info, this_tags)
    context = {'movie_info': cont}
    return render(request, "pybo/gallery_view.html", context)


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


# @csrf_exempt
def add_movie_view(request):
    """
    Add Movie View page
    :return: add_movie_view
    """
    movie_tags = Movie_tags.objects.order_by('tag')
    context = {'movie_tags': movie_tags}
    return render(request, "pybo/add_movie_view.html", context=context)


def add_movie_submit(request):
    """
    Add Movie to DB
    :param request:
    :return: add_movie_view
    """

    if request.method == 'POST':
        form = add_movie_Form(request.POST, request.FILES)
        post = request.POST
        file = request.FILES
        print("!!! ", post, file)
        if form.is_valid():
            form.save()
            return redirect('pybo:add_movie')
    else:
        form = add_movie_Form()

    movie_tags = Movie_tags.objects.order_by('tag')
    context = {'movie_tags': movie_tags, 'form': form}

    return render(request, "pybo/add_movie_view.html", context=context)


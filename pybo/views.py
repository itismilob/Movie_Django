from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie_info, Movie_tags
from .forms import add_movie_Form, edit_movie_Form
from django.db.models import Q


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
    :param request:
    :return:
    """
    term = request.GET.get('term', '')
    movie_list = Movie_info.objects.order_by('-title')
    this_tags = []

    if term:
        movie_list = movie_list.filter(
            Q(title__icontains=term)|
            Q(tags__icontains=term)
        ).distinct()
        for movie in movie_list:
            this_tags.append(to_list(movie.tags))

    else:
        return render(request, "pybo/list_view.html")

    cont = zip(movie_list, this_tags)
    context = {'movie_info':cont, 'term':term}
    return render(request, "pybo/list_view.html", context)

def index_view(request):
    """
    main index view
    :param request:
    :return:
    """
    return render(request, "index_view.html")

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
    movie_info = Movie_info.objects.order_by('title')
    this_tags = []
    for i in movie_info:
        this_tags.append(to_list(i.tags))

    cont = zip(movie_info, this_tags)
    context = {'movie_info': cont}
    return render(request, "pybo/list_view.html", context)


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
        if form.is_valid():
            form.save()
            return redirect('pybo:add_movie_view')
    else:
        form = add_movie_Form()

    movie_tags = Movie_tags.objects.order_by('tag')
    context = {'movie_tags': movie_tags, 'form': form}

    return render(request, "pybo/add_movie_view.html", context=context)

def edit_movie_view(request, movie_id):

    movie_info = Movie_info.objects.get(id=movie_id)
    this_tags = to_list(movie_info.tags)
    movie_tags = Movie_tags.objects.exclude(tag__in=this_tags).order_by('tag')

    context = {'movie_info': movie_info, 'this_tags': this_tags, 'movie_tags': movie_tags}
    return render(request, "pybo/edit_movie_view.html", context=context)

def edit_movie_submit(request, movie_id):
    movie_info = Movie_info.objects.get(id=movie_id)
    if request.method == 'POST':
        form = edit_movie_Form(request.POST, request.FILES)
        if form.is_valid():
            movie_info.title = form['title'].value()
            movie_info.year = form['year'].value()
            movie_info.tags = form['tags'].value()
            movie_info.rating = form['rating'].value()
            movie_info.link = form['link'].value()

            print(form['poster'].value())
            if form['poster'].value():
                movie_info.poster = form['poster'].value()

            movie_info.save()

        this_tags = movie_info.tags.split(',')
        context = {'movie_info': movie_info, 'tags': this_tags}
        return render(request, "pybo/specific_view.html", context=context)

    return render(request, "pybo/single_view.html")

def specific(request, movie_id):
    movie_info = Movie_info.objects.get(id=movie_id)
    this_tags = to_list(movie_info.tags)

    context = {'movie_info': movie_info, 'tags': this_tags}
    return render(request, "pybo/specific_view.html", context=context)

def search(request, text):
    movie_info = Movie_info.objects.filter(title=text)
    this_tags = to_list(movie_info.tags)

    context = {'movie_info': movie_info, 'tags': this_tags}
    return render(request, "pybo/specific_view.html", context=context)

def tag(request, tag_name):

    movie_list = Movie_info.objects.order_by('-title')
    this_tags = []

    movie_list = movie_list.filter(
        Q(tags__icontains=tag_name)
    ).distinct()
    for movie in movie_list:
        this_tags.append(to_list(movie.tags))


    cont = zip(movie_list, this_tags)
    context = {'movie_info':cont}
    return render(request, "pybo/list_view.html", context)

def order(request):

    select = request.GET.get('select', '')
    id_list = request.GET.get('id_list', '').split(',')
    movie_list = []

    if(select == 'Title'):
        movie_list = Movie_info.objects.order_by('title').filter(id__in=id_list)
    elif(select == 'Year'):
        movie_list = Movie_info.objects.order_by('-year').filter(id__in=id_list)
    elif(select == 'Rating'):
        movie_list = Movie_info.objects.order_by('-rating').filter(id__in=id_list)

    this_tags = []
    for movie in movie_list:
        this_tags.append(to_list(movie.tags))

    cont = zip(movie_list, this_tags)
    context = {'movie_info':cont, 'select':select}
    return render(request, "pybo/list_view.html", context)


def delete_movie(request, movie_id):
    movie = Movie_info.objects.get(id=movie_id)
    movie.delete()

    movie_info = Movie_info.objects.order_by('title')
    this_tags = []
    for i in movie_info:
        this_tags.append(to_list(i.tags))

    cont = zip(movie_info, this_tags)
    context = {'movie_info': cont}
    return render(request, "pybo/list_view.html", context)
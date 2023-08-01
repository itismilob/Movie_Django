from django.contrib import admin
from .models import Movie_info, Movie_tags

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Movie_info, MovieAdmin)
admin.site.register(Movie_tags, MovieAdmin)

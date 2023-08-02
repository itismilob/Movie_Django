from django.db import models

# Create your models here.
class Movie_info(models.Model):
    title = models.CharField(max_length=50, )
    year = models.IntegerField()
    poster = models.ImageField(upload_to='', height_field=None, width_field=None)
    tags = models.TextField()
    rating = models.IntegerField()
    link = models.URLField()

    def __str__(self):
        return "Movie Title: " + self.title

class Movie_tags(models.Model):
    tag = models.CharField(max_length=50)
    def __str__(self):
        return self.tag
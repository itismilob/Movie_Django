from django.db import models

# Create your models here.
class Movie_info(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    poster = models.ImageField()
    tags = models.TextField()
    def __str__(self):
        return self.title

class Movie_tags(models.Model):
    tag = models.CharField(max_length=50)
    def __str__(self):
        return self.tag
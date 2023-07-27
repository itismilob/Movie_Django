from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Movie_info(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    poster = models.TextField()
    tags = models.TextField()

    def __str__(self):
        return self.title

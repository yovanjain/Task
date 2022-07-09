from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genres(models.Model):
    title =models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=100, unique= True)
    release_year = models.IntegerField()
    rating = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    genres = models.ManyToManyField(Genres)
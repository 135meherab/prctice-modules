from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=80)
    released_date = models.DateField()
    ratings = (
        ('1', 'ONE'),
        ('2', 'TWO'),
        ('3', 'THREE'),
        ('4', 'FOUR'),
        ('5', 'FIVE'),
    )
    rating = models.CharField(max_length=10, choices=ratings)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.album_name} by {self.musician.first_name} {self.musician.last_name}'
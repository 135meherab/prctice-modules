from django.db import models
from Musician.models import Musician
# Create your models here.
class Album(models.Model):
    album_Name = models.CharField(max_length=30)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, default=None)
    release_date = models.DateField()
    rate = [
        ('one', 1),
        ('two', 2),
        ('three', 3),
        ('four', 4),
        ('five', 5),
    ]
    rate_album = models.CharField(max_length=10, choices=rate, default=None)
    def __str__(self):
        return self.album_Name
from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    instuments = [
        ('guitar', 'Guitar'),
        ('drum', 'Drum'),
        ('banjo', 'Banjo'),
        ('marimba', 'Marimba'),
        ('harmonica', 'Harmonica')
    ]
    instument = models.CharField(max_length=10, choices=instuments, default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
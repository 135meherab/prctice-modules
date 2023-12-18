from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 15)
    choice = (
        ('guiter', 'Guiter'),
        ('drums', 'Drums'),
        ('violin', 'Violin'),
        ('banjo', 'Banjo'),
    )
    instument = models.CharField(max_length=10, choices=choice)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
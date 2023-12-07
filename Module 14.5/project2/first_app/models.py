from django.db import models

# Create your models here.
class StudentModel(models.Model):
    id = models.AutoField(primary_key=True)
    roll = models.IntegerField()
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    social = models.URLField(blank=True)
    form = models.FileField()
    img = models.ImageField()
    address = models.TextField()
    new = models.BooleanField(default=False)
    fee = models.DecimalField(max_digits=3, decimal_places=2)
    birth_date = models.DateField()
    birth_time = models.TimeField()
    Weight = models.FloatField()
from django.shortcuts import render
from Album.models import Album
def home(request):
    data = Album.objects.all()
    print(data)
    return render(request, 'home.html',{"data": data})
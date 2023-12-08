from django.shortcuts import render, redirect
from . form import AlbumForm
from . models import Album

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('album_page')
    else:
        form = AlbumForm()
    return render(request, 'album.html', {'form': form})

def edit_album(request, id):
    album = Album.objects.get(pk=id)
    form = AlbumForm(instance=album)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'album.html', {'form': form})
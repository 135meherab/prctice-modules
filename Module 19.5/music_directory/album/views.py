from django.shortcuts import render
from . form import AlbumForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from . models import Album
from django.contrib.auth.mixins import LoginRequiredMixin

    

class create_album(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_page.html'
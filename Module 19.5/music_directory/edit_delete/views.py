from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from album.models import Album
from musician.models import Musician
from album.form import AlbumForm
from musician.form import MusicinaForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# @login_required(login_url='login_page')
class edit_album(LoginRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'edit_album.html'
    pk_url_kwarg = 'id'	
    success_url = reverse_lazy('home_page')

# @login_required(login_url='login_page')
class edit_musicain(LoginRequiredMixin, UpdateView):
    model = Musician
    form_class = MusicinaForm
    template_name = 'edit_musician.html'
    pk_url_kwarg = 'id'	
    success_url = reverse_lazy('home_page')

# @login_required(login_url='login_page')
class delete_album(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'delete_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home_page')
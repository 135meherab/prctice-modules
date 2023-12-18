from django.shortcuts import render
from . form import MusicinaForm
from . models import Musician
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

# Create your views here.

class create_musician(LoginRequiredMixin, CreateView):
    model = Musician
    form_class = MusicinaForm
    template_name='musician_page.html'
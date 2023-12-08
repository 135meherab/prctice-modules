from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_album, name='album_page'),
    path('edit_album/<int:id>', views.edit_album, name='edit_album')
]


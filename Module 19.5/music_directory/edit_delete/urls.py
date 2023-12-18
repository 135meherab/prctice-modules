from django.urls import path
from . import views

urlpatterns = [
    path('album_edit/<int:id>', views.edit_album.as_view(), name ='album_edit'),
    path('musician_edit/<int:id>', views.edit_musicain.as_view(), name ='musician_edit'),
    path('delete/<int:id>', views.delete_album.as_view(), name ='album_delete'),
]

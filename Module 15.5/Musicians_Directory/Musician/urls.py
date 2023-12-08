from django.urls import path
from . import views

urlpatterns = [
    path('',views.musician, name='musician_page'),
    path('edit_musician/<int:id>', views.edit_musician, name='edit_musician'),
    path('delete_musician/<int:id>', views.delete_musician, name='delete_musician')

]

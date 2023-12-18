from django.urls import path
from . import views
urlpatterns = [
    path('',views.create_musician.as_view(), name= 'musician_page')
]

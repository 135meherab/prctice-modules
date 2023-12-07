from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('login', views.login, name = 'login'),
    path('django_form', views.django_form, name = 'django_form'),
]
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register_page'),
    path('login/', views.login.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
]

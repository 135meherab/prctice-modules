from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

def register(request):
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')
    else:
        form = CreateUserForm()
    return render(request,'register.html',{'form': form})


class login(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('home_page')

    def form_valid(self, form):
        messages.success(self.request, 'logged in successfully')
        return super().form_valid(form)
    

    
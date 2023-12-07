from django.shortcuts import render
from . forms import contactform
# Create your views here.
def home(request):
    return render (request, 'home.html')

def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        rate = request.POST.get('select')
        return render (request, 'about.html', {'name': name, 'email': email, 'rate': rate})
    else:
        return render (request, 'about.html')

def login(request):
    return render(request, 'form.html')

def django_form(request):
    if request.method == 'POST':
        form = contactform(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['image']
            with open('./app/uploaded_file/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request, 'djangoform.html', {'form':form})
    else:
        form = contactform()
    return render(request, 'djangoform.html', {'form':form})
from django.shortcuts import render, redirect
from . form import MusicicanForm
from . models import Musician

# Create your views here.
def musician(request):
    if request.method == 'POST':
        form = MusicicanForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('musician_page')
    else:
        form = MusicicanForm()
    return render(request, 'musician.html', {'form': form})


def edit_musician(request, id):
    musician = Musician.objects.get(pk=id)
    form = MusicicanForm(instance=musician)
    if request.method == 'POST':
        form = MusicicanForm(request.POST, instance=musician)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
    return render(request, 'musician.html', {'form': form})

def delete_musician(request, id):
    Musician.objects.get(pk=id).delete()
    return redirect('home')

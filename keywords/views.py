from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewUrlForm  


def home(request):
    if request.method == 'POST':
        form = NewUrlForm(request.POST)
        if form.is_valid():
            input_url = form.save()
            return redirect('results')                  #TODO some clever redirection

    else:
        form = NewUrlForm()

    return render(request, 'home.html', {'form': form})


def results(request):
    return render(request, 'results.html')

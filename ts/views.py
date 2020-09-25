from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Url
from .services.paths import get_paths
from ts.forms import CitiesForm, UrlForm
from .services.shortener import Shortener


def index(request):
    if request.method == 'POST':
        form = CitiesForm(request.POST)
        dep_city = form.data['dep']
        dest_cities = request.POST.getlist('dest')
        print('dep_city is ' + str(dep_city))
        print('dest_cities ' + str(dest_cities))
        dest_cities.append(dep_city)
        my_set = set(dest_cities)
        paths = get_paths(dep_city, list(my_set))
        return render(request, 'ts/dests.html', {'paths': paths})
    else:
        form = CitiesForm()
    return render(request, 'ts/all_cities.html', {'form': form})


def url(request):
    a = ''
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = Shortener().issue_token()
            NewUrl.short_url = a
            NewUrl.save()
        else:
            form = UrlForm
            a = 'Invalid URL'
    else:
        form = UrlForm()
    return render(request, 'ts/url.html', {'form': form, 'a':a})


def get_url(request, token):
    long_url = Url.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)
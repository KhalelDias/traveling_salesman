from django.http import HttpResponse
from django.shortcuts import render
from .services.paths import get_paths
from ts.forms import CitiesForm


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

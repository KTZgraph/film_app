from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Film
from .forms import FilmForm

def all_films(request):
    all = Film.objects.all()
    return render(request, 'films.html', {"films":all})


def new_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_films)

    return render(request, 'film_form.html', {'form': form})


def edit_film(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(all_films)

    return render(request, 'film_form.html', {'form': form})


def delete_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(all_films)

    return render(request, 'confirm_form.html', {'film': film})
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Film, AdditionalInfo, Rating, Actor
from .forms import FilmForm, AdditionalInfoForm, RatingForm


def all_films(request):
    all = Film.objects.all()
    return render(request, 'films.html', {"films":all})

@login_required
def new_film(request):
    form_film = FilmForm(request.POST or None, request.FILES or None)
    additional_form= AdditionalInfoForm(request.POST or None)

    if all((form_film.is_valid(), additional_form.is_valid())):
        film = form_film.save(commit=False) # jeszcze nie zaaplikowane do bazy
        additional_info = additional_form.save()
        film.additional = additional_info
        film.save()

        return redirect(all_films)

    return render(request, 'film_form.html', {'form': form_film, 'additional_form': additional_form, 'is_new': True})


@login_required
def edit_film(request, id):
    film = get_object_or_404(Film, pk=id)
    ratings = Rating.objects.filter(film=film)
    actors = film.actors.all()

    try:
        additional_info = AdditionalInfo.objects.get(film=film.id) #jak film jest to mamy id
    except AdditionalInfo.DoesNotExist:
        additional_info = None

    form = FilmForm(request.POST or None, request.FILES or None, instance=film)
    additional_form = AdditionalInfoForm(request.POST or None, instance=additional_info)
    rating_form = RatingForm(request.POST or None)

    if request.method == 'POST':
        if 'stars' in request.POST:
            rating = rating_form.save(commit=False)
            rating.film = film
            rating.save()

    if all((form.is_valid(), additional_form.is_valid())):
        film = form.save(commit=False)
        additional = additional_form.save()
        film.additional = additional
        film.save()

        return redirect(all_films)

    return render(request, 'film_form.html', {
        'form': form,
        'additional_form': additional_form,
        'ratings': ratings,
        'rating_form' : rating_form,
        'actors': actors,
        'is_new': False})

@login_required
def delete_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(all_films)

    return render(request, 'confirm_form.html', {'film': film})
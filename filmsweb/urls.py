from django.urls import path
from filmsweb.views import all_films, new_film, edit_film, delete_film

urlpatterns = [
    path('all/', all_films, name="all_films"),
    path('new/', new_film, name="new_film"),
    path('edit/<int:id>/', edit_film, name="edit_film"),
    path('delete/<int:id>/', delete_film, name="delete_film"),
]

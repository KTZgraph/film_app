from django.db import models
# https://docs.djangoproject.com/en/3.0/topics/db/examples/

class AdditionalInfo(models.Model):
    FILM_TYPE = { # nie trzeba w bazie przechowywac calego duzego stringu
        (0, 'Inny'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
        (4, 'Dramat')
    }

    duration = models.PositiveSmallIntegerField(default=0)
    film_type = models.PositiveSmallIntegerField(default=0, choices=FILM_TYPE)


class Film(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default="")
    premiere = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)
    additional = models.OneToOneField(AdditionalInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return f'{self.title} ({self.year})'

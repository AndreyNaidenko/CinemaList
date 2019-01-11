from django.db import models


class Cinema(models.Model):
    name = models.CharField(max_length=50, blank=True)
    year = models.IntegerField(blank=True)
    rating = models.DecimalField(max_digits=10, decimal_places=6, blank=True)


class Actor(models.Model):
    cinema_id = models.ForeignKey(
        'Cinema',
        on_delete=models.CASCADE,
        blank=True
    )
    name = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(blank=True)


class Genre(models.Model):
    cinema_id = models.ForeignKey(
        'Cinema',
        on_delete=models.CASCADE,
        blank=True
    )
    name = models.CharField(max_length=30, blank=True)

from django.db import models


class Pokemon(models.Model):
    text = models.CharField(max_length=200)
    photo_of_pokemon = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.text}'


class PokemonEntity(models.Model):
    Lat = models.FloatField(null=True)
    Lon = models.FloatField(null=True)

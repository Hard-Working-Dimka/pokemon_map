from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    photo_of_pokemon = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class PokemonEntity(models.Model):
    name = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=False, blank=False)
    Lat = models.FloatField(null=True)
    Lon = models.FloatField(null=True)

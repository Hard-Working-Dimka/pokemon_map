from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    photo_of_pokemon = models.ImageField(blank=True, null=True)
    appeared_at = models.DateTimeField(blank=True, null=True, default=None)
    disappeared_at = models.DateTimeField(blank=True, null=True, default=None)
    level = models.IntegerField(null=True)
    health = models.IntegerField(null=True)
    strength = models.IntegerField(null=True)
    defence = models.IntegerField(null=True)
    stamina = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.name}'


class PokemonEntity(models.Model):
    name = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=False, blank=False)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)

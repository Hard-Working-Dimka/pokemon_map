from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, null=True)
    title_en = models.CharField(max_length=200, null=True)
    title_jp = models.CharField(max_length=200, null=True)
    photo_of_pokemon = models.ImageField(blank=True, null=True)
    appeared_at = models.DateTimeField(blank=True, null=True, default=None)
    disappeared_at = models.DateTimeField(blank=True, null=True, default=None)
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    evolution = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title_ru}'


class PokemonEntity(models.Model):
    title_ru = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=False, blank=False,
                                 related_name='pokemon_entities')
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)

    def __str__(self):
        return f'{self.title_ru}'

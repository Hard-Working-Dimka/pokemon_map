from django.db import models


class Pokemon(models.Model):
    name_of_pokemon_ru = models.CharField(max_length=200, null=False, blank=False, verbose_name='Имя на русском')
    name_of_pokemon_en = models.CharField(max_length=200, blank=True, verbose_name='Имя на английском')
    name_of_pokemon_jp = models.CharField(max_length=200, blank=True, verbose_name='Имя на японском')
    photo_of_pokemon = models.ImageField(blank=True, null=True, upload_to='photos_of_pokemons/',
                                         verbose_name='Фотография')
    description = models.TextField(blank=True, verbose_name='Описание')
    previous_evolution = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                                           related_name='next_evolutions', verbose_name='Из кого эволюционировал')

    def __str__(self):
        return f'{self.name_of_pokemon_ru}'

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'


class PokemonEntity(models.Model):
    title_ru = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=False, blank=False,
                                 related_name='pokemon_entities', verbose_name='Имя на русском')
    lat = models.FloatField(null=False, blank=False, verbose_name='Широта')
    lon = models.FloatField(null=False, blank=False, verbose_name='Долгота')
    appeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Появится')
    disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Исчезнет')
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, blank=True, verbose_name='Атака')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')

    def __str__(self):
        return f'{self.title_ru}'

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

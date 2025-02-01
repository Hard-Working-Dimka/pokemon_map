# Generated by Django 3.1.14 on 2025-02-01 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=200, verbose_name='Имя на русском')),
                ('title_en', models.CharField(blank=True, max_length=200, verbose_name='Имя на английском')),
                ('title_jp', models.CharField(blank=True, max_length=200, verbose_name='Имя на японском')),
                ('photo_of_pokemon', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('evolution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_evolutions', to='pokemon_entities.pokemon', verbose_name='Из кого эволюционировал')),
            ],
            options={
                'verbose_name': 'Покемон',
                'verbose_name_plural': 'Покемоны',
            },
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lon', models.FloatField(verbose_name='Долгота')),
                ('appeared_at', models.DateTimeField(verbose_name='Появится')),
                ('disappeared_at', models.DateTimeField(verbose_name='Исчезнет')),
                ('level', models.IntegerField(blank=True, null=True, verbose_name='Уровень')),
                ('health', models.IntegerField(blank=True, null=True, verbose_name='Здоровье')),
                ('strength', models.IntegerField(blank=True, null=True, verbose_name='Атака')),
                ('defence', models.IntegerField(blank=True, null=True, verbose_name='Защита')),
                ('stamina', models.IntegerField(blank=True, null=True, verbose_name='Выносливость')),
                ('title_ru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_entities', to='pokemon_entities.pokemon', verbose_name='Имя на русском')),
            ],
            options={
                'verbose_name': 'Местоположение',
                'verbose_name_plural': 'Местоположения',
            },
        ),
    ]

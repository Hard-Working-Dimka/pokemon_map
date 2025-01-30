import folium

from django.http import HttpResponseNotFound
from django.shortcuts import render
from pokemon_entities.models import Pokemon, PokemonEntity
from django.utils.timezone import localtime

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons_entity = PokemonEntity.objects.filter(disappeared_at__gte=localtime(), appeared_at__lte=localtime())
    pokemons = Pokemon.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entity:
        img_url = get_img_url(pokemon_entity.title_ru.photo_of_pokemon, request)
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            img_url,
        )

    pokemons_on_page = []
    for pokemon in pokemons:
        img_url = get_img_url(pokemon.photo_of_pokemon, request)
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': img_url,
            'title_ru': pokemon.title_ru,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден, возможно, он скоро появится!</h1>')
    img_url = get_img_url(pokemon.photo_of_pokemon, request)

    pokemon_info = {
        "pokemon_id": pokemon.id,
        "title_ru": pokemon.title_ru,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "description": pokemon.description,
        "img_url": img_url,
    }
    if pokemon.evolution:
        pokemon_info["previous_evolution"] = {
            "title_ru": pokemon.evolution.title_ru,
            "pokemon_id": pokemon.evolution.id,
            "img_url": img_url,
        }
    pokemon_next_evolutions = pokemon.next_evolutions.all()
    for pokemon_evolution in pokemon_next_evolutions:
        img_url = get_img_url(pokemon_evolution.photo_of_pokemon, request)
        pokemon_info["next_evolution"] = {
            "title_ru": pokemon_evolution.title_ru,
            "pokemon_id": pokemon_evolution.id,
            "img_url": img_url,
        }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    active_pokemons = pokemon.pokemon_entities.filter(disappeared_at__gte=localtime(),
                                                      appeared_at__lte=localtime())
    for pokemon_entity in active_pokemons:
        img_url = get_img_url(pokemon_entity.title_ru.photo_of_pokemon, request)
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            img_url,
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_info
    })


def get_img_url(photo, request):
    if photo:
        return request.build_absolute_uri(f'/media/{photo}')
    else:
        return DEFAULT_IMAGE_URL

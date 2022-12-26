from django.shortcuts import render
from datetime import date


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [{'id': '1', 'title': 'Miojo', 'name': 'Joao', 'data': date.today(), 'url': 'https://picsum.photos/seed/picsum/650/300'}, {'title': 'Feijao', 'name': 'Maria', 'data': date.today(), 'url': 'https://picsum.photos/seed/picsum/650/300'}],
        'is_home_page': True,
    })


def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': {'id': '1', 'title': 'Feijoada', 'name': 'Will'},
    })

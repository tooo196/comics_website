from django.db import models

# Create your models here.
comics_data = [
    {
        'id': 1,
        'title': 'Супергерои: Начало',
        'author': 'Марк Джонсон',
        'description': 'Захватывающая история о первых шагах супергероев',
        'image': 'comic1.jpg',
        'pages': 24,
        'genre': 'Супергерои'
    },
    {
        'id': 2,
        'title': 'Космические приключения',
        'author': 'Анна Смит',
        'description': 'Фантастический комикс о межгалактических путешествиях',
        'image': 'comic2.jpg',
        'pages': 32,
        'genre': 'Фантастика'
    },
    {
        'id': 3,
        'title': 'Детектив в большом городе',
        'author': 'Роберт Чейз',
        'description': 'Загадочное дело, которое предстоит раскрыть',
        'image': 'comic3.jpg',
        'pages': 28,
        'genre': 'Детектив'
    }
]
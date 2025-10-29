from django.db import models

# Create your models here.
comics_data = {
    'ru': [
    {
        'id': 1,
        'title': 'Король в Чёрном',
        'author': 'Marvel',
        'description': 'Комикс «Король в Чёрном» повествует о масштабном вторжении Кналла, бога симбиотов. После долгого и глубокого сна Кналл пробуждается и направляется на Землю с целью завоевания и подчинения всех носителей симбиотов. Его возвращение вызывает хаос, и мир оказывается на грани разрушения.',
        'image': 'comic1.jpg',
        'pages': 24,
        'genre': 'Супергерои'
    },
    {
        'id': 2,
        'title': 'Бэтмен: Три Джокера',
        'author': 'DC Comics',
        'description': 'Серия рассказывает историю о трех разных Джокерах, которые появились в Готэме. Бэтмен и его союзники - Барбара Гордон (Бэтгерл) и Джейсон Тодд (Красный Капюшон) - сталкиваются с тремя Джокерами, каждый из которых проявляет свои уникальные черты.',
        'image': 'comic2.jpg',
        'pages': 32,
        'genre': 'Фантастика'
    },
    {
        'id': 3,
        'title': 'Пацаны',
        'author': 'Dynamite Entertainment',
        'description': 'Сюжет "Пацанов" разворачивается в мире, где супергерои являются популярными и могущественными фигурами, но часто злоупотребляют своей властью и причиняют разрушение и насилие. Главные герои комикса - члены секретной группы под названием "Пацаны", назначенные правительством Соединенных Штатов для контроля и нейтрализации супергероев, выходящих из-под контроля.',
        'image': 'comic3.jpg',
        'pages': 28,
        'genre': 'Фантастика'
    }],
    'en': [
    {
        'id': 1,
        'title': 'King In Black',
        'author': 'Marvel',
        'description': 'The comic "King in Black" tells the story of a massive invasion by Knall, the god of symbiotes. After a long and deep sleep, Knall awakens and heads to Earth in order to conquer and subjugate all the symbiote carriers. His return causes chaos, and the world is on the verge of destruction.',
        'image': 'comic1.jpg',
        'pages': 24,
        'genre': 'Superhero',
        'rating': 4.8,
        'year': 2023
    },
    {
        'id': 2,
        'title': 'Batman: Three Jokers',
        'author': 'DC Comics',
        'description': 'The series tells the story of three different Jokers who appeared in Gotham. Batman and his allies, Barbara Gordon (Batgirl) and Jason Todd (Red Hood), face three Jokers, each with their own unique traits.',
        'image': 'comic2.jpg',
        'pages': 32,
        'genre': 'Superhero',
        'rating': 4.6,
        'year': 2024
    },
    {
        'id': 3,
        'title': 'The Boys',
        'author': 'Dynamite Entertainment',
        'description': 'The plot of "Boys" takes place in a world where superheroes are popular and powerful figures, but they often abuse their power and cause destruction and violence. The main characters of the comic are members of a secret group called "The Boys," appointed by the United States government to control and neutralize superheroes who are spiraling out of control.',
        'image': 'comic3.jpg',
        'pages': 28,
        'genre': 'Superhero',
        'rating': 4.7,
        'year': 2023
    }
]}

# Локализованные тексты для интерфейса
LOCALIZED_TEXTS = {
    'ru': {
        'site_title': 'Комиксы Онлайн',
        'home': 'Главная',
        'display_settings': 'Настройки отображения',
        'theme': 'Тема оформления',
        'language': 'Язык интерфейса',
        'font_size': 'Размер шрифта',
        'save_settings': 'Сохранить настройки',
        'available_comics': 'Доступные комиксы',
        'author': 'Автор',
        'genre': 'Жанр',
        'pages': 'Страниц',
        'read': 'Читать',
        'recently_viewed': 'Недавно просмотренные',
        'back_to_list': 'Назад к списку',
        'all_rights_reserved': 'Все права защищены.',
        'rating': 'Рейтинг',
        'year': 'Год',
        'clear_history': 'Очистить историю',
        'no_comics': 'Комиксы не найдены',
        'pages_short': 'стр.',
        'view_details': 'Подробнее',
        'light_theme': 'Светлая тема',
        'dark_theme': 'Темная тема',
        'comic_theme': 'Комикс стиль',
        'russian': 'Русский',
        'english': 'Английский'
    },
    'en': {
        'site_title': 'Comics Online',
        'home': 'Home',
        'display_settings': 'Display Settings',
        'theme': 'Theme',
        'language': 'Language',
        'font_size': 'Font Size',
        'save_settings': 'Save Settings',
        'available_comics': 'Available Comics',
        'author': 'Author',
        'genre': 'Genre',
        'pages': 'Pages',
        'read': 'Read',
        'recently_viewed': 'Recently Viewed',
        'back_to_list': 'Back to list',
        'all_rights_reserved': 'All rights reserved.',
        'rating': 'Rating',
        'year': 'Year',
        'clear_history': 'Clear History',
        'no_comics': 'No comics found',
        'pages_short': 'p.',
        'view_details': 'View Details',
        'light_theme': 'Light theme',
        'dark_theme': 'Dark theme',
        'comic_theme': 'Comic style',
        'russian': 'Russian',
        'english': 'English'
    }
}

# Настройки тем оформления
THEME_SETTINGS = {
    'light': {
        'background_color': '#ffffff',
        'text_color': '#333333',
        'card_background': '#ffffff',
        'header_background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'font_family': 'Arial, sans-serif'
    },
    'dark': {
        'background_color': '#1a1a1a',
        'text_color': '#ffffff',
        'card_background': '#2d2d2d',
        'header_background': 'linear-gradient(135deg, #2c3e50 0%, #3498db 100%)',
        'font_family': 'Arial, sans-serif'
    },
    'comic': {
        'background_color': '#fff8e1',
        'text_color': '#333333',
        'card_background': '#ffffff',
        'header_background': 'linear-gradient(135deg, #ff6b6b 0%, #ffd93d 100%)',
        'font_family': '"Comic Sans MS", cursive, sans-serif'
    }
}

def get_localized_comics(language):
    """
    Возвращает список комиксов на выбранном языке
    """
    return comics_data.get(language, comics_data['ru'])

def get_localized_texts(language):
    """
    Возвращает словарь с локализованными текстами для интерфейса
    """
    return LOCALIZED_TEXTS.get(language, LOCALIZED_TEXTS['ru'])

def get_theme_settings(theme):
    """
    Возвращает настройки CSS для выбранной темы
    """
    return THEME_SETTINGS.get(theme, THEME_SETTINGS['light'])

def get_comic_by_id(comic_id, language):
    """
    Находит комикс по ID на выбранном языке
    """
    comics = get_localized_comics(language)
    return next((comic for comic in comics if comic['id'] == comic_id), None)
from django.shortcuts import render, redirect
from .forms import SettingsForm
from .models import (
    get_localized_comics,
    get_localized_texts,
    get_comic_by_id
)


def comics_list(request):
    """
    Главная страница со списком комиксов и настройками
    """
    # Получаем настройки из cookies
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'ru')
    font_size = request.COOKIES.get('font_size', '16')

    # Получаем локализованные тексты
    texts = get_localized_texts(language)

    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            # Создаем response для установки cookies
            response = redirect('comics_list')

            # Сохраняем настройки в cookies на 30 дней
            new_theme = form.cleaned_data['theme']
            new_language = form.cleaned_data['language']
            new_font_size = str(form.cleaned_data['font_size'])

            response.set_cookie('theme', new_theme, max_age=30*24*60*60)
            response.set_cookie('language', new_language, max_age=30*24*60*60)
            response.set_cookie('font_size', new_font_size, max_age=30*24*60*60)

            return response
    else:
        # Заполняем форму текущими значениями из cookies
        form = SettingsForm(initial={
            'theme': theme,
            'language': language,
            'font_size': int(font_size)
        })

    # Получаем комиксы на выбранном языке
    comics = get_localized_comics(language)

    # Получаем историю просмотров
    viewed_comics = request.COOKIES.get('viewed_comics', '')
    viewed_list = viewed_comics.split(',') if viewed_comics else []

    # Фильтруем просмотренные комиксы
    viewed_comics_list = []
    for comic_id in viewed_list:
        comic = get_comic_by_id(int(comic_id), language)
        if comic:
            viewed_comics_list.append(comic)

    context = {
        'comics': comics,
        'viewed_comics': viewed_comics_list[:5],
        'form': form,
        'current_theme': theme,
        'current_language': language,
        'current_font_size': font_size,
        'texts': texts
    }

    return render(request, 'comics/list.html', context)

def comic_detail(request, comic_id):
    """
    Страница детального просмотра комикса
    """
    # Получаем настройки из cookies
    language = request.COOKIES.get('language', 'ru')
    theme = request.COOKIES.get('theme', 'light')
    font_size = request.COOKIES.get('font_size', '16')

    # Получаем локализованные тексты
    texts = get_localized_texts(language)

    # Находим комикс по ID
    comic = get_comic_by_id(comic_id, language)

    if not comic:
        return redirect('comics_list')

    # Получаем историю просмотров
    viewed_comics = request.COOKIES.get('viewed_comics', '')
    viewed_list = viewed_comics.split(',') if viewed_comics else []

    # Обновляем историю просмотров
    if str(comic_id) not in viewed_list:
        viewed_list.insert(0, str(comic_id))
        viewed_list = viewed_list[:5]

    # Получаем похожие комиксы (того же жанра)
    comics = get_localized_comics(language)
    similar_comics = [c for c in comics if c['genre'] == comic['genre'] and c['id'] != comic_id][:3]

    context = {
        'comic': comic,
        'similar_comics': similar_comics,
        'current_theme': theme,
        'current_language': language,
        'current_font_size': font_size,
        'texts': texts
    }

    # Создаем response для установки cookies
    response = render(request, 'comics/detail.html', context)
    response.set_cookie('viewed_comics', ','.join(viewed_list), max_age=30*24*60*60)

    return response

def clear_history(request):
    """
    Очистка истории просмотров
    """
    response = redirect('comics_list')
    response.delete_cookie('viewed_comics')
    return response
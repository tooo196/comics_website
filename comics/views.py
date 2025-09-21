from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import SettingsForm
from .models import comics_data

def comics_list(request):
    # Получаем настройки из cookies
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'ru')
    font_size = request.COOKIES.get('font_size', '16')

    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            response = redirect('comics_list')
            # Сохраняем настройки в cookies на 30 дней
            response.set_cookie('theme', form.cleaned_data['theme'], max_age=30*24*60*60)
            response.set_cookie('language', form.cleaned_data['language'], max_age=30*24*60*60)
            response.set_cookie('font_size', str(form.cleaned_data['font_size']), max_age=30*24*60*60)
            return response
    else:
        form = SettingsForm(initial={
            'theme': theme,
            'language': language,
            'font_size': int(font_size)
        })

    context = {
        'comics': comics_data,
        'form': form,
        'current_theme': theme,
        'current_language': language,
        'current_font_size': font_size
    }
    return render(request, 'comics/list.html', context)

def comic_detail(request, comic_id):
    comic = next((c for c in comics_data if c['id'] == comic_id), None)
    if not comic:
        return redirect('comics_list')

    # Получаем историю просмотров
    viewed_comics = request.COOKIES.get('viewed_comics', '')
    viewed_list = viewed_comics.split(',') if viewed_comics else []

    # Добавляем текущий комикс в историю (если его там нет)
    if str(comic_id) not in viewed_list:
        viewed_list.insert(0, str(comic_id))
        viewed_list = viewed_list[:5]  # Ограничиваем историю 5 комиксами

    response = render(request, 'comics/detail.html', {
        'comic': comic,
        'viewed_comics': [c for c in comics_data if str(c['id']) in viewed_list[:5]]
    })

    # Сохраняем историю просмотров
    response.set_cookie('viewed_comics', ','.join(viewed_list), max_age=30*24*60*60)
    return response
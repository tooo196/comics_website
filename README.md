# Комиксы Онлайн

Веб-сайт для чтения комиксов с настройками внешнего вида.

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone <ваш-репозиторий>
cd comics_website

    Создайте виртуальное окружение:

bash

python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

    Установите зависимости:

bash

pip install -r requirements.txt

    Примените миграции:

bash

python manage.py migrate

    Запустите сервер:

bash

python manage.py runserver
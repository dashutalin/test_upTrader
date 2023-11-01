# test_upTrader

## Описание
Проект представляет собой создание древовидного меню.
В проекте присутствувует создание собственного тэга, ORM.
Используется СУБД Postgresql.

## Как запустить проект на локальной машине
Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:dashutalin/test_upTrader.git
cd test_upTrader
```
Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```bash
pip install -r req.txt
```
Выполнить миграции:
```bash
python manage.py migrate
```
Загрузитьо тестовые данные в базу данных:
```bash
python manage.py loaddata ../db.json
```
Запустить проект:
```bash
python manage.py runserver

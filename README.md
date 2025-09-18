- python3 -m venv venv
- source venv/bin/activate
- pip3 install django # pip3 freeze > requirements.txt
- pip3 freeze > requirements.txt

- django-admin startproject staff
- cd staff
-- staff/staff - конфиг проекта
-- staff/manage.py - управление проектом
--- проект : Яндекс
--- приложение : Яндекс.Карты
--- INSTALLED_APPS - приложения
--- приложение - store
--- python3 manage.py startapp store

- python3 manage.py [команда]

# client-server arch

- клиент (браузер) -> URL -> (GET / POST) -> сервер
- сервер: маршрутизация - urls.py (URL(path) -> python-function(view)) 
- сервер: views.py - логика обработки данных -> ответ клиенту
- сервер: models.py - структура базы данных -> ORM -> migrate -> BD
- сервер: templates - внешний вид данных (html)
- сервер: url -> request -> views (templates + models) -> response -> client

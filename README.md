# Django-blog-v1.0

**Django Blog v1.0** — это мощная и масштабируемая платформа для блогов, созданная с использованием Django. Проект демонстрирует навыки веб-разработки, работы с API, аутентификации и управления контентом через админ-панель.

## Основные возможности

- Аутентификация пользователей (регистрация, вход, восстановление пароля)
- Полный CRUD для постов
- Комментарии
- REST API для постов
- Админ-панель
- Email-уведомления

## Технические особенности

- **Django**, **Django REST Framework**
- **SQLite** (по умолчанию)
- **Bootstrap** для интерфейса
- **AJAX** для обновления без перезагрузки

## Требования

- Python 3.8+
- Django 3.2+
- SQLite

## Установка и настройка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Mrklv001/Django-blog-v1.0.git

2. Перейдите в директорию проекта:
   ```bash
   cd Django-blog-v1.0
   
3. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv env
   source env/bin/activate  # для Windows: `env\Scripts\activate`

4. Установите зависимости:
   ```bash
   pip install -r requirements.txt

5. Примените миграции:
   ```bash
   python manage.py migrate

6. Создайте суперпользователя:
   ```bash
   python manage.py createsuperuser

7. Запустите сервер разработки:
   ```bash
   python manage.py runserver

## Использование
**API**

- GET /api/posts/
- POST /api/posts/
- PUT /api/posts/{id}/
- DELETE /api/posts/{id}/

**Админ-панель**

Админ-панель доступна по адресу http://localhost:8000/admin.

## Тестирование

**Запустите тесты:**
```bash
python manage.py test
```

## Развертывание

1. Настройте файл .env.
2. Настройте базу данных (например, PostgreSQL).
3. Настройте сервер (Gunicorn + Nginx).

## Вклад в проект

1. Сделайте форк проекта.
2. Создайте ветку:
```bash
git checkout -b feature/my-feature
```
3. Сделайте коммит:
```bash
git commit -m "Добавлена новая функция"
```
4. Отправьте изменения:
```bash
git push origin feature/my-feature
```

5. Создайте Pull Request.

## Лицензия

Проект распространяется под лицензией MIT. См. файл LICENSE для получения подробной информации.



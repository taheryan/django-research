# Django members App

This repository contains a minimal Django project (`my_tennis_club`) with a `members` app and pytest tests.

Quick start:
1. Create a virtualenv and install dependencies:
   pip install -r requirements.txt

2. Apply migrations:
   python manage.py migrate

3. Run the development server:
   python manage.py runserver

4. Run tests:
   pytest

The app provides:
- List tasks, add tasks (via the list page), toggle completion, delete tasks.

Notes:
- This project uses the default Django SQLite database `db.sqlite3`.
- Tests use pytest + pytest-django. The pytest.ini file sets DJANGO_SETTINGS_MODULE to `my_tennis_club.settings`.
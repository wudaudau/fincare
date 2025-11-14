---
mode: agent
---
Define the task to achieve, including specific requirements, constraints, and success criteria.

1. Set up a new Django project named as "core".

    ```bash
    django-admin startproject core
    ```

2. Create the following Django apps within the project: "finance", "authentication", and "dashboard".

    ```bash
    mkdir apps
    python manage.py startapp apps/finance
    python manage.py startapp apps/authentication
    python manage.py startapp apps/dashboard
    ```

3. Create a directory structure for static files and templates within the project.

    ```bash
    mkdir -p apps/static/css apps/static/js apps/static/images
    mkdir -p apps/templates/includes
    mkdir -p apps/templates/finance
    mkdir -p apps/templates/authentication
    mkdir -p apps/templates/dashboard
    ```

4. Create an admin user for the Django project.

    ```bash
    python manage.py createsuperuser
    ```

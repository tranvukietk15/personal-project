on mac:

- Create admin project: django-admin startproject mysite
- Create app: python manage.py startapp polls
- Create migrations: python manage.py makemigrations polls
- Update database: python manage.py sqlmigrate polls 0001 || python manage.py migrate

GRAPHQL
- Install graphql: 
    pip install graphene-django
    pip install django-graphiql
    
    INSTALLED_APPS = [
        ...
        "django.contrib.staticfiles", # Required for GraphiQL
        "graphene_django"
    ]
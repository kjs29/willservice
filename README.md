# When changing from production to development

1. settings.py
```py
DEBUG = True
ALLOWED_HOSTS = ['www.calgarymobilewills.ca','calgarymobilewills.ca','127.0.0.1']
PREPEND_WWW = False
```

2. Terminal
```
python manage.py makemigrations wills
```

```
python manage.py migrate
```

3. Add questionnaire file

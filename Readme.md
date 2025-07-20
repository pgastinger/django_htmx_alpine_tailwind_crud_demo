# Django demo with htmx, alpinejs and tailwind css

## How to run

- commands
```
git clone https://github.com/pgastinger/django_htmx_alpine_tailwind_crud_demo.git
cd django_htmx_alpine_tailwind_crud_demo/
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt 
python manage.py migrate
python manage.py runserver
```

- log
``` bash
peter@pptm-linux:/tmp$ git clone https://github.com/pgastinger/django_htmx_alpine_tailwind_crud_demo.git
Cloning into 'django_htmx_alpine_tailwind_crud_demo'...
remote: Enumerating objects: 70, done.
remote: Counting objects: 100% (70/70), done.
remote: Compressing objects: 100% (43/43), done.
remote: Total 70 (delta 17), reused 70 (delta 17), pack-reused 0 (from 0)
Receiving objects: 100% (70/70), 28.90 KiB | 5.78 MiB/s, done.
Resolving deltas: 100% (17/17), done.
peter@pptm-linux:/tmp$ cd django_htmx_alpine_tailwind_crud_demo/
peter@pptm-linux:/tmp/django_htmx_alpine_tailwind_crud_demo$ python3 -m venv venv
peter@pptm-linux:/tmp/django_htmx_alpine_tailwind_crud_demo$ . venv/bin/activate
(venv) peter@pptm-linux:/tmp/django_htmx_alpine_tailwind_crud_demo$ pip install -r requirements.txt 
Collecting Django>=4.0 (from -r requirements.txt (line 1))
  Using cached django-5.2.4-py3-none-any.whl.metadata (4.1 kB)
Collecting django-htmx (from -r requirements.txt (line 2))
  Using cached django_htmx-1.23.2-py3-none-any.whl.metadata (2.6 kB)
Collecting asgiref>=3.8.1 (from Django>=4.0->-r requirements.txt (line 1))
  Using cached asgiref-3.9.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.3.1 (from Django>=4.0->-r requirements.txt (line 1))
  Using cached sqlparse-0.5.3-py3-none-any.whl.metadata (3.9 kB)
Using cached django-5.2.4-py3-none-any.whl (8.3 MB)
Using cached django_htmx-1.23.2-py3-none-any.whl (61 kB)
Using cached asgiref-3.9.1-py3-none-any.whl (23 kB)
Using cached sqlparse-0.5.3-py3-none-any.whl (44 kB)
Installing collected packages: sqlparse, asgiref, Django, django-htmx
Successfully installed Django-5.2.4 asgiref-3.9.1 django-htmx-1.23.2 sqlparse-0.5.3
(venv) peter@pptm-linux:/tmp/django_htmx_alpine_tailwind_crud_demo$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, tasks
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  Applying tasks.0001_initial... OK
(venv) peter@pptm-linux:/tmp/django_htmx_alpine_tailwind_crud_demo$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 20, 2025 - 11:14:00
Django version 5.2.4, using settings 'django_htmx_project.settings.dev'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
```

- Update tailwind css

```bash
npm install tailwindcss @tailwindcss/cli
npx @tailwindcss/cli -i static/css/input.css -o static/css/main.css
```

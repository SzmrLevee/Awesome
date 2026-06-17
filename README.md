
# Django Projekt Indítása

## 1. Python verzió ellenőrzése

```bash
python3 --version
```

---

## 2. Virtuális környezet létrehozása

```bash
python3 -m venv venv
```

A `venv` modul segítségével létrejön egy `venv` nevű virtuális környezet.

### Aktiválás PowerShell-ben

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 3. Django telepítése

```bash
pip install django
```

### Pip frissítése

```bash
python3 -m pip install --upgrade pip
```

---

## 4. Django projekt létrehozása

```bash
django-admin startproject a_core .
```

Ez létrehozza az `a_core` projektet az aktuális mappában.

---

## 5. Fejlesztői szerver indítása

```bash
python manage.py runserver
```

A szerver leállítása:

```text
CTRL + C
```

---

## 6. Adatbázis migrációk futtatása

```bash
python manage.py migrate
```

Ez létrehozza az alapértelmezett Django táblákat (auth, sessions stb.).

---

## 7. Admin felhasználó létrehozása

```bash
python manage.py createsuperuser
```

---

## 8. Szerver újraindítása

```bash
python manage.py runserver
```

---

# Templates mappa beállítása

Hozz létre egy `templates` mappát a projekt gyökerében.

### `a_core/settings.py`

Módosítsd a `TEMPLATES` beállítást:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

A fontos rész:

```python
BASE_DIR / 'templates'
```

---

# Új alkalmazás létrehozása

```bash
python manage.py startapp a_posts
```

---

# App regisztrálása

### `a_core/settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'a_posts',
]
```

---

# Első View létrehozása

### `a_posts/views.py`

```python
from django.shortcuts import render


def home_view(request):
    return render(request, 'index.html')
```

---

# URL Routing beállítása

### `a_core/urls.py`

```python
from django.contrib import admin
from django.urls import path

from a_posts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
]
```

Szükséges:

```python
from a_posts.views import *
```

és

```python
path('', home_view)
```

---

# Adatok átadása a Template-nek

### `a_posts/views.py`

```python
from django.shortcuts import render


def home_view(request):
    title = 'Welcome to Django'

    return render(
        request,
        'index.html',
        {
            'title': title
        }
    )
```

---

# Template használata

### `templates/index.html`

Korábban:

```html
<h1 class="font1 text-6xl title-fadein">
    Awesome Photos & Captions
</h1>
```

Módosítás:

```html
<h1 class="font1 text-6xl title-fadein">
    {{ title }}
</h1>
```

Így a cím dinamikusan a Django View-ból érkezik.

```
```

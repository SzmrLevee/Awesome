
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

# Automatikus böngésző frissítés Django alatt

Django fejlesztés közben a `runserver` újraindítja a szervert fájlváltozáskor, de a böngészőt nem frissíti automatikusan. Ehhez használható a `django-browser-reload`.

## 1. Telepítés

```bash
pip install django-browser-reload
```

## 2. App regisztrálása

### `a_core/settings.py`

Az `INSTALLED_APPS` listához add hozzá:

```python
INSTALLED_APPS = [
    ...
    'django_browser_reload',
]
```

Fontos: telepítéskor kötőjel van:

```bash
django-browser-reload
```

de a Django beállításokban aláhúzás kell:

```python
django_browser_reload
```

## 3. Middleware hozzáadása

### `a_core/settings.py`

A `MIDDLEWARE` lista végére add hozzá:

```python
MIDDLEWARE = [
    ...
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]
```

## 4. URL beállítása

### `a_core/urls.py`

Az import legyen:

```python
from django.urls import path, include
```

Majd az `urlpatterns` listába kerüljön bele:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),

    path('__reload__/', include('django_browser_reload.urls')),
]
```

## 5. Template beállítása

### `templates/index.html`

A fájl elejére:

```html
{% load django_browser_reload %}
```

Majd közvetlenül a `</body>` elé:

```html
{% django_browser_reload_script %}
```

Példa:

```html
{% load django_browser_reload %}
<!DOCTYPE html>
<html lang="en">
<head>
    ...
</head>
<body>

    ...

    {% django_browser_reload_script %}
</body>
</html>
```

## 6. Szerver újraindítása

```bash
python manage.py runserver
```

Ezután HTML, CSS vagy Python fájl mentésekor a böngésző automatikusan frissül.

# Minimized CSS

## 1. Node.js verzió ellenőrzése

```bash
node --version
```

---

## 2. Tailwind mappa létrehozása

A `templates` mappán belül hozz létre egy `tailwind` mappát.

```text
templates/
└── tailwind/
```

Lépj be a mappába:

```bash
cd templates/tailwind
```

---

## 3. NPM projekt inicializálása

```bash
npm init -y
```

---

## 4. Tailwind CSS telepítése

```bash
npm install -D tailwindcss@3 postcss autoprefixer
```

---

## 5. Konfigurációs fájlok létrehozása

```bash
npx tailwindcss init -p
```

Ez létrehozza:

```text
tailwind.config.js
postcss.config.js
```

---

## 6. Tailwind CSS fájl létrehozása

Hozz létre egy `tailwind.css` fájlt:

```text
templates/
└── tailwind/
    └── tailwind.css
```

Tartalma:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

---

## 7. Tailwind konfiguráció

### `tailwind.config.js`

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['../index.html'],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

---

## 8. Git Ignore

### `.gitignore`

```gitignore
# Python
venv/
__pycache__/
*.pyc

# Django
db.sqlite3

# Node
node_modules/

# Build
dist/

# VS Code
.vscode/

# OS
.DS_Store
Thumbs.db
```

---

## 9. Build Script beállítása

### `package.json`

Alapértelmezett:

```json
"scripts": {
  "test": "echo \"Error: no test specified\" && exit 1"
}
```

Cseréld erre:

```json
"scripts": {
  "tailwind": "tailwind build -i tailwind.css -o ../../static/style.css --watch"
}
```

---

## 10. Static mappa létrehozása

A projekt gyökerében:

```text
static/
└── style.css
```

A `style.css` fájlt a Tailwind automatikusan generálja.

---

## 11. Django Static Files beállítása

### `a_core/settings.py`

```python
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

---

## 12. Static betöltése a Template-ben

A fájl elejére:

```django
{% load static %}
```

A `<head>` részbe:

```html
<link rel="stylesheet" href="{% static 'style.css' %}">
```

Ezután a korábbi Tailwind CDN link eltávolítható.

---

## 13. Tailwind Build indítása

A `templates/tailwind` mappában:

```bash
npm run tailwind
```

A parancs figyeli a változásokat és automatikusan újragenerálja a CSS-t.

---

## 14. Django szerver indítása

### 1. Terminál

```bash
python manage.py runserver
```

### 2. Terminál

```bash
cd templates/tailwind
npm run tailwind
```

Mindkét folyamatnak futnia kell fejlesztés közben.

# CSS Minifikálás Tailwind után

A Tailwind által generált `style.css` fájl tovább csökkenthető minifikálással.

## 1. Clean CSS CLI telepítése

A `templates/tailwind` mappában:

```bash
npm install clean-css-cli
```

---

## 2. Package.json módosítása

### `package.json`

```json
"scripts": {
  "tailwind": "tailwind build -i tailwind.css -o ../../static/style.css --watch",
  "minify": "cleancss ../../static/style.css -o ../../static/style.min.css"
}
```

---

## 3. CSS minifikálása

```bash
npm run minify
```

Ez létrehozza:

```text
static/
├── style.css
└── style.min.css
```

A `style.min.css` tömörített változat, kisebb méretű és gyorsabban töltődik be.

---

## 4. Django Template módosítása

Korábban:

```html
<link rel="stylesheet" href="{% static 'style.css' %}">
```

Módosítsd erre:

```html
<link rel="stylesheet" href="{% static 'style.min.css' %}">
```

---

## 5. Fejlesztés közbeni workflow

### Tailwind figyelése

```bash
npm run tailwind
```

### Minifikálás

Minden nagyobb módosítás után:

```bash
npm run minify
```

---

## Végleges struktúra

```text
awesome/
├── static/
│   ├── style.css
│   └── style.min.css
│
├── templates/
│   ├── index.html
│   └── tailwind/
│       ├── tailwind.css
│       ├── package.json
│       ├── postcss.config.js
│       └── tailwind.config.js
│
├── a_core/
└── manage.py
```

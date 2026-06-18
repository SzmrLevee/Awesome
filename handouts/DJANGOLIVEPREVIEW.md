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
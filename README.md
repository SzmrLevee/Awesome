# Awesome

Django + Tailwind CSS gyakorló projekt.

## Projekt klónozása

```bash
git clone <repository-url>
cd awesome
```

## Virtuális környezet aktiválása

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Python függőségek telepítése

```bash
pip install django
pip install django-browser-reload
```

## Node modulok telepítése

```bash
cd templates/tailwind
npm install
```

Ez telepíti a projektben használt csomagokat:

* Tailwind CSS
* PostCSS
* Autoprefixer
* Clean CSS CLI

## Projekt indítása

### 1. Terminál

A projekt gyökerében:

```bash
python manage.py runserver
```

Debug mód nélkül:

```bash
python manage.py runserver --insecure
```

### 2. Terminál

A Tailwind mappában:

```bash
cd templates/tailwind
npm run tailwind
```

## CSS minifikálása

Nagyobb módosítások után:

```bash
cd templates/tailwind
npm run minify
```

Ez frissíti a:

```text
static/style.min.css
```

fájlt.

## Használt technológiák

* Python
* Django
* Tailwind CSS
* PostCSS
* Alpine.js
* django-browser-reload
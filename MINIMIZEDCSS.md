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
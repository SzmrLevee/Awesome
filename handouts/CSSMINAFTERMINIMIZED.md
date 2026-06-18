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
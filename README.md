python3 --version
python3 -m venv venv - venv module as venv 
.\venv\Scripts\Activate.ps1 

pip install django
python3 -m pip install --upgrade pip

django-admin startproject a_core .  - a_core with packages in the folder

python manage.py runserver - run the server

CTRL C - Stop the server

python manage.py migrate - tables, authentications
python manage.py createsuperuser
python manage.py runserver - run the server

templates folder creation than in the a_core/settings:

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'],
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

BASE_DIR / 'templates'

python manage.py startapp a_posts

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'a_posts'
]

'a_posts'

a_posts/views.py:

def home_view(request):
    return render(request, 'index.html')

a_core/urls.py:

from a_posts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view)
]

from a_posts.views import *
AND 
path('', home_view)

a_posts/views.py:

def home_view(request):
    title = 'Welcome to Django'
    return render(request, 'index.html', {'title': title})

templates/index.html:
<h1 class="font1 text-6xl title-fadein">Awesome Photos & Captions</h1>
->
<h1 class="font1 text-6xl title-fadein">{{ title }}</h1>
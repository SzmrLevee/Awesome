#!/bin/sh

set -e

if [ ! -f /app/a_core/.env ] && [ -f /app/a_core/.env.example ]; then
    cp /app/a_core/.env.example /app/a_core/.env
fi

python manage.py makemigrations
python manage.py migrate

python manage.py shell -c "
from django.contrib.sites.models import Site
from django.conf import settings
Site.objects.update_or_create(
    id=1,
    defaults={'domain': 'localhost:8000', 'name': settings.PROJECT_TITLE}
)
"

python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'root_p_ssW0rd')
"

python manage.py runserver 0.0.0.0:8000
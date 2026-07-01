# Awesome

Django + Tailwind CSS gyakorló projekt Docker támogatással.

## Indítás Dockerrel

Windows PowerShell:

```powershell
.\start.ps1
```

Linux / macOS:

```bash
./start.sh
```

Az első indítás során automatikusan:

* létrejön az `a_core/.env` fájl, ha hiányzik
* lefutnak a migrációk
* létrejön vagy frissül a Django `Site`
* létrejön az `admin` superuser
* elindul az app, a PostgreSQL, a Redis, a Celery worker, a Celery Beat és a Flower

## Elérhetőségek

| Szolgáltatás | URL                     |
| ------------ | ----------------------- |
| Django       | http://localhost:8000   |
| Admin        | http://localhost:8000/admin |
| Flower       | http://localhost:5555   |

### Alapértelmezett admin

```text
Username: admin
Password: root_p_ssW0rd
```

## Technológiák

* Python
* Django
* PostgreSQL
* Redis
* Celery
* Flower
* Tailwind CSS
* django-allauth
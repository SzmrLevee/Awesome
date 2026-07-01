from django.conf import settings


def project_title(request):
    return {
        'project_title': getattr(settings, 'PROJECT_TITLE', 'Awesome'),
    }
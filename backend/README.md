# generate secret key

    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    python -c 'import secrets; print(secrets.token_urlsafe(64))'

# easilty create superuser

    DJANGO_SUPERUSER_USERNAME='<your-username>' DJANGO_SUPERUSER_PASSWORD='<your-password>' DJANGO_SUPERUSER_EMAIL='<your-email>' python manage.py createsuperuser --no-input

## next steps

. add notification logic,
. possible integrate django-allauth, django-allauth-ui, django-anymail, django-channels

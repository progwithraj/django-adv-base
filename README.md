# generate secret key

    - python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    - python -c 'import secrets; print(secrets.token_urlsafe(64))'

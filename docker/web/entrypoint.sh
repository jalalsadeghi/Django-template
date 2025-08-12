#!/usr/bin/env bash
set -euo pipefail

# Run migrations and start the server.
python src/manage.py migrate --noinput
# Create superuser if not exists (optional: controlled by env)
if [ "${DJANGO_SUPERUSER_EMAIL:-}" != "" ]; then
  python src/manage.py shell <<'PY'
from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()
email = settings.SUPERUSER_EMAIL
if not User.objects.filter(username=settings.SUPERUSER_USERNAME).exists():
    User.objects.create_superuser(
        username=settings.SUPERUSER_USERNAME,
        email=settings.SUPERUSER_EMAIL,
        password=settings.SUPERUSER_PASSWORD,
    )
PY
fi

# Collect static (kept minimal; no CSS in spec)
python src/manage.py collectstatic --noinput

# Start Django dev server (sufficient for the task demo)
python src/manage.py runserver 0.0.0.0:8000
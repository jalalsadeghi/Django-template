# MIR MEDIA – Minimal Django Task (Dockerized)

This repository implements the MIR MEDIA Django task **exactly as specified**:
- **Models**: `Article` (title, slug prepopulated from title, content, author FK, publication datetime, online/offline) and `ContactRequest` (email, name, content, date).
- **Admin**: `Article` fully editable; `ContactRequest` can be **deleted only** (no add/edit).
- **Views** (all CBV):
  - Article list (5 per page) with pagination links at bottom and link to detail.
  - Article detail with **both slug and id** in URL, shows title, content, author's full name, publication datetime, and link back to list.
  - Contact view: form saves to DB and sends email to **debug@mir.de**; sets **Reply-To** to user email.
- **Tests**: Django unit tests included.
- **DB**: SQLite.
- **Docker**: Single-container for simplicity.

## Quick Start (Docker)
```bash
cp .env.example .env
# (edit .env as needed; keep DEBUG=1 for local dev)
docker compose up --build
# App: http://localhost:8000
# Admin: http://localhost:8000/admin/ (set SUPERUSER_* envs in .env to auto-create)
```

## Running Tests
```bash
docker compose run --rm web python src/manage.py test -v 2
```

## Production-like Demo
- Set `DEBUG=0` and provide real SMTP settings via env vars to send emails to `debug@mir.de` with a proper Reply-To header.
- Set `ALLOWED_HOSTS` to your domain or host.
- Provide real `SECRET_KEY`.
- Share admin credentials with MIR privately.

## Notes
- Layout intentionally plain (no CSS), per task.
- Comments are **English-only**.
- Minimal dependencies to match the brief’s spirit.
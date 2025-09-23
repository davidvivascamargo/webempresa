import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webempresa.settings")

django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin123")
    print("✅ Superusuario creado: admin / admin123")
else:
    print("ℹ️ El superusuario ya existe.")

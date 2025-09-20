"""
WSGI config for webempresa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webempresa.settings")

application = get_wsgi_application()
"""
"""
WSGI config for webempresa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
import os
import django
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webempresa.settings")

# Inicializamos Django
django.setup()

# Ejecutamos migraciones automáticamente
try:
    call_command('migrate', interactive=False)
    print("Migraciones aplicadas con éxito")
except Exception as e:
    print(f"Error al correr migraciones: {e}")

# Cargar datos si la base está vacía
try:
    from blog.models import Post  # Cambia esto por un modelo real tuyo
    if not Post.objects.exists():
        call_command('loaddata', 'datos.json')
        print("Datos cargados correctamente")
    else:
        print("Ya hay datos, no se cargaron de nuevo.")
except Exception as e:
    print(f"Error al cargar datos: {e}")

# Levantamos la aplicación
application = get_wsgi_application()

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
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webempresa.settings")

django.setup()

# Importa tu función que carga los datos
#from webempresa.load_data import run

# Ejecuta la carga de datos (esto lo puedes controlar para que solo corra la primera vez)
#run()

# Cargar datos automáticamente si es necesario
try:
    import load_data
except Exception as e:
    print(f"⚠ Error al ejecutar load_data: {e}")

application = get_wsgi_application()


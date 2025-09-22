'''
from django.core.management import call_command

def run():
    try:
        call_command('loaddata', 'datos.json')
        print("Datos importados correctamente")
    except Exception as e:
        print(f"Error importando datos: {e}")
'''
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webempresa.settings')
django.setup()

from django.core.management import call_command
from django.db.utils import OperationalError

try:
    # Solo cargar si la base está vacía
    from django.contrib.auth.models import User
    if not User.objects.exists():
        call_command('loaddata', 'datos.json')
        print("✔ Datos cargados correctamente.")
    else:
        print("ℹ Base de datos ya contiene usuarios. No se cargó nada.")
except OperationalError as e:
    print(f"❌ Error al cargar los datos: {e}")

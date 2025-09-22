'''
import os
import django
import json
from django.core.management import call_command
from io import StringIO

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webempresa.settings")
django.setup()

# Dump a string in memory
out = StringIO()
call_command("dumpdata", stdout=out, indent=2)
data = out.getvalue()

# Parse and re-dump with ensure_ascii=False
parsed = json.loads(data)
with open("datos.json", "w", encoding="utf-8") as f:
    json.dump(parsed, f, indent=2, ensure_ascii=False)
'''
from django.core.management import call_command

with open('datos.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata',
                 exclude=['auth.permission', 'contenttypes'],
                 indent=4,
                 stdout=f)

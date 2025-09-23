import os
import django
import json
from django.core.management import call_command
from io import StringIO

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webempresa.settings")
django.setup()

out = StringIO()

call_command("dumpdata", exclude=['auth.permission', 'contenttypes'], stdout=out, indent=4)

data = out.getvalue()

parsed = json.loads(data)

with open("datos_completo_utf8.json", "w", encoding="utf-8") as f:
    json.dump(parsed, f, indent=4, ensure_ascii=False)

print("Dump completo guardado en datos_completo_utf8.json")

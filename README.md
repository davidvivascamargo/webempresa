# Neko Cream - Proyecto de Pruebas en Django

Este es un proyecto de prueba desarrollado con **Django 5**, con fines educativos y experimentales. Permite explorar la creación de aplicaciones web completas con gestión de contenido, 
formulario de contacto,  manejo de contenido dinámico, páginas estáticas y un **panel de administración personalizado**.

---

 ## 🌟 Características principales

### Panel de administración personalizado
- Gestión completa de usuarios y grupos.
- Gestión de contenido del **blog**:
  - Posts con títulos, imágenes, autores, fechas de publicación y categorías.
- Gestión de **páginas estáticas**.
- Administración de **servicios** con:
  - Títulos, subtítulos, contenido enriquecido (CKEditor) e imágenes.
- Administración de **enlaces a redes sociales**.
- Campos de solo lectura (`created`, `updated`) y ordenamiento automático.
- Búsquedas, filtros y experiencia mejorada en el admin.

### Front-end dinámico
- Las páginas cargan contenido directamente desde el **admin de Django**:
  - **Inicio**, **Historia**, **Servicios**, **Visítanos**, **Contacto**, **Blog**.
- Diseño **responsivo** con **Bootstrap 5**.
- Formularios funcionales, como el formulario de contacto con envío de correo.
- Uso de **CKEditor** para contenido enriquecido en servicios y posts.

### Experiencia de usuario
- Blog con posts, categorías e imágenes.
- Servicios con títulos, subtítulos, descripciones y fotografías cargadas desde el admin.
- Contacto con validación de campos y confirmación de envío.
- Navegación intuitiva y moderna con menú activo según la página.

---

## 🗂 Estructura del proyecto

webempresa/
├─ core/ # Plantillas y recursos estáticos
├─ services/ # Gestión de servicios
├─ blog/ # Gestión de posts y categorías
├─ pages/ # Gestión de páginas estáticas
├─ contact/ # Formulario de contacto
├─ social/ # Gestión de enlaces de redes sociales
├─ media/ # Archivos subidos (imágenes de blog, servicios, etc.)
├─ staticfiles/ # Archivos estáticos recolectados
├─ manage.py
└─ requirements.txt

---

## ⚙️ Instalación rápida

1. Clonar el repositorio:

```bash
git clone https://github.com/davidvivascamargo/webempresa.git
cd webempresa
Crear y activar un entorno virtual:

bash
Copiar código
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt
Aplicar migraciones:

bash
Copiar código
python manage.py migrate
Crear superusuario para acceder al admin:

bash
Copiar código
python manage.py createsuperuser
Ejecutar servidor local:

bash
Copiar código
python manage.py runserver
Accede a: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

📝 Notas importantes
Proyecto experimental; no está optimizado para producción.

Todo el contenido se gestiona desde el panel de administración.

Posts del blog, servicios, páginas y enlaces de redes sociales.

El formulario de contacto requiere configuración de correo en settings.py.

Las imágenes y archivos subidos se almacenan en media/.

Los estilos y scripts se cargan desde static/ y librerías externas (Bootstrap, Font Awesome).

📌 Tecnologías usadas
Python 3.11+

Django 5.2.6

CKEditor

Bootstrap 5

SQLite (por defecto)

Whitenoise (servicio de archivos estáticos)

Pillow, psycopg2-binary, dj-database-url, gunicorn

© 2025 Proyecto experimental - Neko Cream

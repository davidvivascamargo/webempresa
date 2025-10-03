🐾 Neko Cream - Proyecto de Pruebas en Django

Proyecto experimental desarrollado con Django 5, con fines educativos y de prueba. Permite explorar la creación de aplicaciones web completas con gestión de contenido, páginas dinámicas, formulario de contacto y un panel de administración personalizado.

🌟 Características principales
🛠️ Panel de administración personalizado

Gestión de usuarios y grupos.

Gestión de contenido del blog:

Posts con títulos, imágenes, autor, fecha de publicación y categorías.

Gestión de páginas estáticas.

Administración de servicios:

Títulos, subtítulos, contenido enriquecido (CKEditor) e imágenes.

Administración de enlaces a redes sociales.

Campos de solo lectura (created, updated) y ordenamiento automático.

Búsquedas y filtros mejorados en el admin.

🎨 Frontend dinámico

Contenido cargado directamente desde el admin de Django:

Inicio, Historia, Servicios, Visítanos, Contacto, Blog.

Diseño responsivo con Bootstrap 5.

Formularios funcionales con validación, incluyendo el formulario de contacto.

Contenido enriquecido con CKEditor en servicios y posts.

⚙️ Backend

Implementado con Django 5.2.

Cada app (blog, services, pages, contact, social) tiene sus propias vistas (views.py) y rutas (urls.py).

Modelos principales:

Blog: Posts y Categorys.

Services: Productos y servicios.

Pages: Páginas personalizadas.

Social Links: Enlaces a redes sociales.

Formulario de contacto usando forms.Form y EmailMessage.

Archivos subidos (imágenes) en media/.

Archivos CSS/JS y librerías externas en static/.

Dependencias clave: django-ckeditor, pillow, psycopg2-binary, whitenoise.

👤 Experiencia de usuario

Blog con posts, categorías e imágenes.

Servicios con títulos, subtítulos, descripciones y fotografías.

Formulario de contacto con validación y confirmación de envío.

Navegación intuitiva y moderna.

🗂 Estructura del proyecto
webempresa/
├─ core/        # Plantillas y recursos estáticos
├─ services/    # Gestión de servicios
├─ blog/        # Gestión de posts y categorías
├─ pages/       # Gestión de páginas estáticas
├─ contact/     # Formulario de contacto
├─ social/      # Enlaces a redes sociales
├─ media/       # Archivos subidos
├─ staticfiles/ # Archivos estáticos recolectados
├─ manage.py
└─ requirements.txt

🚀 Instalación rápida
💾 Clonar el repositorio
git clone https://github.com/davidvivascamargo/webempresa.git
cd webempresa

🐍 Crear y activar entorno virtual
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows

📦 Instalar dependencias
pip install -r requirements.txt

🛠️ Aplicar migraciones
python manage.py migrate

🔑 Crear superusuario
python manage.py createsuperuser

🖥️ Ejecutar servidor local
python manage.py runserver


Accede a la web: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

📝 Notas importantes

Proyecto experimental; no optimizado para producción.

Todo el contenido se gestiona desde el panel de administración.

Formulario de contacto requiere configuración de correo en settings.py.

Imágenes y archivos subidos se almacenan en media/.

Estilos y scripts se cargan desde static/ y librerías externas (Bootstrap, Font Awesome).

📌 Tecnologías usadas

Python 3.11+

Django 5.2.6

CKEditor

Bootstrap 5

SQLite (por defecto)

Whitenoise

Pillow, psycopg2-binary, dj-database-url, gunicorn


# WebEmpresa - Proyecto Django

Proyecto desarrollado con Django 5, JavaScript y Python. Incluye funcionalidades de registro, login, gestión de noticias, películas y reseñas, así como un panel de administración.

---
# Vista de la Página

## 🏠 Inicio
![Inicio](capturas/view_home.png)

## 🏛️ Historia
![Historia](capturas/view_historia_empresa.png)

## 🛠️ Servicios
![Servicios](capturas/view_servicios.png)

## 📍 Visítanos
![Visítanos](capturas/view_visitarnos_mapa.png)

## ✉️ Contacto
![Contacto](capturas/view_contacto.png)

## 📰 Blog
![Blog](capturas/view_blog.png)
![Página 2](capturas/blog_pagina_2.png)

## ⚖️ Aviso Legal
![Aviso Legal](capturas/view_aviso_legal.png)

## 🍪 Cookies
![Cookies](capturas/view_cookies.png)

## 🔒 Política de Privacidad
![Política de Privacidad](capturas/view_politica_privacidad.png)


---

# Panel de Administración

## 👥 Usuarios
![Usuarios](capturas/admin_usuarios.png)

## 🔗 Redes Sociales
![Asignación de red social](capturas/admin_asignacion_red_social.png)
![Links redes sociales](capturas/admin_links_redes_sociales.png)

## 👨‍👩‍👧‍👦 Grupos
![Clasificación de grupos](capturas/admin_clasificacion_grupos.png)
![Ejemplo creación grupo](capturas/admin_ejemplo_creacion_grupo.png)
![Asignación grupo usuario](capturas/admin_asignacion_grupo_usuario.png)

## 📝 Publicaciones
![Creación post (Full)](capturas/admin_creacion_post_full.png)
![Creación post (2)](capturas/admin_creacion_post_2.png)

## 🗂️ Categorías
![Crear categoría blog](capturas/admin_crear_categoria_blog.png)
![Creación categoría](capturas/admin_creacion_categoria.png)

## 🛠️ Servicios
![Servicios](capturas/admin_servicios.png)
![Creación servicio](capturas/admin_creacion_servicio.png)

## ⚖️ Páginas Legales
![Aviso Legal](capturas/admin_aviso_legal.png)
![Editar aviso legal](capturas/admin_editar_aviso_legal.png)
![Editar cookies](capturas/admin_editar_cookies.png)
![Editar política de privacidad](capturas/admin_editar_politica_privacidad.png)

## 📄 Gestor de Páginas
![Page Manager](capturas/admin_page_manager.png)
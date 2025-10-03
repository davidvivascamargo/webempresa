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

---

IMPORTANTE!:

✉️ Formulario de Contacto

La sección de Contacto permite que los usuarios envíen mensajes directamente desde la página web.

Configuración de correo en Django:

# Email config
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '0123a6c92e0bb7'
EMAIL_HOST_PASSWORD = '78bde6eca44b3a'
EMAIL_PORT = '2525'


Flujo de envío:

El usuario completa el formulario de contacto en la web.

Django envía el correo usando la configuración de Mailtrap.

Todos los mensajes quedan capturados en Mailtrap para pruebas y revisión.

Visualización de los mensajes:

Los mensajes enviados pueden revisarse en el inbox de Mailtrap:
https://mailtrap.io/inboxes/4039666/messages

---
 
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
*Vista de gestión de usuarios en el panel de administración.*

## 🔗 Redes Sociales
![Asignación de red social](capturas/admin_asignacion_red_social.png)  
*Formulario para asignar redes sociales a la página.*

--

![Links redes sociales](capturas/admin_links_redes_sociales.png)  
*Listado y edición de links de redes sociales.*

## 👨‍👩‍👧‍👦 Grupos
![Clasificación de grupos](capturas/admin_clasificacion_grupos.png)  
*Vista de clasificación de grupos de usuarios.*

--

![Ejemplo creación grupo](capturas/admin_ejemplo_creacion_grupo.png)  
*Ejemplo práctico de creación de un grupo con privilegios.*

--

![Asignación grupo usuario](capturas/admin_asignacion_grupo_usuario.png)  
*Asignación de un grupo a un usuario específico.*

## 📝 Publicaciones
![Creación post (Full)](capturas/admin_creacion_post_full.png)  
*Pantalla completa para crear una publicación.*

--

![Creación post (2)](capturas/admin_creacion_post_2.png)  
*Segunda vista de la creación de publicaciones.*

## 🗂️ Categorías
![Crear categoría blog](capturas/admin_crear_categoria_blog.png)  
*Formulario para crear categorías en el blog.*

--

![Creación categoría](capturas/admin_creacion_categoria.png)  
*Ejemplo de creación de una categoría.*

## 🛠️ Servicios
![Servicios](capturas/admin_servicios.png)  
*Listado de servicios disponibles.*

--

![Creación servicio](capturas/admin_creacion_servicio.png)  
*Formulario para la creación de un servicio.*

## ⚖️ Páginas Legales
![Aviso Legal](capturas/admin_aviso_legal.png)  
*Vista del aviso legal en el panel.*

--

![Editar aviso legal](capturas/admin_editar_aviso_legal.png)  
*Edición del aviso legal.*

--

![Editar cookies](capturas/admin_editar_cookies.png)  
*Pantalla de edición de cookies.*

--

![Editar política de privacidad](capturas/admin_editar_politica_privacidad.png)  
*Pantalla de edición de política de privacidad.*

## 📄 Gestor de Páginas
![Page Manager](capturas/admin_page_manager.png)  
*Gestor de páginas del panel de administración.*

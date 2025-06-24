# Sistema de Gestión Veterinaria

Este es un sistema web básico para la gestión de mascotas, propietarios y consultas veterinarias, desarrollado con Django.

## Requisitos

- Python 3.8 o superior
- Django 4.2 o superior
- (Opcional) djangorestframework, psycopg2-binary, django-cors-headers

## Instalación

1. **Clona el repositorio y entra a la carpeta del proyecto:**

   ```bash
   git clone <URL-del-repositorio>
   cd veterinary_management
   ```

2. **Crea y activa un entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # En Windows
   # source venv/bin/activate   # En Linux/Mac
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuración de la base de datos

Por defecto, el proyecto utiliza SQLite, por lo que no necesitas configuración adicional para pruebas locales.

## Migraciones iniciales

Ejecuta los siguientes comandos para crear las tablas en la base de datos:

```bash
python gestionar.py makemigrations
python gestionar.py migrate
```

## Crear superusuario

Para acceder al panel de administración de Django, crea un superusuario:

```bash
python gestionar.py createsuperuser
```

Sigue las instrucciones en pantalla para definir usuario y contraseña.

## Ejecutar la aplicación

Inicia el servidor de desarrollo con:

```bash
python gestionar.py runserver
```

Accede a la aplicación en [http://localhost:8000/](http://localhost:8000/)  
El panel de administración está en [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Funcionalidades

- Registrar y listar mascotas, propietarios y consultas veterinarias.
- Listar los servicios disponibles.

---

**Nota:** Si deseas usar otra base de datos (como PostgreSQL), actualiza la configuración en `settings.py` y asegúrate de instalar el driver correspondiente (`psycopg2-binary`).

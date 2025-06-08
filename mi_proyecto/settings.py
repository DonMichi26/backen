"""
Archivo de configuración principal para el proyecto Django 'mi_proyecto'.
Contiene todas las configuraciones necesarias para el funcionamiento del proyecto,
como seguridad, aplicaciones instaladas, base de datos, internacionalización, etc.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# =========================
# Rutas base del proyecto
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# Seguridad
# =========================
# ¡IMPORTANTE! Cambia esta clave en producción y mantenla en secreto
SECRET_KEY = os.getenv('SECRET_KEY')

# Activa el modo debug solo en desarrollo
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Lista de hosts permitidos para el despliegue
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',') if not DEBUG else []

# =========================
# Aplicaciones instaladas
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',           # Panel de administración de Django
    'django.contrib.auth',            # Sistema de autenticación
    'django.contrib.contenttypes',    # Tipos de contenido
    'django.contrib.sessions',        # Manejo de sesiones
    'django.contrib.messages',        # Mensajes entre vistas
    'django.contrib.staticfiles',     # Archivos estáticos (CSS, JS, imágenes)
    'rest_framework',                 # Django REST Framework para APIs
    'autenticacion',                  # Nuestra app personalizada de autenticación
    'corsheaders',                    # Permitir peticiones CORS desde el frontend
]

# =========================
# Middleware
# =========================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',                      # Middleware para CORS (debe ir al inicio)
    'django.middleware.security.SecurityMiddleware',            # Seguridad
    'django.contrib.sessions.middleware.SessionMiddleware',     # Manejo de sesiones
    'django.middleware.common.CommonMiddleware',                # Funcionalidades comunes
    'django.middleware.csrf.CsrfViewMiddleware',                # Protección CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Autenticación
    'django.contrib.messages.middleware.MessageMiddleware',     # Mensajes
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   # Protección contra clickjacking
]

# =========================
# Configuración de URLs
# =========================
ROOT_URLCONF = 'mi_proyecto.urls'

# =========================
# Plantillas (Templates)
# =========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Directorios adicionales para plantillas
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# =========================
# WSGI
# =========================
WSGI_APPLICATION = 'mi_proyecto.wsgi.application'

# =========================
# Base de datos
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Motor de base de datos
        'NAME': BASE_DIR / 'db.sqlite3',         # Nombre del archivo de la base de datos
    }
}

# =========================
# Validación de contraseñas
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# =========================
# Internacionalización
# =========================
LANGUAGE_CODE = 'es-es'  # Idioma en español
TIME_ZONE = 'UTC'        # Zona horaria
USE_I18N = True          # Habilita la internacionalización
USE_TZ = True            # Habilita el uso de zonas horarias

# =========================
# Archivos estáticos
# =========================
STATIC_URL = 'static/'

# =========================
# Configuración por defecto para claves primarias
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =========================
# Configuración de Django REST Framework y JWT
# =========================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# =========================
# Configuración de CORS
# =========================
CORS_ALLOW_ALL_ORIGINS = DEBUG  # Solo permite todos los orígenes en desarrollo

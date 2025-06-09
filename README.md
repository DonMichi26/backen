# Sistema de Autenticación JWT con Django

Este proyecto implementa un sistema de autenticación usando JWT (JSON Web Tokens) con Django y Django REST Framework.

## Características

- Autenticación basada en JWT
- Endpoints protegidos
- Sistema de registro de usuarios
- Frontend simple para pruebas
- Integración con MySQL
- Manejo de CORS


. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

. Instalar dependencias:
```bash
pip install -r requirements.txt
```

. Configurar la base de datos:
- Crear una base de datos MySQL llamada 'backend'
- Configurar las credenciales en `mi_proyecto/settings.py`

. Aplicar migraciones:
```bash
python manage.py migrate
```

. Crear superusuario:
```bash
python manage.py createsuperuser
```

## Uso

1. Iniciar el servidor:
```bash
python manage.py runserver
```

2. Acceder a los endpoints:
- Panel de administración: http://127.0.0.1:8000/admin/
- API de autenticación: http://127.0.0.1:8000/api/v1/login/
- API de autenticación JSON: http://127.0.0.1:8000/api/v1/login-json/
- Endpoint protegido: http://127.0.0.1:8000/api/v1/protegido/

## Estructura del Proyecto

```
backend/
├── mi_proyecto/           # Configuración principal de Django
├── autenticacion/         # Aplicación de autenticación
│   ├── views.py          # Vistas de la API
│   ├── urls.py           # Rutas de la API
│   └── usuarios.json     # Almacenamiento de usuarios
├── static/               # Archivos estáticos
├── templates/            # Plantillas HTML
├── manage.py            # Script de administración
└── requirements.txt     # Dependencias
```

## Endpoints de la API

### Autenticación

- `POST /api/v1/login/`
  - Autenticación JWT
  - Body: `{"username": "usuario", "password": "contraseña"}`
  - Retorna: `{"access": "token", "refresh": "token"}`

- `POST /api/v1/login-json/`
  - Autenticación simple
  - Body: `{"username": "usuario", "password": "contraseña"}`
  - Retorna: `{"access": "token", "mensaje": "Login exitoso"}`

### Registro

- `POST /api/v1/registro-json/`
  - Registro de usuarios
  - Body: `{"username": "usuario", "password": "contraseña"}`
  - Retorna: `{"mensaje": "Usuario registrado correctamente"}`

### Endpoints Protegidos

- `GET /api/v1/protegido/`
  - Requiere token JWT
  - Header: `Authorization: Bearer <token>`
  - Retorna: `{"mensaje": "¡Acceso concedido!"}`

## Desarrollo

### Frontend

El frontend incluye:
- Formulario de login
- Manejo de tokens JWT
- Acceso a endpoints protegidos
- Manejo de errores

### Backend

El backend implementa:
- Autenticación JWT
- Protección de rutas
- Validación de usuarios
- Almacenamiento seguro de contraseñas

## Seguridad

- Tokens JWT con tiempo de expiración
- Protección CSRF
- Validación de contraseñas
- Headers de seguridad
- CORS configurado




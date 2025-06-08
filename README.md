# Proyecto de Autenticación JWT con Django

## 📋 Descripción
Este proyecto implementa un sistema de autenticación utilizando JWT (JSON Web Tokens) con Django en el backend y una interfaz web simple en el frontend.

## 🚀 Características
- Autenticación basada en JWT
- Endpoints protegidos
- Interfaz de usuario simple y responsive
- Almacenamiento seguro de tokens

## 🛠️ Tecnologías Utilizadas
- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript
- **Base de Datos**: SQLite
- **Autenticación**: JWT (JSON Web Tokens)

## 📦 Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Entorno virtual (recomendado)

### Pasos de Instalación
1. Clonar el repositorio:
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd backen
   ```

2. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```

5. Crear superusuario (opcional):
   ```bash
   python manage.py createsuperuser
   ```

## 🚀 Uso

### Iniciar el Servidor
```bash
python manage.py runserver
```

### Acceder a la Aplicación
1. Abrir `frontend.html` en el navegador
2. Iniciar sesión con las credenciales
3. Usar el token JWT para acceder a endpoints protegidos

## 📁 Estructura del Proyecto
```
backen/
├── manage.py
├── mi_proyecto/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── autenticacion/
│   ├── views.py
│   └── urls.py
├── frontend.html
└── script.js
```

## 🔒 Endpoints API
- `POST /api/v1/login-json/`: Autenticación y obtención de token
- `GET /api/v1/protegido/`: Endpoint protegido que requiere token JWT

## 👥 Contribución
1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📝 Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles.


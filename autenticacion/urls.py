from django.urls import path
from .views import PruebaProtegida, LoginJSON, RegistroJSON, VerificarDB
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # Vista para obtener el par de tokens (access y refresh)
    TokenRefreshView,     # Vista para refrescar el token de acceso
)

# Definimos las rutas URL de nuestra aplicación
urlpatterns = [
    # Ruta para obtener tokens JWT (access y refresh)
    # POST /login/ - Recibe username y password, devuelve tokens
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Ruta para refrescar el token de acceso
    # POST /refresh/ - Recibe refresh token, devuelve nuevo access token
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Ruta personalizada para login que devuelve respuesta en formato JSON
    # POST /login-json/ - Recibe credenciales, devuelve mensaje de éxito/error
    path('login-json/', LoginJSON.as_view(), name='login_json'),
    
    # Ruta para registro de nuevos usuarios
    # POST /registro-json/ - Recibe datos del usuario, crea nuevo usuario
    path('registro-json/', RegistroJSON.as_view(), name='registro_json'),
    
    # Ruta protegida que requiere autenticación
    # GET /protegido/ - Requiere token JWT válido en las cookies
    path('protegido/', PruebaProtegida.as_view(), name='prueba_protegida'),
    
    # Ruta para verificar la base de datos
    path('verificar-db/', VerificarDB.as_view(), name='verificar_db'),
] 
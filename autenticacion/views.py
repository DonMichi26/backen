"""
Vistas para el sistema de autenticación.
Este módulo contiene todas las vistas necesarias para manejar la autenticación
y los endpoints protegidos de la API.
"""

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import status
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.settings import api_settings

# Ruta al archivo JSON de usuarios
USUARIOS_JSON = os.path.join(os.path.dirname(__file__), 'usuarios.json')

def leer_usuarios():
    """
    Lee los usuarios almacenados en el archivo JSON.
    Si el archivo no existe, retorna una lista vacía.
    """
    if not os.path.exists(USUARIOS_JSON):
        return []
    with open(USUARIOS_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)

def escribir_usuarios(usuarios):
    """
    Guarda la lista de usuarios en el archivo JSON.
    """
    with open(USUARIOS_JSON, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, indent=2)

# Create your views here.

class CookieJWTAuthentication(JWTAuthentication):
    def get_header(self, request):
        header = super().get_header(request)
        if header is None:
            # Si no hay token en el header Authorization, buscar en las cookies
            access_token = request.COOKIES.get('access_token')
            if access_token:
                # Formatear como un header Authorization estándar
                return f"{api_settings.AUTH_HEADER_TYPES[0]} {access_token}".encode('utf-8')
        return header

    def get_raw_token(self, header):
        # Sobreescribir para manejar el token que viene de la cookie sin el prefijo 'Bearer '
        parts = header.split()
        if parts[0] == api_settings.AUTH_HEADER_TYPES[0].encode():
            return parts[1]
        return super().get_raw_token(header)

# Vista protegida que solo permite el acceso a usuarios autenticados con un token válido
class PruebaProtegida(APIView):
    """
    Vista de prueba que requiere autenticación.
    Solo permite el acceso a usuarios autenticados con un token válido.
    """
    # Solo usuarios autenticados pueden acceder a esta vista
    authentication_classes = [CookieJWTAuthentication] # Usar nuestra clase personalizada
    permission_classes = [IsAuthenticated]

    # Método GET que retorna un mensaje si el usuario tiene un token válido
    def get(self, request):
        """
        Maneja las peticiones GET a la ruta protegida.
        Verifica el token de autenticación en el header.
        """
        return Response({"mensaje": f"¡Acceso concedido al usuario {request.user.username} con token válido!"})

@method_decorator(csrf_exempt, name='dispatch')
class LoginJSON(APIView):
    authentication_classes = [] # No requiere autenticación
    permission_classes = []   # Permite acceso a cualquiera
    """
    Vista para el login usando autenticación basada en JSON.
    Permite a los usuarios iniciar sesión y obtener un token.
    """
    def post(self, request):
        """
        Maneja las peticiones POST para el login.
        Verifica las credenciales y retorna un token si son válidas.
        """
        data = request.data
        print(f"Datos recibidos en LoginJSON: {data}")
        username = data.get('username')
        password = data.get('password')
        print(f"Username: {username}, Password: {password}")
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            response = Response({'mensaje': 'Login exitoso'}, status=status.HTTP_200_OK)
            response.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                samesite='Lax',
                secure=not settings.DEBUG,
                max_age=60*60
            )
            return response
        return Response({'mensaje': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)

@method_decorator(csrf_exempt, name='dispatch')
class RegistroJSON(APIView):
    """
    Vista para el registro de nuevos usuarios.
    Permite crear nuevas cuentas de usuario.
    """
    def post(self, request):
        """
        Maneja las peticiones POST para el registro.
        Crea un nuevo usuario si no existe.
        """
        data = request.data
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return Response({'mensaje': 'Usuario y contraseña requeridos'}, status=status.HTTP_400_BAD_REQUEST)
        usuarios = leer_usuarios()
        if any(user['username'] == username for user in usuarios):
            return Response({'mensaje': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)
        usuarios.append({'username': username, 'password': password})
        escribir_usuarios(usuarios)
        return Response({'mensaje': 'Usuario registrado correctamente'}, status=status.HTTP_201_CREATED)

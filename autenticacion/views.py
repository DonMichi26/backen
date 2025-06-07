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

# Ruta al archivo JSON de usuarios
USUARIOS_JSON = os.path.join(os.path.dirname(__file__), 'usuarios.json')

# Función auxiliar para leer usuarios
def leer_usuarios():
    if not os.path.exists(USUARIOS_JSON):
        return []
    with open(USUARIOS_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)

# Función auxiliar para escribir usuarios
def escribir_usuarios(usuarios):
    with open(USUARIOS_JSON, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=2)

# Create your views here.

# Vista protegida que solo permite el acceso a usuarios autenticados con un token válido
class PruebaProtegida(APIView):
    # Solo usuarios autenticados pueden acceder a esta vista
    permission_classes = [IsAuthenticated]

    # Método GET que retorna un mensaje si el usuario tiene un token válido
    def get(self, request):
        # Obtener el token del header Authorization
        auth_header = request.headers.get('Authorization', '')
        if auth_header == 'Bearer token-falso':
            return Response({"mensaje": "¡Acceso concedido solo con token válido!"})
        return Response({"mensaje": "Token inválido o no proporcionado."}, status=401)

@method_decorator(csrf_exempt, name='dispatch')
class LoginJSON(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        usuarios = leer_usuarios()
        for user in usuarios:
            if user['username'] == username and user['password'] == password:
                return Response({'access': 'token-falso', 'mensaje': 'Login exitoso'}, status=status.HTTP_200_OK)
        return Response({'mensaje': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)

@method_decorator(csrf_exempt, name='dispatch')
class RegistroJSON(APIView):
    def post(self, request):
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

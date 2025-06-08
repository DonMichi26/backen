// Variable global para almacenar el token de acceso JWT
let accessToken = localStorage.getItem('accessToken') || '';

// Configuración de la API
const API_BASE_URL = 'http://localhost:8000/api/v1';

// Función para mostrar mensajes de respuesta
function mostrarMensaje(mensaje, tipo = 'info') {
    const respuesta = document.getElementById('respuesta');
    respuesta.textContent = mensaje;
    respuesta.className = 'respuesta ' + tipo;
}

// Función para manejar errores de red
function manejarError(error) {
    console.error('Error:', error);
    mostrarMensaje('Error: ' + error.message, 'error');
}

// Función para iniciar sesión y obtener el token JWT
async function login() {
    try {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        if (!username || !password) {
            mostrarMensaje('Por favor, completa todos los campos', 'error');
            return;
        }

        const response = await fetch(`${API_BASE_URL}/login-json/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password })
        });

        if (!response.ok) {
            throw new Error(`Error HTTP: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        console.log('Respuesta del servidor:', data);

        if (data.access) {
            accessToken = data.access;
            localStorage.setItem('accessToken', accessToken);
            mostrarMensaje('Login exitoso. Token guardado.', 'success');
        } else {
            mostrarMensaje('Error en login: ' + (data.detail || JSON.stringify(data)), 'error');
        }
    } catch (error) {
        manejarError(error);
    }
}

// Función para acceder a un endpoint protegido usando el token JWT
async function accederProtegido() {
    try {
        if (!accessToken) {
            mostrarMensaje('Primero debes iniciar sesión para obtener el token.', 'error');
            return;
        }

        const response = await fetch(`${API_BASE_URL}/protegido/`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        });

        if (!response.ok) {
            if (response.status === 401) {
                accessToken = '';
                localStorage.removeItem('accessToken');
                mostrarMensaje('Sesión expirada. Por favor, inicia sesión nuevamente.', 'error');
                return;
            }
            throw new Error(`Error HTTP: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        mostrarMensaje('Respuesta del backend: ' + JSON.stringify(data), 'success');
    } catch (error) {
        manejarError(error);
    }
}

// Función para cerrar sesión
function logout() {
    accessToken = '';
    localStorage.removeItem('accessToken');
    mostrarMensaje('Sesión cerrada correctamente', 'success');
    document.getElementById('username').value = '';
    document.getElementById('password').value = '';
}

// Verificar el estado del token al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    if (accessToken) {
        mostrarMensaje('Sesión activa. Token disponible.', 'success');
    }
}); 
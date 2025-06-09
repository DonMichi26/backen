/**
 * Sistema de Autenticación JWT - Frontend
 * Este archivo maneja toda la lógica del cliente para la autenticación JWT
 * y la interacción con el backend de Django.
 */

// Variable global para almacenar el token de acceso JWT
// Se recupera del localStorage si existe, o se inicializa vacío
// Eliminado ya que el token se gestiona por cookies HTTP-only
// let accessToken = localStorage.getItem('accessToken') || '';

// URL base de la API - Punto de entrada para todas las peticiones al backend
const API_BASE_URL = 'http://localhost:8000/api/v1';

/**
 * Función para mostrar mensajes de respuesta al usuario
 * @param {string} mensaje - El mensaje a mostrar
 * @param {string} tipo - El tipo de mensaje ('info', 'error', 'success')
 */
function mostrarMensaje(mensaje, tipo = 'info') {
    const respuesta = document.getElementById('respuesta');
    respuesta.textContent = mensaje;
    respuesta.className = 'respuesta ' + tipo;
}

/**
 * Función para manejar errores de red y mostrar mensajes al usuario
 * @param {Error} error - El objeto de error capturado
 */
function manejarError(error) {
    console.error('Error:', error);
    mostrarMensaje('Error: ' + error.message, 'error');
}

/**
 * Función para iniciar sesión y obtener el token JWT
 * Realiza una petición POST al endpoint de login y almacena el token
 */
async function login() {
    try {
        // Obtener valores del formulario
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Validar que los campos no estén vacíos
        if (!username || !password) {
            mostrarMensaje('Por favor, completa todos los campos', 'error');
            return;
        }

        // Realizar petición al backend
        const response = await fetch(`${API_BASE_URL}/login-json/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
            credentials: 'include' // IMPORTANTE: Incluir cookies en la petición cross-origin
        });

        // Verificar si la respuesta fue exitosa
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`Error HTTP: ${response.status} - ${errorData.mensaje || response.statusText}`);
        }

        // Procesar la respuesta
        // const data = await response.json(); // Ya no esperamos un 'access' token en el body
        // console.log('Respuesta del servidor:', data);

        // Si se recibió un token, guardarlo (ya no es necesario, se gestiona por cookie)
        // if (data.access) {
        //     accessToken = data.access;
        //     localStorage.setItem('accessToken', accessToken);
        //     mostrarMensaje('Login exitoso. Token guardado.', 'success');
        // } else {
        //     mostrarMensaje('Error en login: ' + (data.detail || JSON.stringify(data)), 'error');
        // }
        mostrarMensaje('Login exitoso.', 'success'); // Simplemente indicamos éxito

    } catch (error) {
        manejarError(error);
    }
}

/**
 * Función para acceder a un endpoint protegido usando el token JWT
 * Demuestra cómo usar el token para acceder a recursos protegidos
 */
async function accederProtegido() {
    try {
        // No es necesario verificar accessToken aquí, la cookie se envía automáticamente
        // if (!accessToken) {
        //     mostrarMensaje('Primero debes iniciar sesión para obtener el token.', 'error');
        //     return;
        // }

        // Realizar petición al endpoint protegido
        const response = await fetch(`${API_BASE_URL}/protegido/`, {
            method: 'GET',
            // Ya no es necesario enviar el Authorization header manualmente
            // headers: {
            //     'Authorization': `Bearer ${accessToken}`
            // },
            credentials: 'include' // IMPORTANTE: Incluir cookies en la petición cross-origin
        });

        // Manejar diferentes casos de respuesta
        if (!response.ok) {
            if (response.status === 401) {
                // Si el token expiró o es inválido, no manipulamos localStorage
                mostrarMensaje('Sesión expirada o token inválido. Por favor, inicia sesión nuevamente.', 'error');
                return;
            }
            throw new Error(`Error HTTP: ${response.status} ${response.statusText}`);
        }

        // Mostrar la respuesta exitosa
        const data = await response.json();
        mostrarMensaje('Respuesta del backend: ' + JSON.stringify(data), 'success');
    } catch (error) {
        manejarError(error);
    }
}

/**
 * Función para cerrar sesión
 * Limpia el token y los campos del formulario
 */
function logout() {
    // No es necesario limpiar localStorage, la cookie es HTTP-only y se limpia en el backend
    // accessToken = '';
    // localStorage.removeItem('accessToken');
    mostrarMensaje('Sesión cerrada correctamente', 'success');
    document.getElementById('username').value = '';
    document.getElementById('password').value = '';
    // Opcional: Si quieres forzar la eliminación de la cookie (solo si no es HttpOnly)
    // document.cookie = 'access_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
}

// Verificar el estado del token al cargar la página (ahora se basa en la cookie)
document.addEventListener('DOMContentLoaded', () => {
    // No es necesario verificar accessToken aquí, ya que se basa en la cookie
    // if (accessToken) {
    //     mostrarMensaje('Sesión activa. Token disponible.', 'success');
    // }
}); 
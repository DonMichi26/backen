// Variable global para almacenar el token de acceso JWT
let accessToken = '';

// Función para iniciar sesión y obtener el token JWT
function login() {
    // Obtiene los valores ingresados por el usuario
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Realiza una petición POST al endpoint de login
    fetch('http://localhost:8000/api/v1/login-json/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    })
    .then(res => {
        // Verifica si la respuesta es exitosa
        if (!res.ok) {
            throw new Error('Error HTTP: ' + res.status + ' ' + res.statusText);
        }
        return res.json();
    })
    .then(data => {
        console.log(data); // Muestra la respuesta en consola para depuración
        if (data.access) {
            // Si se recibe un token, lo guarda en localStorage y actualiza la variable global
            localStorage.setItem('accessToken', data.access);
            accessToken = localStorage.getItem('accessToken');
            document.getElementById('respuesta').innerText = 'Login exitoso. Token guardado.';
        } else {
            // Si no se recibe un token, muestra un mensaje de error
            document.getElementById('respuesta').innerText = 'Error en login: ' + (data.detail || JSON.stringify(data));
        }
    })
    .catch(err => {
        // Captura y muestra errores de red o CORS
        document.getElementById('respuesta').innerText = 'Error de red o CORS: ' + err;
    });
}

// Función para acceder a un endpoint protegido usando el token JWT
function accederProtegido() {
    // Verifica si el token existe
    if (!accessToken) {
        document.getElementById('respuesta').innerText = 'Primero haz login para obtener el token.';
        return;
    }

    // Realiza una petición GET al endpoint protegido
    fetch('http://localhost:8000/api/v1/protegido/', {
        method: 'GET',
        headers: { 'Authorization': 'Bearer ' + accessToken }
    })
    .then(res => res.json())
    .then(data => {
        // Muestra la respuesta del backend
        document.getElementById('respuesta').innerText = 'Respuesta del backend: ' + JSON.stringify(data);
    })
    .catch(err => {
        // Captura y muestra errores de red
        document.getElementById('respuesta').innerText = 'Error de red: ' + err;
    });
} 
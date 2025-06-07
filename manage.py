#!/usr/bin/env python
""" 
Archivo de utilidad para administrar tareas del proyecto Django.
Este archivo permite ejecutar comandos como iniciar el servidor, aplicar migraciones, crear usuarios, etc.
"""

import os
import sys

def main():
    """Punto de entrada principal para ejecutar comandos de Django."""
    # Establece la configuración predeterminada del proyecto Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
    try:
        # Importa la función de ejecución de comandos de Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si Django no está instalado, muestra un mensaje de error
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y disponible en tu entorno virtual?"
        ) from exc
    # Ejecuta el comando recibido por línea de comandos
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

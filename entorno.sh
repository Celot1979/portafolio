#!/bin/bash

# IMPORTANTE: Este script DEBE ser ejecutado con 'source' para que los cambios de entorno
# se apliquen a tu terminal actual. Ejemplo: source ./configurar_entorno.sh

echo "--- Iniciando configuración de entorno ---"

# 1. Intentar desactivar cualquier entorno de Conda activo en el shell actual
echo "Intentando desactivar cualquier entorno de Conda activo..."

# Primero, verificamos si 'conda' está disponible como comando en este shell
if command -v conda &> /dev/null; then
    # Si 'conda' está disponible, verificamos si hay un entorno activo ($CONDA_PREFIX)
    if [[ -n "$CONDA_PREFIX" ]]; then
        conda deactivate
        echo "Entorno de Conda desactivado."
    else
        echo "No hay un entorno de Conda activo para desactivar."
    fi
else
    echo "El comando 'conda' no se encontró o no está inicializado en este shell."
    echo "Asegúrate de haber ejecutado 'conda init <TU_SHELL>' y reiniciado tu terminal."
    # No es un error crítico si no hay conda, el script puede continuar si es posible.
fi

# 2. Ir a la ruta específica y ejecutar 'source ./activate'
# Define la ruta a tu directorio 'bin'
TARGET_DIR="/Users/danielgil/Documents/portafolio_mio/portafolio/trabajo/bin"

echo "Cambiando al directorio: $TARGET_DIR"

# Verifica si el directorio existe
if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: El directorio '$TARGET_DIR' no existe. No se puede continuar."
    return 1 # Devuelve un código de error y sale del script (importante para 'source')
fi

# Cambia al directorio; si falla, imprime un error y sale
cd "$TARGET_DIR" || { echo "Error: No se pudo cambiar al directorio '$TARGET_DIR'."; return 1; }

echo "Ejecutando source ./activate en $TARGET_DIR..."

# Verifica si el archivo 'activate' existe en el directorio actual
if [ -f "./activate" ]; then
    source "./activate" # ¡Este es el comando clave que activa el entorno en tu terminal!
    echo "Comando source ./activate ejecutado exitosamente."
else
    echo "Error: El archivo './activate' no se encontró en el directorio '$TARGET_DIR'."
    return 1 # Devuelve un código de error y sale
fi

echo "--- Configuración de entorno finalizada ---"

# Si necesitas ejecutar algún script de Python DESPUÉS de que el entorno esté activado
# en tu terminal, puedes añadirlo aquí. Por ejemplo:
# python /ruta/a/tu_script_principal.py
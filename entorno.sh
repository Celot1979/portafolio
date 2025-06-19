#!/bin/bash

# Ruta al directorio base de tu proyecto
PROJECT_ROOT="/Users/danielgil/Desktop/portafolio"

# Ruta al script de activación de tu entorno virtual
VENV_ACTIVATE_SCRIPT="${PROJECT_ROOT}/trabajo2/bin/activate"

# 1. Activar el entorno virtual
echo "Activando entorno virtual..."
if [ -f "$VENV_ACTIVATE_SCRIPT" ]; then
    source "$VENV_ACTIVATE_SCRIPT"
    echo "Entorno virtual 'trabajo2' activado."
else
    echo "Error: El script de activación del entorno virtual no se encontró en: $VENV_ACTIVATE_SCRIPT"
    echo "Por favor, verifica la ruta o asegúrate de que el entorno virtual 'trabajo2' existe."
    exit 1 # Salir con error
fi

# 2. Navegar al directorio del proyecto
echo "Navegando a la ruta del proyecto: $PROJECT_ROOT"
if [ -d "$PROJECT_ROOT" ]; then
    cd "$PROJECT_ROOT"
    echo "¡Listo! Estás en la carpeta del proyecto."
else
    echo "Error: El directorio del proyecto no se encontró en: $PROJECT_ROOT"
    exit 1 # Salir con error
fi

# 3. Ejecutar test_BBDD.py y verificar su resultado
echo "Ejecutando test_BBDD.py..."
if python "${PROJECT_ROOT}/test_BBDD.py"; then
    echo "✅ test_BBDD.py se ejecutó correctamente"
    
    # 4. Preguntar si se quiere ejecutar reflex run solo si test_BBDD.py fue exitoso
    echo -n "¿Quieres ejecutar el comando 'reflex run' ahora? (s/n): "
    read REPLY

    echo # Imprime una nueva línea para una mejor presentación

    if [[ "$REPLY" == "s" || "$REPLY" == "S" ]]
    then
        echo "Ejecutando 'reflex run'..."
        reflex run
    else
        echo "No se ejecutó 'reflex run'. Puedes hacerlo manualmente cuando quieras."
    fi
else
    echo "❌ test_BBDD.py falló. Por favor, corrige los errores antes de continuar."
    exit 1
fi

# El script terminará aquí, dejándote en la terminal dentro de la carpeta del proyecto
# con el entorno virtual activado, independientemente de si elegiste ejecutar 'reflex run'.
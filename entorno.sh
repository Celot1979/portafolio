#!/bin/bash

# Ruta al directorio base de tu proyecto
PROJECT_ROOT="/Users/danielgil/Documents/portafolio_mio/portafolio"

# Ruta al script de activación de tu entorno virtual
VENV_ACTIVATE_SCRIPT="${PROJECT_ROOT}/trabajo/bin/activate"

# 1. Activar el entorno virtual
echo "Activando entorno virtual..."
if [ -f "$VENV_ACTIVATE_SCRIPT" ]; then
    source "$VENV_ACTIVATE_SCRIPT"
    echo "Entorno virtual 'trabajo' activado."
else
    echo "Error: El script de activación del entorno virtual no se encontró en: $VENV_ACTIVATE_SCRIPT"
    echo "Por favor, verifica la ruta o asegúrate de que el entorno virtual 'trabajo' existe."
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

# 3. Preguntar si se quiere ejecutar reflex run (Lógica Mejorada)
# Usamos 'echo' para el prompt y 'read' sin opciones problemáticas.
echo -n "¿Quieres ejecutar el comando 'reflex run' ahora? (s/n): "
read REPLY

echo # Imprime una nueva línea para una mejor presentación

# La comprobación [[ $REPLY =~ ^[Ss]$ ]] es específica de Bash/Zsh.
# Una alternativa más universal es [ "$REPLY" = "s" ] || [ "$REPLY" = "S" ]
if [[ "$REPLY" == "s" || "$REPLY" == "S" ]]
then
    echo "Ejecutando 'reflex run'..."
    reflex run
else
    echo "No se ejecutó 'reflex run'. Puedes hacerlo manualmente cuando quieras."
fi

# El script terminará aquí, dejándote en la terminal dentro de la carpeta del proyecto
# con el entorno virtual activado, independientemente de si elegiste ejecutar 'reflex run'.
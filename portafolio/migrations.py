"""Script para manejar las migraciones de la base de datos."""

import os
import subprocess
from pathlib import Path

def run_migrations():
    """Ejecuta las migraciones de la base de datos."""
    # Obtener el directorio actual
    current_dir = Path(__file__).parent.parent

    # Ejecutar las migraciones
    try:
        # Crear la primera migración si no existe
        if not (current_dir / "alembic" / "versions").exists():
            subprocess.run(["alembic", "revision", "--autogenerate", "-m", "initial"], check=True)
        
        # Aplicar las migraciones
        subprocess.run(["alembic", "upgrade", "head"], check=True)
        print("Migraciones aplicadas correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar las migraciones: {e}")
        raise

if __name__ == "__main__":
    run_migrations() 
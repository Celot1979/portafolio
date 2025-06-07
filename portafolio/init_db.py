"""Script para inicializar la base de datos."""

from database import engine
from models import Base

def init_db():
    """Inicializa la base de datos creando todas las tablas."""
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Base de datos inicializada correctamente.") 
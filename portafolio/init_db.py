"""Script para inicializar la base de datos."""

from .database import engine, SessionLocal
from .models import Base, User

def init_db():
    """Inicializa la base de datos creando todas las tablas y un usuario administrador."""
    # Crear todas las tablas
    Base.metadata.create_all(bind=engine)
    
    # Crear sesión de base de datos
    db = SessionLocal()
    
    try:
        # Verificar si ya existe un usuario administrador
        admin = db.query(User).filter(User.username == "dani").first()
        if not admin:
            # Crear usuario administrador
            admin = User(username="dani")
            admin.set_password("Will2024_")  # Cambiar esto en producción
            db.add(admin)
            db.commit()
            print("Usuario administrador creado correctamente")
        else:
            print("El usuario administrador ya existe")
    except Exception as e:
        print(f"Error al crear el usuario administrador: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db() 
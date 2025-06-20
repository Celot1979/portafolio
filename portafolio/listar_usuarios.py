"""Script para listar todos los usuarios en la base de datos."""

from .database import SessionLocal
from .models import User

def listar_usuarios():
    db = SessionLocal()
    try:
        usuarios = db.query(User).all()
        if not usuarios:
            print("No hay usuarios en la base de datos.")
        else:
            print("Usuarios en la base de datos:")
            for usuario in usuarios:
                print(f"ID: {usuario.id}, Username: {usuario.username}")
    finally:
        db.close()

if __name__ == "__main__":
    listar_usuarios() 
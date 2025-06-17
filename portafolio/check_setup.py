"""Script para verificar la configuración del sistema."""

import sys
import psycopg2
from sqlalchemy import inspect
from .database import engine, SessionLocal
from .models import Base, User, Repository, BlogPost

def check_database_connection():
    """Verifica la conexión a la base de datos."""
    try:
        conn = psycopg2.connect(
            dbname="portafolio",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        conn.close()
        print("✅ Conexión a la base de datos exitosa")
        return True
    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {str(e)}")
        return False

def check_tables():
    """Verifica que todas las tablas existan."""
    inspector = inspect(engine)
    required_tables = ["users", "repositories", "blog_posts"]
    existing_tables = inspector.get_table_names()
    
    all_tables_exist = True
    for table in required_tables:
        if table not in existing_tables:
            print(f"❌ La tabla {table} no existe")
            all_tables_exist = False
        else:
            print(f"✅ La tabla {table} existe")
    
    return all_tables_exist

def check_admin_user():
    """Verifica que exista el usuario administrador."""
    db = SessionLocal()
    try:
        admin = db.query(User).filter(User.username == "admin").first()
        if admin:
            print("✅ Usuario administrador existe")
            return True
        else:
            print("❌ Usuario administrador no existe")
            return False
    finally:
        db.close()

def main():
    """Función principal de verificación."""
    print("🔍 Iniciando verificación del sistema...")
    
    # Verificar conexión a la base de datos
    if not check_database_connection():
        print("\n❌ La verificación ha fallado. Por favor, asegúrate de que:")
        print("1. PostgreSQL está instalado y corriendo")
        print("2. La base de datos 'portafolio' existe")
        print("3. Las credenciales son correctas")
        sys.exit(1)
    
    # Verificar tablas
    if not check_tables():
        print("\n❌ Faltan algunas tablas. Ejecuta:")
        print("python -m portafolio.init_db")
        sys.exit(1)
    
    # Verificar usuario administrador
    if not check_admin_user():
        print("\n❌ No existe el usuario administrador. Ejecuta:")
        print("python -m portafolio.init_db")
        sys.exit(1)
    
    print("\n✅ Todo está configurado correctamente. Puedes ejecutar:")
    print("reflex run")

if __name__ == "__main__":
    main() 
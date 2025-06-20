"""Script para verificar la configuración del sistema."""

import sys
import psycopg2
import os
from sqlalchemy import inspect
from portafolio.database import engine, SessionLocal
from portafolio.models import Base, User, Repository, BlogPost

def check_database_connection():
    """Verifica la conexión a la base de datos."""
    try:
        # Usar DATABASE_URL si está definida, si no, usar los datos de Supabase directamente
        db_url = os.getenv("DATABASE_URL")
        if db_url:
            conn = psycopg2.connect(db_url)
        else:
            conn = psycopg2.connect(
                dbname="neondb",
                user="neondb_owner",
                password="npg_6kmlf9TxJNhX",
                host="ep-silent-cloud-ab3kdk6l-pooler.eu-west-2.aws.neon.tech",
                port="5432",
                sslmode="require"
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
        usuarios = db.query(User).all()
        print("Usuarios encontrados en la tabla users:")
        for usuario in usuarios:
            print(f"ID: {usuario.id}, Username: {usuario.username}")
        admin = db.query(User).filter(User.username == "dani").first()
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

print(os.getenv("DATABASE_URL")) 
"""Configuración de la base de datos."""

import os
import reflex as rx
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import dotenv

dotenv.load_dotenv()

# Configuración de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://neondb_owner:npg_2MGHEULOJt0g@ep-silent-cloud-ab3kdk6l-pooler.eu-west-2.aws.neon.tech/neondb?sslmode=require")
print("USANDO BASE DE DATOS:", DATABASE_URL)

# Crear el motor de la base de datos
engine = create_engine(
    DATABASE_URL,
    pool_size=5,         # Número máximo de conexiones en el pool
    max_overflow=2,      # Conexiones adicionales permitidas
    pool_timeout=30,     # Tiempo máximo de espera para obtener una conexión (segundos)
    pool_recycle=1800    # Reciclar conexiones cada 30 minutos
)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la base para los modelos
Base = declarative_base()

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 
"""Modelos de la base de datos."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from werkzeug.security import generate_password_hash, check_password_hash
from .database import Base

class User(Base):
    """Modelo para los usuarios."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def set_password(self, password: str):
        """Establece la contraseña del usuario."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Verifica la contraseña del usuario."""
        return check_password_hash(self.password_hash, password)

class Repository(Base):
    """Modelo para los repositorios."""
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)
    description = Column(Text)  # Nuevo campo para la descripción
    image_url = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class BlogPost(Base):
    """Modelo para las entradas de blog."""
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    image_url = Column(String(255))
    seo_description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
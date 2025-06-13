"""Configuration for the Reflex app."""

import reflex as rx

config = rx.Config(
    app_name="portafolio",
    db_url="postgresql://localhost:5432/portafolio",
    env=rx.Env.DEV,
    log_level="debug",
    frontend_port=3000,
    backend_port=8000,
    api_url="http://localhost:8000",
    deploy_url="http://localhost:3000",
    db_auto_migrate=False,  # Desactivamos la migración automática
    db_engine="postgresql"  # Forzamos el uso de PostgreSQL
)
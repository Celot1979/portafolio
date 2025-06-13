"""Configuration for the Reflex app."""

import reflex as rx

config = rx.Config(
    app_name="portafolio",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    log_level="debug",
    frontend_port=3000,
    backend_port=8000,
    api_url="http://localhost:8000",
    deploy_url="http://localhost:3000",
)
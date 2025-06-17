"""Página de login."""

import reflex as rx
from ..state.login_state import LoginState

def login_page() -> rx.Component:
    """Renderiza la página de login."""
    return rx.vstack(
        rx.heading("Iniciar Sesión", size="2xl", color="white", font_family="sans-serif", margin_bottom="2em"),
        rx.vstack(
            rx.input(
                placeholder="Usuario",
                value=LoginState.username,
                on_change=LoginState.set_username,
                color="white",
                background_color="#2a2a2a",
                border="1px solid #444",
                border_radius="0.5em",
                padding="0.5em",
                width="100%",
            ),
            rx.input(
                placeholder="Contraseña",
                type="password",
                value=LoginState.password,
                on_change=LoginState.set_password,
                color="white",
                background_color="#2a2a2a",
                border="1px solid #444",
                border_radius="0.5em",
                padding="0.5em",
                width="100%",
            ),
            rx.button(
                "Iniciar Sesión",
                on_click=LoginState.handle_login,
                background_color="#444",
                color="white",
                _hover={"background_color": "#555"},
                width="100%",
            ),
            rx.text(
                LoginState.error_message,
                color="red",
                font_family="sans-serif",
            ),
            spacing="1em",
            width="100%",
            max_width="400px",
            padding="2em",
            background_color="#2d2d2d",
            border_radius="lg",
        ),
        width="100%",
        min_height="100vh",
        background_color="#1a1a1a",
        padding="2em",
        align_items="center",
        justify_content="center",
    )
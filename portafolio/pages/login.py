"""Página de login."""

import reflex as rx
from ..state.login_state import LoginState
from portafolio.components.menu import menu

def login_page() -> rx.Component:
    """Renderiza la página de login."""
    return rx.vstack(
        menu(),
        rx.center(
            rx.vstack(
                rx.heading("Iniciar Sesión", size="6", color="white", font_family="sans-serif", margin_bottom=["1em", "2em"]),
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
                    spacing="1",
                    width="100%",
                    max_width=["100%", "350px", "400px"],
                    padding=["1em", "2em"],
                    background_color="#2d2d2d",
                    border_radius="lg",
                ),
                width="100%",
                align_items="center",
                justify_content="center",
            ),
            width="100%",
            min_height="calc(100vh - 64px)",
            align_items="center",
            justify_content="center",
        ),
        width="100%",
        min_height="100vh",
        background_color="#1a1a1a",
        padding=["1em", "2em"],
    )
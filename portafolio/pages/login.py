"""Página de login."""

import reflex as rx
from portafolio.components.menu import menu
from portafolio.state.login_state import LoginState


def login_page() -> rx.Component:
    """Renderiza la página de login."""
    return rx.vstack(
        menu(),
        rx.heading("Login", size="2xl", color="white", margin_bottom="1em"),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Usuario",
                    id="username",
                    type="text",
                    color="white",
                    background_color="#2a2a2a",
                    border="1px solid #444",
                    border_radius="0.5em",
                    padding="0.5em",
                    width="100%",
                    margin_bottom="1em"
                ),
                rx.input(
                    placeholder="Contraseña",
                    id="password",
                    type="password",
                    color="white",
                    background_color="#2a2a2a",
                    border="1px solid #444",
                    border_radius="0.5em",
                    padding="0.5em",
                    width="100%",
                    margin_bottom="1em"
                ),
                rx.button(
                    "Iniciar Sesión",
                    type="submit",
                    background_color="#444",
                    color="white",
                    _hover={"background_color": "#555"},
                    width="100%"
                ),
                spacing="1em",
                width="100%",
                max_width="400px"
            ),
            on_submit=LoginState.handle_submit
        ),
        width="100%",
        min_height="100vh",
        background_color="#0a0a0a",
        padding="2em"
    ) 
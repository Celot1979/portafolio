"""Página de login."""

import reflex as rx
from ..state.login_state import LoginState
from portafolio.components.menu import menu
from ..styles import colors, animations, heading_style, button_style

def login_page() -> rx.Component:
    """Renderiza la página de login."""
    return rx.vstack(
        menu(),
        rx.center(
            rx.vstack(
                rx.heading("Iniciar Sesión", size="6", **heading_style),
                rx.vstack(
                    rx.input(
                        placeholder="Usuario",
                        value=LoginState.username,
                        on_change=LoginState.set_username,
                        color=colors['text'],
                        background_color=colors['secondary_bg'],
                        border="1px solid #444",
                        border_radius="0.5em",
                        padding="0.5em",
                        width="100%",
                        _hover={"border_color": colors['accent'], "transition": "border-color 0.3s ease"}
                    ),
                    rx.input(
                        placeholder="Contraseña",
                        type="password",
                        value=LoginState.password,
                        on_change=LoginState.set_password,
                        color=colors['text'],
                        background_color=colors['secondary_bg'],
                        border="1px solid #444",
                        border_radius="0.5em",
                        padding="0.5em",
                        width="100%",
                        _hover={"border_color": colors['accent'], "transition": "border-color 0.3s ease"}
                    ),
                    rx.button(
                        "Iniciar Sesión",
                        on_click=LoginState.handle_login,
                        **button_style,
                        width="100%",
                    ),
                    rx.text(
                        LoginState.error_message,
                        color=colors['error'],
                    ),
                    spacing="1",
                    width="100%",
                    max_width=["100%", "350px", "400px"],
                    padding=["1em", "2em"],
                    background_color=colors['secondary_bg'],
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
        background_color=colors['background'],
        padding=["1em", "2em"],
        **animations['fade_in']
    )
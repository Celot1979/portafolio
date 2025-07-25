"""Página para añadir repositorio."""

import reflex as rx
from portafolio.components.menu import menu
from portafolio.state.add_repository_state import AddRepositoryState
from ..styles import colors, animations, heading_style, button_style

def add_repository_page() -> rx.Component:
    """Renderiza la página para añadir repositorio."""
    return rx.vstack(
        menu(),
        rx.heading("Añadir Repositorio", size="6", **heading_style),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="URL del repositorio",
                    id="repository_url",
                    type="text",
                    color=colors['text'],
                    background_color=colors['secondary_bg'],
                    border="1px solid #444",
                    border_radius="0.5em",
                    padding="0.5em",
                    width="100%",
                    margin_bottom="1em",
                    _hover={"border_color": colors['accent'], "transition": "border-color 0.3s ease"}
                ),
                rx.button(
                    "Añadir",
                    type="submit",
                    **button_style,
                    width="100%"
                ),
                spacing="1",
                width="100%",
                max_width="400px"
            ),
            on_submit=AddRepositoryState.handle_submit
        ),
        width="100%",
        min_height="100vh",
        background_color=colors['background'],
        padding="2em",
        **animations['fade_in']
    ) 
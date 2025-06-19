"""Página para añadir repositorio."""

import reflex as rx
from portafolio.components.menu import menu
from portafolio.state.add_repository_state import AddRepositoryState


def add_repository_page() -> rx.Component:
    """Renderiza la página para añadir repositorio."""
    return rx.vstack(
        menu(),
        rx.heading("Añadir Repositorio", size="6", color="white", margin_bottom="1em"),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="URL del repositorio",
                    id="repository_url",
                    type="text",
                    color="white",
                    background_color="#2a2a2a",
                    border="1px solid #444",
                    border_radius="0.5em",
                    padding="0.5em",
                    width="100%",
                    margin_bottom="1em"
                ),
                rx.button(
                    "Añadir",
                    type="submit",
                    background_color="#444",
                    color="white",
                    _hover={"background_color": "#555"},
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
        background_color="#0a0a0a",
        padding="2em"
    ) 
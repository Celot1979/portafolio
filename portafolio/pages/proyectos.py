"""Página de proyectos."""

import reflex as rx
from portafolio.components.menu import menu

def proyectos_page() -> rx.Component:
    """Renderiza la página de proyectos."""
    
    return rx.vstack(
        menu(),
        rx.heading("Proyectos", size="2xl", color="white", margin_bottom="1em"),
        rx.vstack(
            rx.vstack(
                rx.heading("Repo 1", size="lg", color="white"),
                rx.text("Descripción del repo 1", color="#ccc"),
                rx.link(
                    "Ver en GitHub",
                    href="https://github.com/usuario/repo1",
                    color="#444",
                    background_color="white",
                    padding="0.5em 1em",
                    border_radius="0.5em",
                    _hover={"background_color": "#eee"}
                ),
                padding="1em",
                border="1px solid #444",
                border_radius="0.5em",
                width="100%",
                margin_bottom="1em"
            ),
            rx.vstack(
                rx.heading("Repo 2", size="lg", color="white"),
                rx.text("Descripción del repo 2", color="#ccc"),
                rx.link(
                    "Ver en GitHub",
                    href="https://github.com/usuario/repo2",
                    color="#444",
                    background_color="white",
                    padding="0.5em 1em",
                    border_radius="0.5em",
                    _hover={"background_color": "#eee"}
                ),
                padding="1em",
                border="1px solid #444",
                border_radius="0.5em",
                width="100%",
                margin_bottom="1em"
            ),
            width="100%",
            max_width="800px"
        ),
        width="100%",
        min_height="100vh",
        background_color="#0a0a0a",
        padding="2em"
    )
"""Página del blog."""

import reflex as rx
from portafolio.components.menu import menu

def blog_page() -> rx.Component:
    """Renderiza la página del blog."""
    
    return rx.vstack(
        menu(),
        rx.heading("Blog", size="2xl", color="white", margin_bottom="1em"),
        rx.vstack(
            rx.vstack(
                rx.heading("Primera entrada", size="lg", color="white"),
                rx.text("Contenido de la primera entrada del blog...", color="#ccc"),
                rx.image(
                    src="https://via.placeholder.com/400x200",
                    alt="Imagen del blog",
                    width="100%",
                    height="200px",
                    margin_top="1em",
                    border_radius="0.5em"
                ),
                padding="1em",
                border="1px solid #444",
                border_radius="0.5em",
                width="100%",
                margin_bottom="1em"
            ),
            rx.vstack(
                rx.heading("Segunda entrada", size="lg", color="white"),
                rx.text("Contenido de la segunda entrada del blog...", color="#ccc"),
                rx.image(
                    src="https://via.placeholder.com/400x200",
                    alt="Imagen del blog",
                    width="100%",
                    height="200px",
                    margin_top="1em",
                    border_radius="0.5em"
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
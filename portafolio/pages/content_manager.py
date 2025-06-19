"""Gestor de contenido del portafolio."""

import reflex as rx
from portafolio.components.menu import menu

def content_manager_page() -> rx.Component:
    """Renderiza el gestor de contenido."""
    return rx.vstack(
        menu(),
        rx.center(
            rx.vstack(
                rx.heading("Gestor de Contenido", size="6", color="white", margin_bottom=["0.5em", "1em"]),
                rx.vstack(
                    rx.link(
                        rx.button("Crear Blog Post", color_scheme="blue"),
                        href="/content/new-blog",
                        width="100%"
                    ),
                    rx.link(
                        rx.button("Crear Repositorio", color_scheme="green"),
                        href="/content/new-repo",
                        width="100%"
                    ),
                    spacing="2",
                    width="100%",
                    max_width=["100%", "100%", "400px"],
                ),
                width="100%",
                max_width=["100%", "100%", "900px"],
                align="center",
                padding=["2em", "4em"],
                margin_x="auto",
                align_items="center",
                justify_content="center"
            ),
            width="100%",
            min_height="calc(100vh - 64px)",
            align_items="center",
            justify_content="center",
        ),
        width="100%",
        min_height="100vh",
        background_color="#1a1a1a",
    )
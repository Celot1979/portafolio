"""Página de blog."""

import reflex as rx
from portafolio.components.menu import menu

def blog_page() -> rx.Component:
    """Renderiza la página de blog."""
    
    return rx.vstack(
        menu(),
        rx.heading("Blog", size="2xl", color="white", font_family="sans-serif", margin_bottom="2em"),
        rx.vstack(
            rx.vstack(
                rx.heading("Primer Post", size="lg", color="white", font_family="sans-serif"),
                rx.text(
                    "Contenido del primer post del blog. Aquí se incluirá información sobre temas de desarrollo, experiencias y aprendizajes.",
                    color="gray",
                    font_size="1.2em",
                    margin_bottom="1em"
                ),
                rx.text(
                    "Fecha: 1 de Marzo, 2024",
                    color="#888",
                    font_size="0.9em"
                ),
                padding="2em",
                background_color="#2d2d2d",
                border_radius="lg",
                width="100%",
                margin_bottom="2em",
                _hover={"transform": "translateY(-5px)", "transition": "all 0.3s ease"}
            ),
            width="100%",
            max_width="800px",
            align_items="center"
        ),
        width="100%",
        min_height="100vh",
        background_color="#1a1a1a",
        padding="2em",
        spacing="2em"
    ) 
"""Página de contacto."""

import reflex as rx
from portafolio.components.menu import menu

def contacto_page() -> rx.Component:
    """Renderiza la página de contacto."""
    
    return rx.vstack(
        menu(),
        rx.heading("Contacto", size="2xl", color="white", font_family="sans-serif", margin_bottom="2em"),
        rx.vstack(
            rx.vstack(
                rx.heading("¿Tienes un proyecto en mente?", size="lg", color="white", font_family="sans-serif"),
                rx.text(
                    "Estoy siempre abierto a nuevas oportunidades y colaboraciones. Si tienes un proyecto en mente o quieres discutir posibilidades, no dudes en contactarme.",
                    color="gray",
                    font_size="1.2em",
                    margin_bottom="2em"
                ),
                rx.hstack(
                    rx.link(
                        "Enviar Email",
                        href="mailto:dgarciamartinez53@gmail.com",
                        color="#444",
                        background_color="white",
                        padding="0.5em 1em",
                        border_radius="0.5em",
                        _hover={"background_color": "#eee", "transform": "translateY(-2px)", "transition": "all 0.3s ease"}
                    ),
                    rx.link(
                        "LinkedIn",
                        href="https://linkedin.com/in/tu-perfil",
                        color="white",
                        background_color="#2d2d2d",
                        padding="0.5em 1em",
                        border_radius="0.5em",
                        _hover={"background_color": "#3d3d3d", "transform": "translateY(-2px)", "transition": "all 0.3s ease"}
                    ),
                    spacing="1em"
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
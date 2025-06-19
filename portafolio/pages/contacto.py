"""Página de contacto."""

import reflex as rx
from portafolio.components.menu import menu

def contacto_page() -> rx.Component:
    """Renderiza la página de contacto."""
    
    return rx.vstack(
        menu(),
        rx.center(
            rx.vstack(
                rx.heading("Contacto", size="6", color="white", font_family="sans-serif", margin_bottom=["1em", "2em"]),
                rx.vstack(
                    rx.heading("¿Tienes un proyecto en mente?", size="4", color="white", font_family="sans-serif"),
                    rx.text(
                        "Estoy siempre abierto a nuevas oportunidades y colaboraciones. Si tienes un proyecto en mente o quieres discutir posibilidades, no dudes en contactarme.",
                        color="gray",
                        font_size=["1em", "1.1em", "1.2em"],
                        margin_bottom=["1em", "2em"]
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
                            "Telegram",
                            href="https://t.me/Celot1979",
                            color="white",
                            background_color="#0088cc", # Color de Telegram
                            padding="0.5em 1em",
                            border_radius="0.5em",
                            _hover={"background_color": "#007bb5", "transform": "translateY(-2px)", "transition": "all 0.3s ease"}
                        ),
                        spacing="1"
                    ),
                    padding=["1em", "2em"],
                    background_color="#2d2d2d",
                    border_radius="lg",
                    width="100%",
                    margin_bottom=["1em", "2em"],
                    _hover={"transform": "translateY(-5px)", "transition": "all 0.3s ease"}
                ),
                width="100%",
                max_width=["100%", "100%", "800px"],
                align_items="center"
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
        spacing="2"
    ) 
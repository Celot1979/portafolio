"""Página de contacto."""

import reflex as rx
from portafolio.components.menu import menu
from ..styles import heading_style, colors, button_style, animations

def contacto_page() -> rx.Component:
    """Renderiza la página de contacto."""
    
    return rx.vstack(
        menu(),
        rx.center(
            rx.vstack(
                rx.heading("Contacto", size="6", **heading_style),
                rx.vstack(
                    rx.heading("¿Tienes un proyecto en mente?", size="4", **heading_style),
                    rx.text(
                        "Estoy siempre abierto a nuevas oportunidades y colaboraciones. Si tienes un proyecto en mente o quieres discutir posibilidades, no dudes en contactarme.",
                        color=colors['text'],
                        font_size=["1em", "1.1em", "1.2em"],
                        margin_bottom=["1em", "2em"]
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                "Enviar Email",
                                **button_style
                            ),
                            href="mailto:dgarciamartinez53@gmail.com",
                        ),
                        rx.link(
                            rx.button(
                                "Telegram",
                                **{k: v for k, v in button_style.items() if k not in ['background_color', '_hover']},
                                background_color="#0088cc", # Color de Telegram
                                _hover={"background_color": "#007bb5"}
                            ),
                            href="https://t.me/Celot1979",
                        ),
                        spacing="1"
                    ),
                    padding=["1em", "2em"],
                    background_color=colors['secondary_bg'],
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
        padding=["1em", "2em"],
        spacing="2",
        **animations['fade_in']
    ) 
"""Gestor de contenido del portafolio."""

import reflex as rx
from portafolio.components.menu import menu
from ..styles import heading_style, button_style, animations, colors

def content_manager_page() -> rx.Component:
    """Renderiza el gestor de contenido."""
    return rx.vstack(
        menu(),
        rx.center(
            rx.vstack(
                rx.heading("Gestor de Contenido", size="6", **heading_style),
                rx.vstack(
                    rx.link(
                        rx.button("Crear Blog Post", **button_style),
                        href="/content/new-blog",
                        width="100%"
                    ),
                    rx.link(
                        rx.button("Crear Repositorio", **{k: v for k, v in button_style.items() if k not in ['background_color', '_hover']},
                                background_color="#00A86B", # Color de Telegram
                                _hover={"background_color": "#007bb5"},
                                transition="all 0.3s ease"
                            ),
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
        background_color=colors['background'],
        **animations['fade_in']
    )
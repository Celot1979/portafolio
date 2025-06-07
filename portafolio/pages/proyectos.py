"""Página de proyectos."""

import reflex as rx
from portafolio.components.menu import menu

def proyectos_page() -> rx.Component:
    """Renderiza la página de proyectos."""
    
    return rx.vstack(
        menu(),
        rx.heading("Proyectos", size="2xl", color="white", font_family="sans-serif", margin_bottom="2em"),
        rx.vstack(
            rx.vstack(
                rx.heading("Portafolio Personal", size="lg", color="white", font_family="sans-serif"),
                rx.text(
                    "Desarrollo de un portafolio personal utilizando Reflex, un framework moderno para crear aplicaciones web en Python. El proyecto incluye diseño responsive, animaciones suaves y una interfaz de usuario intuitiva.",
                    color="gray",
                    font_size="1.2em",
                    margin_bottom="1em"
                ),
                rx.hstack(
                    rx.link(
                        "Ver en GitHub",
                        href="https://github.com/danielgil/portafolio",
                        color="#444",
                        background_color="white",
                        padding="0.5em 1em",
                        border_radius="0.5em",
                        _hover={"background_color": "#eee", "transform": "translateY(-2px)", "transition": "all 0.3s ease"}
                    ),
                    rx.link(
                        "Ver Demo",
                        href="/",
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
            rx.vstack(
                rx.heading("Proyecto 2", size="lg", color="white", font_family="sans-serif"),
                rx.text(
                    "Descripción detallada del segundo proyecto. Aquí se incluirá información sobre las tecnologías utilizadas, los desafíos enfrentados y las soluciones implementadas.",
                    color="gray",
                    font_size="1.2em",
                    margin_bottom="1em"
                ),
                rx.hstack(
                    rx.link(
                        "Ver en GitHub",
                        href="https://github.com/danielgil/proyecto2",
                        color="#444",
                        background_color="white",
                        padding="0.5em 1em",
                        border_radius="0.5em",
                        _hover={"background_color": "#eee", "transform": "translateY(-2px)", "transition": "all 0.3s ease"}
                    ),
                    rx.link(
                        "Ver Demo",
                        href="#",
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
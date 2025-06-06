"""Página del dashboard."""

import reflex as rx
from portafolio.components.menu import menu
from portafolio.state.dashboard_state import DashboardState


def dashboard_page() -> rx.Component:
    """Renderiza la página del dashboard."""
    return rx.vstack(
        menu(),
        rx.heading("Dashboard", size="2xl", color="white", margin_bottom="1em"),
        rx.vstack(
            rx.heading("Añadir Repositorio", size="lg", color="white", margin_bottom="1em"),
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
                    spacing="1em",
                    width="100%",
                    max_width="600px"
                ),
                on_submit=DashboardState.handle_add_repository
            ),
            rx.heading("Añadir Entrada de Blog", size="lg", color="white", margin_bottom="1em"),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Título",
                        id="title",
                        type="text",
                        color="white",
                        background_color="#2a2a2a",
                        border="1px solid #444",
                        border_radius="0.5em",
                        padding="0.5em",
                        width="100%",
                        margin_bottom="1em"
                    ),
                    rx.text_area(
                        placeholder="Contenido",
                        id="content",
                        color="white",
                        background_color="#2a2a2a",
                        border="1px solid #444",
                        border_radius="0.5em",
                        padding="0.5em",
                        width="100%",
                        margin_bottom="1em"
                    ),
                    rx.input(
                        placeholder="URL de la imagen",
                        id="image_url",
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
                        "Publicar",
                        type="submit",
                        background_color="#444",
                        color="white",
                        _hover={"background_color": "#555"},
                        width="100%"
                    ),
                    spacing="1em",
                    width="100%",
                    max_width="600px"
                ),
                on_submit=DashboardState.handle_add_blog_post
            ),
            spacing="2em",
            width="100%",
            max_width="800px"
        ),
        width="100%",
        min_height="100vh",
        background_color="#0a0a0a",
        padding="2em"
    ) 
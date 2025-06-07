"""Página del dashboard."""

import reflex as rx
from portafolio.components.menu import menu
from portafolio.state.dashboard_state import DashboardState


def dashboard_page() -> rx.Component:
    """Renderiza la página del dashboard."""
    return rx.vstack(
        menu(),
        rx.heading("Dashboard", size="2xl", color="white", font_family="sans-serif", margin_bottom="2em"),
        rx.hstack(
            # Sección de Repositorios (Izquierda)
            rx.vstack(
                rx.heading("Añadir Repositorio", size="lg", color="white", font_family="sans-serif", margin_bottom="1em", align_self="flex-start"),
                rx.form(
                    rx.vstack(
                        rx.vstack(
                            rx.text("Título del repositorio", color="white", font_family="sans-serif"),
                            rx.input(
                                id="repository_title",
                                type="text",
                                color="white",
                                background_color="#2d2d2d",
                                border="1px solid #444",
                                border_radius="0.5em",
                                padding="0.5em",
                                width="100%",
                                _hover={"border_color": "#666"},
                                _focus={"border_color": "#888", "box_shadow": "0 0 0 1px #888"}
                            ),
                            spacing="0.5em",
                            width="100%",
                            margin_bottom="1em"
                        ),
                        rx.vstack(
                            rx.text("URL del repositorio", color="white", font_family="sans-serif"),
                            rx.input(
                                id="repository_url",
                                type="text",
                                color="white",
                                background_color="#2d2d2d",
                                border="1px solid #444",
                                border_radius="0.5em",
                                padding="0.5em",
                                width="100%",
                                _hover={"border_color": "#666"},
                                _focus={"border_color": "#888", "box_shadow": "0 0 0 1px #888"}
                            ),
                            spacing="0.5em",
                            width="100%",
                            margin_bottom="1em"
                        ),
                        rx.vstack(
                            rx.text("URL de la imagen del repositorio", color="white", font_family="sans-serif"),
                            rx.input(
                                id="repository_image_url",
                                type="text",
                                color="white",
                                background_color="#2d2d2d",
                                border="1px solid #444",
                                border_radius="0.5em",
                                padding="0.5em",
                                width="100%",
                                _hover={"border_color": "#666"},
                                _focus={"border_color": "#888", "box_shadow": "0 0 0 1px #888"}
                            ),
                            spacing="0.5em",
                            width="100%",
                            margin_bottom="1em"
                        ),
                        rx.button(
                            "Añadir",
                            type="submit",
                            background_color="#2d2d2d",
                            color="white",
                            border="1px solid white",
                            _hover={"background_color": "#3d3d3d", "transform": "translateY(-2px)", "transition": "all 0.3s ease"},
                            width="100%",
                            padding="0.5em",
                            border_radius="0.5em"
                        ),
                        spacing="1em",
                        width="100%",
                        max_width="600px"
                    ),
                    on_submit=DashboardState.handle_add_repository
                ),
                padding="2em",
                background_color="#2d2d2d",
                border_radius="lg",
                width="100%",
                height="100%",
                _hover={"transform": "translateY(-5px)", "transition": "all 0.3s ease"}
            ),
            # Sección de Blog (Derecha)
            rx.vstack(
                rx.heading("Añadir Entrada de Blog", size="lg", color="white", font_family="sans-serif", margin_bottom="1em"),
                rx.form(
                    rx.vstack(
                        rx.vstack(
                            rx.text("Título", color="white", font_family="sans-serif"),
                            rx.input(
                                id="title",
                                type="text",
                                color="white",
                                background_color="#2d2d2d",
                                border="1px solid #444",
                                border_radius="0.5em",
                                padding="0.5em",
                                width="100%",
                                _hover={"border_color": "#666"},
                                _focus={"border_color": "#888", "box_shadow": "0 0 0 1px #888"}
                            ),
                            spacing="0.5em",
                            width="100%",
                            margin_bottom="1em"
                        ),
                        rx.vstack(
                            rx.text("Contenido", color="white", font_family="sans-serif"),
                            rx.text_area(
                                id="content",
                                color="white",
                                background_color="#2d2d2d",
                                border="1px solid #444",
                                border_radius="0.5em",
                                padding="0.5em",
                                width="100%",
                                min_height="200px",
                                _hover={"border_color": "#666"},
                                _focus={"border_color": "#888", "box_shadow": "0 0 0 1px #888"}
                            ),
                            spacing="0.5em",
                            width="100%",
                            margin_bottom="1em"
                        ),
                        rx.vstack(
                            rx.text("URL de la imagen", color="white", font_family="sans-serif"),
                            rx.input(
                                id="image_url",
                                type="text",
                                color="white",
                                background_color="#2d2d2d",
                                border="1px solid #444",
                                border_radius="0.5em",
                                padding="0.5em",
                                width="100%",
                                _hover={"border_color": "#666"},
                                _focus={"border_color": "#888", "box_shadow": "0 0 0 1px #888"}
                            ),
                            spacing="0.5em",
                            width="100%",
                            margin_bottom="1em"
                        ),
                        rx.button(
                            "Publicar",
                            type="submit",
                            background_color="#2d2d2d",
                            color="white",
                            border="1px solid white",
                            _hover={"background_color": "#3d3d3d", "transform": "translateY(-2px)", "transition": "all 0.3s ease"},
                            width="100%",
                            padding="0.5em",
                            border_radius="0.5em"
                        ),
                        spacing="1em",
                        width="100%",
                        max_width="600px"
                    ),
                    on_submit=DashboardState.handle_add_blog_post
                ),
                padding="2em",
                background_color="#2d2d2d",
                border_radius="lg",
                width="100%",
                height="100%",
                _hover={"transform": "translateY(-5px)", "transition": "all 0.3s ease"}
            ),
            spacing="4em",
            width="100%",
            max_width="1400px",
            align_items="stretch",
            flex_direction="row",
            padding="2em",
            display=["flex", "flex", "flex", "flex"],
            flex_wrap="wrap"
        ),
        width="100%",
        min_height="100vh",
        background_color="#1a1a1a",
        padding="2em",
        spacing="2em"
    ) 
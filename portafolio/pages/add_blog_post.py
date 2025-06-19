"""Página para añadir entrada de blog."""

import reflex as rx
from portafolio.components.menu import menu
from portafolio.state.add_blog_post_state import AddBlogPostState


def add_blog_post_page() -> rx.Component:
    """Renderiza la página para añadir entrada de blog."""
    return rx.vstack(
        menu(),
        rx.heading("Añadir Entrada de Blog", size="6", color="white", margin_bottom="1em"),
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
                spacing="1",
                width="100%",
                max_width="600px"
            ),
            on_submit=AddBlogPostState.handle_submit
        ),
        width="100%",
        min_height="100vh",
        background_color="#0a0a0a",
        padding="2em"
    ) 
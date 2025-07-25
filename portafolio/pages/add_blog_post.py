"""Página para añadir entrada de blog."""

import reflex as rx
from portafolio.components.menu import menu
from portafolio.state.add_blog_post_state import AddBlogPostState
from ..styles import colors, animations, heading_style, button_style

def add_blog_post_page() -> rx.Component:
    """Renderiza la página para añadir entrada de blog."""
    return rx.vstack(
        menu(),
        rx.heading("Añadir Entrada de Blog", size="6", **heading_style),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Título",
                    id="title",
                    type="text",
                    color=colors['text'],
                    background_color=colors['secondary_bg'],
                    border="1px solid #444",
                    border_radius="0.5em",
                    padding="0.5em",
                    width="100%",
                    margin_bottom="1em",
                    _hover={"border_color": colors['accent'], "transition": "border-color 0.3s ease"}
                ),
                rx.text_area(
                    placeholder="Contenido",
                    id="content",
                    color=colors['text'],
                    background_color=colors['secondary_bg'],
                    border="1px solid #444",
                    border_radius="0.5em",
                    padding="0.5em",
                    width="100%",
                    margin_bottom="1em",
                    _hover={"border_color": colors['accent'], "transition": "border-color 0.3s ease"}
                ),
                rx.input(
                    placeholder="URL de la imagen",
                    id="image_url",
                    type="text",
                    color=colors['text'],
                    background_color=colors['secondary_bg'],
                    border="1px solid #444",
                    border_radius="0.5em",
                    padding="0.5em",
                    width="100%",
                    margin_bottom="1em",
                    _hover={"border_color": colors['accent'], "transition": "border-color 0.3s ease"}
                ),
                rx.button(
                    "Publicar",
                    type="submit",
                    **button_style,
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
        background_color=colors['background'],
        padding="2em",
        **animations['fade_in']
    ) 
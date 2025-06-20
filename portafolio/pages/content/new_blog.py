"""Página para crear un nuevo post de blog."""

import reflex as rx
from ...components.menu import menu
from ...state.content_state import ContentState
from ...state.login_state import LoginState

def new_blog_page():
    """Página para crear un nuevo post de blog."""
    return rx.vstack(
        menu(),
        rx.hstack(
            rx.spacer(),
            rx.button(
                "Cerrar sesión",
                on_click=LoginState.logout,
                color_scheme="red",
                mr="2"
            ),
            rx.link(
                rx.button(
                    "Gestor de contenido",
                    color_scheme="blue"
                ),
                href="/content-manager"
            ),
            mt="2",
            width="100%"
        ),
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading("Nuevo Post de Blog", size="7", color="white", mb="1.5em", text_align="center"),
                    rx.form(
                        rx.vstack(
                            rx.input(
                                placeholder="Título",
                                id="title",
                                mb="4",
                                width="100%",
                                value=ContentState.blog_title,
                                on_change=ContentState.set_blog_title,
                                size="3"
                            ),
                            rx.input(
                                placeholder="URL de la imagen (opcional)",
                                id="image_url",
                                mb="4",
                                width="100%",
                                value=ContentState.blog_image_url,
                                on_change=ContentState.set_blog_image_url,
                                size="3"
                            ),
                            rx.text_area(
                                placeholder="Contenido",
                                id="content",
                                mb="4",
                                width="100%",
                                value=ContentState.blog_content,
                                on_change=ContentState.set_blog_content,
                                size="3"
                            ),
                            rx.button(
                                "Guardar entrada",
                                type_="submit",
                                color_scheme="blue",
                                size="3",
                                width="100%",
                                mt="2"
                            ),
                            align_items="center",
                            spacing="4",
                            width="100%"
                        ),
                        on_submit=ContentState.create_blog_post,
                        width="100%"
                    ),
                    rx.text(ContentState.blog_message, color="red", mt="2"),
                    spacing="4",
                    align_items="center",
                    width="100%"
                ),
                background="#18181b",
                border_radius="xl",
                box_shadow="0 8px 32px rgba(0,0,0,0.35)",
                p="8",
                max_width="600px",
                width="100%",
                mt="4"
            ),
            width="100%",
            min_height="calc(100vh - 64px)",
            align_items="center",
            justify_content="center"
        ),
        width="100%",
        min_height="100vh",
        background_color="#111"
    ) 
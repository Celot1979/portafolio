"""Página para crear un nuevo repositorio."""

import reflex as rx
from ...components.menu import menu
from ...state.content_state import ContentState
from ...state.login_state import LoginState

def new_repo_page():
    """Página para crear un nuevo repositorio."""
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
                    rx.heading("Nuevo Repositorio", size="7", color="white", mb="1.5em", text_align="center"),
                    rx.form(
                        rx.vstack(
                            rx.input(
                                placeholder="Título",
                                id="title",
                                mb="4",
                                width="100%",
                                value=ContentState.repo_title,
                                on_change=ContentState.set_repo_title,
                                size="3"
                            ),
                            rx.input(
                                placeholder="Descripción",
                                id="description",
                                mb="4",
                                width="100%",
                                value=ContentState.repo_description,
                                on_change=ContentState.set_repo_description,
                                size="3"
                            ),
                            rx.input(
                                placeholder="URL del repositorio",
                                id="url",
                                mb="4",
                                width="100%",
                                value=ContentState.repo_url,
                                on_change=ContentState.set_repo_url,
                                size="3"
                            ),
                            rx.input(
                                placeholder="URL de la imagen (opcional)",
                                id="image_url",
                                mb="4",
                                width="100%",
                                value=ContentState.repo_image_url,
                                on_change=ContentState.set_repo_image_url,
                                size="3"
                            ),
                            rx.button(
                                "Guardar repositorio",
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
                        on_submit=ContentState.create_repository,
                        width="100%"
                    ),
                    rx.text(ContentState.repo_message, color="red", mt="2"),
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
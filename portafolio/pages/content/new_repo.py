"""Página para crear un nuevo repositorio."""

import reflex as rx
from ...components.menu import menu
from ...state.content_state import ContentState
from ...state.login_state import LoginState

def new_repo_page():
    """Página para crear un nuevo repositorio."""
    return rx.vstack(
        menu(),
        rx.vstack(
            rx.heading("Nuevo Repositorio", size="4", mb="4"),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Título",
                        id="title",
                        mb="4",
                        width="100%",
                        value=ContentState.repo_title,
                        on_change=ContentState.set_repo_title,
                    ),
                    rx.input(
                        placeholder="Descripción",
                        id="description",
                        mb="4",
                        width="100%",
                        value=ContentState.repo_description,
                        on_change=ContentState.set_repo_description,
                    ),
                    rx.input(
                        placeholder="URL del repositorio",
                        id="url",
                        mb="4",
                        width="100%",
                        value=ContentState.repo_url,
                        on_change=ContentState.set_repo_url,
                    ),
                    rx.input(
                        placeholder="URL de la imagen (opcional)",
                        id="image_url",
                        mb="4",
                        width="100%",
                        value=ContentState.repo_image_url,
                        on_change=ContentState.set_repo_image_url,
                    ),
                    rx.text(
                        ContentState.repo_message,
                        color=rx.cond(
                            ContentState.repo_message.contains("correctamente"),
                            "green",
                            "red"
                        ),
                        mb="2"
                    ),
                    rx.hstack(
                        rx.cond(
                            ContentState.repo_edit_id.is_none(),
                            rx.button(
                                "Guardar",
                                on_click=ContentState.create_repository,
                                color_scheme="blue",
                            ),
                            rx.button(
                                "Guardar cambios",
                                on_click=ContentState.save_edit_repo,
                                color_scheme="yellow",
                            ),
                        ),
                        rx.link(
                            rx.button(
                                "Cancelar",
                                color_scheme="gray",
                            ),
                            href="/content-manager",
                        ),
                        width="100%",
                        justify="between",
                    ),
                    width="100%",
                    max_width="800px",
                    spacing="4",
                ),
            ),
            rx.heading("Repositorios actuales", size="3", mt="6", mb="2"),
            rx.foreach(
                ContentState.repositories,
                lambda repo: rx.box(
                    rx.heading(repo["title"], size="2", color="white"),
                    rx.text(repo["url"], color="white"),
                    rx.cond(
                        repo.get("image_url"),
                        rx.image(src=repo["image_url"], alt=repo["title"], width="200px", border_radius="md"),
                    ),
                    rx.hstack(
                        rx.button(
                            "Editar",
                            color_scheme="yellow",
                            on_click=lambda repo_id=repo["id"]: ContentState.start_edit_repo(repo_id),
                            mt="2"
                        ),
                        rx.button(
                            "Borrar",
                            color_scheme="red",
                            on_click=lambda repo_id=repo["id"]: ContentState.delete_repository(repo_id),
                            mt="2"
                        ),
                    ),
                    background_color="#222",
                    border_radius="md",
                    p="4",
                    mb="4",
                )
            ),
            width="100%",
            max_width="1200px",
            min_height="100vh",
            py="8",
            px="4",
            background_color="#1a1a1a",
            color="white",
        ),
    ) 
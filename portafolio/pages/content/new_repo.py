"""Página para crear un nuevo repositorio."""

import reflex as rx
from ...components.menu import menu
from ...state.content_state import ContentState
from ...state.login_state import LoginState

def new_repo_page():
    """Página para crear un nuevo repositorio."""
    # Estado local para la confirmación de borrado
    confirm_delete_id = rx.var(None)

    def render_repo(repo):
        return rx.vstack(
            rx.heading(
                repo.get("title", ""),
                as_="h3",
                font_size=["1.2em", "1.3em", "1.5em"],
                color="white",
                font_family="sans-serif",
                width="100%",
                word_wrap="break-word"
            ),
            rx.text(
                repo.get("url", ""),
                color="#00bfff",
                font_family="sans-serif",
                width="100%",
                word_wrap="break-word",
                font_size=["0.9em", "1em", "1em"]
            ),
            rx.cond(
                repo.get("image_url"),
                rx.image(
                    src=repo.get("image_url", ""),
                    alt=repo.get("title", ""),
                    width="100%",
                    height="auto",
                    border_radius="lg"
                )
            ),
            rx.cond(
                ContentState.repo_confirm_delete_id == repo["id"],
                rx.hstack(
                    rx.text("¿Seguro que quieres borrar este repositorio?", color="red"),
                    rx.button(
                        "Confirmar",
                        color_scheme="red",
                        on_click=lambda: ContentState.delete_and_reset_repository(repo["id"]),
                        size="2"
                    ),
                    rx.button(
                        "Cancelar",
                        color_scheme="gray",
                        on_click=ContentState.cancel_delete_repository,
                        size="2"
                    ),
                    spacing="2"
                ),
                rx.hstack(
                    rx.button(
                        "Borrar",
                        color_scheme="red",
                        on_click=lambda: ContentState.confirm_delete_repository(repo["id"]),
                        size="2"
                    ),
                    rx.button(
                        "Modificar",
                        color_scheme="yellow",
                        on_click=lambda: ContentState.start_edit_repo(repo["id"]),
                        size="2"
                    ),
                    spacing="2"
                )
            ),
            spacing="2",
            width="100%",
            padding_y=["2", "3"],
            padding_x=["2", "3"],
            background_color="#232526",
            border_radius="md",
            margin_bottom="1em"
        )

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
                                rx.cond(
                                    ContentState.repo_edit_id is not None,
                                    "Guardar cambios",
                                    "Guardar repositorio"
                                ),
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
                        on_submit=rx.cond(
                            ContentState.repo_edit_id is not None,
                            ContentState.save_edit_repo,
                            ContentState.create_repository
                        ),
                        width="100%"
                    ),
                    rx.text(ContentState.repo_message, color="green", mt="2"),
                    rx.divider(margin_y="2"),
                    rx.heading("Repositorios subidos", size="6", color="white", mb="1em", text_align="center"),
                    rx.cond(
                        ContentState.repositories,
                        rx.foreach(ContentState.repositories, render_repo),
                        rx.text("No hay repositorios guardados.", color="white")
                    ),
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
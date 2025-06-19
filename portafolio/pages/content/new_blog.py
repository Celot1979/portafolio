"""Página para crear un nuevo post de blog."""

import reflex as rx
from ...components.menu import menu
from ...state.content_state import ContentState
from ...state.login_state import LoginState

def new_blog_page():
    """Página para crear un nuevo post de blog."""
    return rx.vstack(
        menu(),
        rx.vstack(
            rx.heading("Nuevo Post de Blog", size="4", mb="4"),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Título",
                        id="title",
                        mb="4",
                        width="100%",
                        value=ContentState.blog_title,
                        on_change=ContentState.set_blog_title,
                    ),
                    rx.input(
                        placeholder="Contenido",
                        id="content",
                        mb="4",
                        width="100%",
                        value=ContentState.blog_content,
                        on_change=ContentState.set_blog_content,
                    ),
                    rx.input(
                        placeholder="URL de la imagen (opcional)",
                        id="image_url",
                        mb="4",
                        width="100%",
                        value=ContentState.blog_image_url,
                        on_change=ContentState.set_blog_image_url,
                    ),
                    rx.text(
                        ContentState.blog_message,
                        color=rx.cond(
                            ContentState.blog_message.contains("correctamente"),
                            "green",
                            "red"
                        ),
                        mb="2"
                    ),
                    rx.hstack(
                        rx.cond(
                            ContentState.blog_edit_id.is_none(),
                            rx.button(
                                "Guardar",
                                on_click=ContentState.create_blog_post,
                                color_scheme="blue",
                            ),
                            rx.button(
                                "Guardar cambios",
                                on_click=ContentState.save_edit_blog,
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
            rx.heading("Entradas actuales", size="3", mt="6", mb="2"),
            rx.foreach(
                ContentState.blog_posts,
                lambda post: rx.box(
                    rx.heading(post["title"], size="2", color="white"),
                    rx.text(post["content"], color="white"),
                    rx.cond(
                        post.get("image_url"),
                        rx.image(src=post["image_url"], alt=post["title"], width="200px", border_radius="md"),
                    ),
                    rx.hstack(
                        rx.button(
                            "Editar",
                            color_scheme="yellow",
                            on_click=lambda post_id=post["id"]: ContentState.start_edit_blog(post_id),
                            mt="2"
                        ),
                        rx.button(
                            "Borrar",
                            color_scheme="red",
                            on_click=lambda post_id=post["id"]: ContentState.delete_blog_post(post_id),
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
"""Página para gestionar el contenido del portafolio."""

import reflex as rx
from ..components.menu import menu
from ..state.content_state import ContentState
from ..state.login_state import LoginState

def content_manager_page():
    """Página para gestionar el contenido del portafolio."""
    return rx.vstack(
        menu(),
        rx.hstack(
            rx.spacer(),
            rx.button(
                "Cerrar sesión",
                on_click=LoginState.logout,
                color_scheme="red",
                _hover={"background_color": "#cc0000"},
            ),
            width="100%",
        ),
        rx.heading("Gestor de Contenido", size="lg", mb="4"),
        
        # Sección de Blog Posts
        rx.vstack(
            rx.heading("Blog Posts", size="md", mb="4"),
            rx.cond(
                ContentState.blog_posts.length() == 0,
                rx.text("No hay posts de blog disponibles."),
                rx.vstack(
                    rx.foreach(
                        ContentState.blog_posts,
                        lambda post: rx.box(
                            rx.hstack(
                                rx.cond(
                                    getattr(post, "image_url", None) is not None,
                                    rx.image(
                                        src=getattr(post, "image_url", ""),
                                        alt=getattr(post, "title", "Blog post"),
                                        width="100px",
                                        height="100px",
                                        object_fit="cover",
                                        border_radius="md",
                                    ),
                                    rx.box(width="100px", height="100px", bg="gray.200", border_radius="md")
                                ),
                                rx.vstack(
                                    rx.heading(getattr(post, "title", "Sin título"), size="sm"),
                                    rx.text(
                                        getattr(post, "content", "")[:100] + "..." if len(getattr(post, "content", "")) > 100 else getattr(post, "content", "")
                                    ),
                                    rx.hstack(
                                        rx.link("Ver", href=f"/blog/{getattr(post, 'id', '')}", color="blue.500"),
                                        rx.button(
                                            "Eliminar",
                                            color_scheme="red",
                                            size="sm",
                                            on_click=lambda: ContentState.delete_blog_post(getattr(post, "id", "")),
                                        ),
                                    ),
                                    align="start",
                                ),
                                width="100%",
                                p="4",
                                border_width="1",
                                border_radius="lg",
                                _hover={"shadow": "lg"},
                            ),
                            width="100%",
                        ),
                    ),
                    width="100%",
                    spacing="4",
                ),
            ),
            rx.button(
                "Nuevo Post",
                color_scheme="blue",
                on_click=lambda: rx.redirect("/content/new-blog"),
            ),
            width="100%",
            spacing="4",
            p="4",
            border_width="1",
            border_radius="lg",
        ),
        
        # Sección de Repositorios
        rx.vstack(
            rx.heading("Repositorios", size="md", mb="4"),
            rx.cond(
                ContentState.repositories.length() == 0,
                rx.text("No hay repositorios disponibles."),
                rx.vstack(
                    rx.foreach(
                        ContentState.repositories,
                        lambda repo: rx.box(
                            rx.hstack(
                                rx.cond(
                                    getattr(repo, "image_url", None) is not None,
                                    rx.image(
                                        src=getattr(repo, "image_url", ""),
                                        alt=getattr(repo, "title", "Repositorio"),
                                        width="100px",
                                        height="100px",
                                        object_fit="cover",
                                        border_radius="md",
                                    ),
                                    rx.box(width="100px", height="100px", bg="gray.200", border_radius="md")
                                ),
                                rx.vstack(
                                    rx.heading(getattr(repo, "title", "Sin título"), size="sm"),
                                    rx.text(getattr(repo, "description", "Sin descripción")),
                                    rx.hstack(
                                        rx.link("Ver", href=getattr(repo, "url", "#"), color="blue.500"),
                                        rx.button(
                                            "Eliminar",
                                            color_scheme="red",
                                            size="sm",
                                            on_click=lambda: ContentState.delete_repository(getattr(repo, "id", "")),
                                        ),
                                    ),
                                    align="start",
                                ),
                                width="100%",
                                p="4",
                                border_width="1",
                                border_radius="lg",
                                _hover={"shadow": "lg"},
                            ),
                            width="100%",
                        ),
                    ),
                    width="100%",
                    spacing="4",
                ),
            ),
            rx.button(
                "Nuevo Repositorio",
                color_scheme="blue",
                on_click=lambda: rx.redirect("/content/new-repo"),
            ),
            width="100%",
            spacing="4",
            p="4",
            border_width="1",
            border_radius="lg",
        ),
        
        width="100%",
        max_width="1200px",
        min_height="100vh",
        py="8",
        px="4",
        spacing="8",
        on_mount=ContentState.load_content,
    )
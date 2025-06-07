"""Página del dashboard."""

import reflex as rx
from portafolio.components.menu import menu
from portafolio.state.dashboard_state import DashboardState
from portafolio.models import Repository, BlogPost
from portafolio.database import get_db

def dashboard_page() -> rx.Component:
    """Renderiza la página del dashboard."""
    db = next(get_db())
    repositories = db.query(Repository).all()
    blog_posts = db.query(BlogPost).all()
    db.close()
    
    return rx.vstack(
        menu(),
        rx.heading("Dashboard", size="2xl", color="white", font_family="sans-serif", margin_bottom="2em"),
        rx.hstack(
            # Sección de Repositorios (Izquierda)
            rx.vstack(
                rx.heading("Añadir Repositorio", size="lg", color="white", font_family="sans-serif", margin_bottom="1em", align_self="flex-start"),
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
                            _focus={"border_color": "#888", "box_shadow": "0 0 0 1px #888"},
                            value=DashboardState.repository_title,
                            on_change=DashboardState.set_repository_title
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
                            _focus={"border_color": "#888", "box_shadow": "0 0 0 1px #888"},
                            value=DashboardState.repository_url,
                            on_change=DashboardState.set_repository_url
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
                            _focus={"border_color": "#888", "box_shadow": "0 0 0 1px #888"},
                            value=DashboardState.repository_image_url,
                            on_change=DashboardState.set_repository_image_url
                        ),
                        spacing="0.5em",
                        width="100%",
                        margin_bottom="1em"
                    ),
                    rx.button(
                        "Añadir",
                        on_click=DashboardState.handle_add_repository,
                        background_color="#2d2d2d",
                        color="white",
                        border="1px solid white",
                        _hover={"background_color": "#3d3d3d", "transform": "translateY(-2px)", "transition": "all 0.3s ease"},
                        width="100%",
                        padding="0.5em",
                        border_radius="0.5em"
                    ),
                    rx.text(
                        DashboardState.repository_message,
                        color="white",
                        font_family="sans-serif",
                        margin_top="1em"
                    ),
                    spacing="1em",
                    width="100%",
                    max_width="600px"
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
                            _focus={"border_color": "#888", "box_shadow": "0 0 0 1px #888"},
                            value=DashboardState.title,
                            on_change=DashboardState.set_title
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
                            _focus={"border_color": "#888", "box_shadow": "0 0 0 1px #888"},
                            value=DashboardState.content,
                            on_change=DashboardState.set_content
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
                            _focus={"border_color": "#888", "box_shadow": "0 0 0 1px #888"},
                            value=DashboardState.image_url,
                            on_change=DashboardState.set_image_url
                        ),
                        spacing="0.5em",
                        width="100%",
                        margin_bottom="1em"
                    ),
                    rx.button(
                        "Publicar",
                        on_click=DashboardState.handle_add_blog_post,
                        background_color="#2d2d2d",
                        color="white",
                        border="1px solid white",
                        _hover={"background_color": "#3d3d3d", "transform": "translateY(-2px)", "transition": "all 0.3s ease"},
                        width="100%",
                        padding="0.5em",
                        border_radius="0.5em"
                    ),
                    rx.text(
                        DashboardState.blog_message,
                        color="white",
                        font_family="sans-serif",
                        margin_top="1em"
                    ),
                    spacing="1em",
                    width="100%",
                    max_width="600px"
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
        # Sección de Repositorios Registrados
        rx.vstack(
            rx.heading("Repositorios Registrados", size="lg", color="white", font_family="sans-serif", margin_bottom="1em"),
            *[
                rx.hstack(
                    rx.vstack(
                        rx.heading(repo.title, size="md", color="white", font_family="sans-serif"),
                        rx.text(repo.url, color="white", font_family="sans-serif"),
                        rx.image(src=repo.image_url, alt=repo.title, width="100%", border_radius="lg"),
                        spacing="0.5em",
                        width="100%",
                        max_width="600px",
                        padding="1em",
                        background_color="#2d2d2d",
                        border_radius="lg",
                        _hover={"transform": "translateY(-5px)", "transition": "all 0.3s ease"}
                    ),
                    rx.button(
                        "Eliminar",
                        on_click=lambda repo_id=repo.id: DashboardState.delete_repository(repo_id),
                        background_color="#ff4444",
                        color="white",
                        border="1px solid white",
                        _hover={"background_color": "#cc0000", "transform": "translateY(-2px)", "transition": "all 0.3s ease"},
                        padding="0.5em",
                        border_radius="0.5em"
                    ),
                    spacing="1em",
                    width="100%",
                    max_width="800px",
                    align_items="center",
                    padding="1em",
                    background_color="#2d2d2d",
                    border_radius="lg",
                    _hover={"transform": "translateY(-5px)", "transition": "all 0.3s ease"}
                ) for repo in repositories
            ],
            spacing="1em",
            width="100%",
            max_width="1400px",
            align_items="center",
            padding="2em"
        ),
        # Sección de Entradas de Blog Registradas
        rx.vstack(
            rx.heading("Entradas de Blog Registradas", size="lg", color="white", font_family="sans-serif", margin_bottom="1em"),
            *[
                rx.hstack(
                    rx.vstack(
                        rx.heading(post.title, size="md", color="white", font_family="sans-serif"),
                        rx.text(post.content, color="white", font_family="sans-serif"),
                        rx.image(src=post.image_url, alt=post.title, width="100%", border_radius="lg"),
                        spacing="0.5em",
                        width="100%",
                        max_width="600px",
                        padding="1em",
                        background_color="#2d2d2d",
                        border_radius="lg",
                        _hover={"transform": "translateY(-5px)", "transition": "all 0.3s ease"}
                    ),
                    rx.button(
                        "Eliminar",
                        on_click=lambda post_id=post.id: DashboardState.delete_blog_post(post_id),
                        background_color="#ff4444",
                        color="white",
                        border="1px solid white",
                        _hover={"background_color": "#cc0000", "transform": "translateY(-2px)", "transition": "all 0.3s ease"},
                        padding="0.5em",
                        border_radius="0.5em"
                    ),
                    spacing="1em",
                    width="100%",
                    max_width="800px",
                    align_items="center",
                    padding="1em",
                    background_color="#2d2d2d",
                    border_radius="lg",
                    _hover={"transform": "translateY(-5px)", "transition": "all 0.3s ease"}
                ) for post in blog_posts
            ],
            spacing="1em",
            width="100%",
            max_width="1400px",
            align_items="center",
            padding="2em"
        ),
        width="100%",
        min_height="100vh",
        background_color="#1a1a1a",
        padding="2em",
        spacing="2em"
    ) 
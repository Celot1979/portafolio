"""Página de blog."""

import reflex as rx
from portafolio.components.menu import menu
from portafolio.state.content_state import ContentState
from portafolio.state.blog_page_state import BlogPageState
from portafolio.models import BlogPost
from portafolio.database import get_db

def generar_resumen(contenido, longitud=200):
    if not isinstance(contenido, str):
        return ""
    if len(contenido) > longitud:
        return contenido[:longitud] + "..."
    return contenido

def render_blog_card(post):
    title = post.get("title", "Sin título")
    content = post.get("content", "")
    image_url = post.get("image_url", None)
    post_id = post.get("id")
    card = rx.card(
        rx.vstack(
            rx.heading(
                title,
                as_="h3",
                font_size=["1.2em", "1.3em", "1.5em"],
                color="white",
                font_family="sans-serif",
                width="100%",
                word_wrap="break-word"
            ),
            rx.cond(
                image_url,
                rx.image(
                    src=image_url,
                    alt=title,
                    width="100%",
                    height="180px",
                    object_fit="cover",
                    border_radius="md",
                    margin_bottom="0.5em"
                )
            ),
            rx.text(
                generar_resumen(content),
                color="#e0e0e0",
                font_size="1em",
                margin_bottom="0.5em"
            ),
            rx.link(
                rx.button(
                    "Leer más",
                    color_scheme="blue",
                    variant="outline",
                    width="100%"
                ),
                href=f"/blog/{post_id}"
            ),
            spacing="2",
            align_items="flex-start",
            width="100%"
        ),
        background_color="#232526",
        border_radius="md",
        box_shadow="0 2px 8px rgba(0,0,0,0.15)",
        padding="1.5em",
        margin_bottom="1.5em",
        _hover={"box_shadow": "0 4px 16px #00e0ff44", "transform": "translateY(-4px)", "transition": "all 0.2s"},
    )
    return card

@rx.page(route="/blog", on_load=ContentState.load_content)
def blog_page() -> rx.Component:
    return rx.vstack(
        menu(),
        rx.center(
            rx.vstack(
                rx.heading("Blog", size="6", color="white", margin_bottom=["1em", "2em"]),
                rx.cond(
                    ContentState.blog_posts,
                    rx.grid(
                        rx.foreach(ContentState.blog_posts, render_blog_card),
                        columns={
                            "base": "1",
                            "sm": "2",
                            "md": "3"
                        },
                        spacing="4",
                        width="100%",
                        max_width=["100%", "100%", "1200px"],
                        margin_x="auto"
                    ),
                    rx.text("No hay entradas de blog.", color="white")
                ),
                width="100%",
                max_width=["100%", "100%", "1200px"],
                align_items="center",
                justify_content="center",
                spacing="2",
                padding=["1em", "2em"]
            ),
            width="100%",
            min_height="calc(100vh - 64px)",
            align_items="center",
            justify_content="center"
        ),
        width="100%",
        min_height="100vh",
        background_color="#1a1a1a"
    )

def render_full_post(post: dict):
    """Renderiza el contenido completo de un post."""
    return rx.box(
        rx.vstack(
            rx.heading(post["title"], as_="h1", color="white", font_size=["2em", "2.5em", "3em"], margin_bottom="0.5em"),
            rx.cond(
                post["image_url"],
                rx.image(
                    src=post["image_url"],
                    alt=post["title"],
                    width="100%",
                    max_height="350px",
                    object_fit="cover",
                    border_radius="md",
                    margin_bottom="1em"
                )
            ),
            rx.markdown(
                post["content"],
                color="white",
                font_size="1.1em",
                width="100%",
                margin_bottom="1em"
            ),
            rx.link(
                rx.button("Volver al blog", color_scheme="gray", variant="outline"),
                href="/blog"
            ),
            spacing="4",
            align_items="flex-start",
            width="100%"
        ),
        background="#232526",
        border_radius="xl",
        box_shadow="0 8px 32px rgba(0,0,0,0.35)",
        p="8",
        max_width="700px",
        width="100%",
        mt="4",
        margin_x="auto"
    )

@rx.page(route="/blog/[post_id]", on_load=ContentState.load_content)
def blog_detail_page():
    return rx.vstack(
        menu(),
        rx.center(
            rx.cond(
                ContentState.content_loaded,
                # Contenido cargado, ahora decide si mostrar post o error
                rx.cond(
                    ContentState.selected_post_from_list.length() > 0,
                    # Post encontrado
                    render_full_post(ContentState.selected_post_from_list[0]),
                    # Post no encontrado
                    rx.text("Entrada de blog no encontrada.", color="red", font_size="1.3em")
                ),
                # Contenido aún no cargado
                rx.text("Cargando...", color="white", font_size="1.3em")
            ),
            width="100%",
            min_height="calc(100vh - 64px)",
            align_items="center",
            justify_content="center"
        ),
        width="100%",
        min_height="100vh",
        background_color="#1a1a1a"
    )
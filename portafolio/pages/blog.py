import reflex as rx
from portafolio.components.menu import menu
from portafolio.state.content_state import ContentState
from portafolio.state.blog_page_state import BlogPageState
from portafolio.models import BlogPost
from portafolio.database import get_db
import os
from ..styles import heading_style, colors, link_style, button_style, animations

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
    
    return rx.link(
        rx.card(
            rx.vstack(
                rx.cond(
                    image_url,
                    rx.image(
                        src=image_url,
                        alt=title,
                        width="100%",
                        height="200px",
                        object_fit="cover",
                        border_top_left_radius="md",
                        border_top_right_radius="md",
                    ),
                ),
                rx.vstack(
                    rx.heading(
                        title,
                        as_="h3",
                        **heading_style,
                        font_size=["1.2em", "1.3em", "1.5em"],
                        width="100%",
                        word_wrap="break-word"
                    ),
                    rx.text(
                        generar_resumen(content),
                        color=colors['text'],
                        font_size="1em",
                        margin_bottom="1em"
                    ),
                    rx.button(
                        "Leer más",
                        **button_style,
                        width="100%"
                    ),
                    spacing="3",
                    align_items="flex-start",
                    width="100%",
                    padding="1.5em"
                ),
                spacing="0",
                width="100%"
            ),
            background_color=colors['secondary_bg'],
            border_radius="md",
            box_shadow="0 4px 6px rgba(0,0,0,0.1)",
            _hover={
                "box_shadow": f"0 8px 24px {colors['accent']}44", 
                "transform": "translateY(-5px)", 
                "transition": "all 0.3s ease"
            },
            width="100%"
        ),
        href=f"/blog/{post_id}",
        style={"text_decoration": "none"}
    )

@rx.page(route="/blog", on_load=ContentState.load_content)
def blog_page() -> rx.Component:
    return rx.vstack(
        menu(),
        rx.center(
            rx.vstack(
                rx.heading("Blog", size="6", **heading_style),
                rx.cond(
                    ~ContentState.content_loaded,
                    rx.box(),  # Placeholder para el indicador de carga
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
                    rx.text("No hay entradas de blog.", color=colors['text'])
                    )
                ),
                rx.cond(
                    ~ContentState.blog_no_more & ContentState.content_loaded,
                    rx.button(
                        "Cargar más entradas",
                        on_click=ContentState.load_more_blogs,
                        **button_style,
                        mt="2"
                    )
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
        on_mount=lambda: ContentState.load_content(page=1, per_page=ContentState.per_page, tipo="blog"),
        **animations['fade_in']
    )

def render_full_post(post: dict):
    """Renderiza el contenido completo de un post."""
    return rx.box(
        rx.vstack(
            rx.heading(post["title"], as_="h1", **heading_style, font_size=["2.5em", "3em", "3.5em"], text_align="center"),
            rx.text(
                f"Publicado el {post['created_at']}", 
                color=colors['text'], 
                font_size="0.9em", 
                margin_bottom="1.5em", 
                text_align="center"
            ),
            rx.cond(
                post["image_url"],
                rx.image(
                    src=post["image_url"],
                    alt=post["title"],
                    width="100%",
                    max_height="450px",
                    object_fit="cover",
                    border_radius="lg",
                    margin_bottom="2em",
                    box_shadow="0 8px 16px rgba(0,0,0,0.2)"
                )
            ),
            rx.markdown(
                post['content'],
                color=colors['text'],
                font_size="1.15em",
                line_height="1.8",
                width="100%",
                margin_bottom="2em"
            ),
            rx.link(
                rx.button(
                    "Volver al blog",
                    **button_style,
                    size="3"
                ),
                href="/blog",
                style={"text_decoration": "none"}
            ),
            spacing="4",
            align_items="center",
            width="100%"
        ),
        max_width="800px",
        width="100%",
        margin_x="auto",
        padding=["2em", "3em", "4em"],
        background_color=colors['background'],
    )

@rx.page(route="/blog/[post_id]", on_load=ContentState.load_single_blog_post)
def blog_detail_page():
    # Construye la URL base para og:url
    base_url = os.environ.get("BASE_URL", "https://portafolio-gold-apple.reflex.run")
    return rx.fragment(
        rx.vstack(
            menu(),
            rx.center(
                rx.cond(
                    ContentState.selected_blog_post,
                    render_full_post(ContentState.selected_blog_post),
                    rx.text("Cargando o entrada de blog no encontrada.", color=colors['text'], font_size="1.3em")
                ),
                width="100%",
                min_height="calc(100vh - 64px)",
                align_items="center",
                justify_content="center"
            ),
            width="100%",
            min_height="100vh",
            background_color=colors['background'],
            **animations['fade_in']
        )
    )
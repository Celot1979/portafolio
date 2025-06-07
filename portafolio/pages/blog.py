"""Página de blog."""

import reflex as rx
from portafolio.components.menu import menu
from portafolio.models import BlogPost
from portafolio.database import get_db

def blog_page() -> rx.Component:
    """Renderiza la página de blog."""
    db = next(get_db())
    blog_posts = db.query(BlogPost).all()
    db.close()
    
    return rx.vstack(
        menu(),
        rx.heading("Blog", size="2xl", color="white", font_family="sans-serif", margin_bottom="2em"),
        rx.vstack(
            *[
                rx.vstack(
                    rx.heading(post.title, size="lg", color="white", font_family="sans-serif"),
                    rx.text(post.content, color="white", font_family="sans-serif"),
                    rx.image(src=post.image_url, alt=post.title, width="100%", border_radius="lg"),
                    spacing="1em",
                    width="100%",
                    max_width="600px",
                    padding="2em",
                    background_color="#2d2d2d",
                    border_radius="lg",
                    _hover={"transform": "translateY(-5px)", "transition": "all 0.3s ease"}
                ) for post in blog_posts
            ],
            spacing="2em",
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
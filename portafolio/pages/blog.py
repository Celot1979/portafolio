"""Página de blog."""

import reflex as rx
from portafolio.components.menu import menu
from portafolio.state.blog_state import BlogState
from portafolio.state.event_state import EventState

def blog_page() -> rx.Component:
    """Renderiza la página de blog."""
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
                ) for post in BlogState.blog_posts
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
        spacing="2em",
        on_mount=BlogState.on_mount,
        on_unmount=BlogState.on_unmount,
        on_event=BlogState.handle_event
    ) 
"""Página de blog."""

import reflex as rx
from portafolio.components.menu import menu
from portafolio.state.content_state import ContentState

def render_post(post):
    return rx.vstack(
        rx.heading(
            post.get("title", ""),
            as_="h2",
            font_size=["1.5em", "1.75em", "2em"],
            color="white",
            font_family="sans-serif",
            width="100%",
            word_wrap="break-word"
        ),
        rx.markdown(
            post.get("content", ""),
            color="white",
            font_family="sans-serif",
            width="100%",
            font_size=["0.9em", "1em", "1em"]
        ),
        rx.cond(
            post.get("image_url"),
            rx.image(
                src=post.get("image_url", ""),
                alt=post.get("title", ""),
                width="100%",
                height="auto",
                border_radius="lg"
            )
        ),
        spacing="4",
        width="100%",
        padding_y=["4", "6"],
        padding_x=["4", "5"],
        background_color="#2d2d2d",
        border_radius="lg",
        _hover={"transform": "translateY(-5px)", "transition": "all 0.3s ease"}
    )

def blog_page() -> rx.Component:
    return rx.vstack(
        menu(),
        rx.center(
            rx.vstack(
                rx.heading("Blog", size="6", color="white", font_family="sans-serif", margin_bottom=["1em", "2em"]),
                rx.cond(
                    ContentState.blog_posts,
                    rx.foreach(ContentState.blog_posts, render_post),
                    rx.text("No hay posts guardados.", color="white")
                ),
                width="100%",
                max_width=["100%", "100%", "900px"],
                margin_x="auto",
                spacing="2",
                align_items="center",
                justify_content="center",
            ),
            width="100%",
            min_height="calc(100vh - 64px)",
            align_items="center",
            justify_content="center",
        ),
        width="100%",
        min_height="100vh",
        background_color="#1a1a1a",
        padding=["1em", "2em"],
        on_mount=ContentState.load_content
    )
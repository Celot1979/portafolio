"""Página de proyectos."""

import reflex as rx
from portafolio.components.menu import menu
from portafolio.state.content_state import ContentState

def proyectos_page() -> rx.Component:
    """Renderiza la página de proyectos."""
    return rx.vstack(
        menu(),
        rx.center(
            rx.vstack(
                rx.heading("Proyectos", size="6", color="white", font_family="sans-serif", margin_bottom=["1em", "2em"]),
                rx.cond(
                    ContentState.repositories,
                    rx.grid(
                        rx.foreach(
                            ContentState.repositories,
                            lambda repo: rx.box(
                                rx.heading(repo["title"], size="4", color="white"),
                                rx.text(repo["url"], color="gray"),
                                rx.cond(
                                    repo.get("image_url"),
                                    rx.image(src=repo["image_url"], alt=repo["title"], width="200px", border_radius="md"),
                                ),
                                background_color="#222",
                                border_radius="md",
                                p="4",
                                mb="8",
                            )
                        ),
                        columns="3",
                        spacing="8",
                        width="100%",
                        max_width=["100%", "100%", "1200px"],
                        margin_x="auto"
                    ),
                    rx.text("No hay proyectos guardados.", color="white")
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
            justify_content="center",
        ),
        width="100%",
        min_height="100vh",
        background_color="#1a1a1a",
        padding=["1em", "2em"],
        spacing="2",
        on_mount=ContentState.load_content
    )
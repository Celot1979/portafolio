"""Página de proyectos."""

import reflex as rx
from portafolio.components.menu import menu
from portafolio.state.content_state import ContentState
from ..styles import heading_style, colors, link_style, button_style, animations

def proyectos_page() -> rx.Component:
    """Renderiza la página de proyectos."""
    return rx.vstack(
        menu(),
        rx.center(
            rx.vstack(
                rx.heading("Proyectos", size="6", **heading_style),
                rx.cond(
                    ~ContentState.content_loaded,
                    rx.box(),  # Placeholder para el indicador de carga
                    rx.cond(
                    ContentState.repositories,
                    rx.grid(
                        rx.foreach(
                            ContentState.repositories,
                            lambda repo: rx.box(
                                rx.heading(repo["title"], size="4", **heading_style, word_wrap="break-word"),
                                    rx.text(repo.get("description", ""), color=colors['text'], font_size="1em", margin_bottom="0.5em"),
                                    rx.link(
                                        repo["url"],
                                        href=repo["url"],
                                        **link_style,
                                        is_external=True,
                                        word_break="break-all",
                                        margin_bottom="0.5em"
                                    ),
                                rx.cond(
                                    repo.get("image_url"),
                                    rx.image(src=repo["image_url"], alt=repo["title"], width="100%", height="auto", border_radius="md"),
                                ),
                                background_color=colors['secondary_bg'],
                                border_radius="md",
                                p="4",
                                _hover={
                                    "transform": "translateY(-5px)",
                                    "box_shadow": "0 8px 16px rgba(0,0,0,0.2)",
                                    "transition": "all 0.3s ease"
                                },
                                transition="all 0.3s ease"
                            )
                        ),
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
                    rx.text("No hay proyectos guardados.", color=colors['text'])
                    )
                ),
                rx.cond(
                    ~ContentState.repo_no_more & ContentState.content_loaded,
                    rx.button(
                        "Cargar más proyectos",
                        on_click=ContentState.load_more_repos,
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
            justify_content="center",
        ),
        width="100%",
        min_height="100vh",
        padding=["1em", "2em"],
        spacing="2",
        on_mount=lambda: ContentState.load_content(page=1, per_page=ContentState.per_page, tipo="repo"),
        **animations['fade_in']
    )
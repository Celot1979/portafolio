import reflex as rx
from ..styles import heading_style, colors, link_style

def menu():
    return rx.hstack(
        rx.heading(
            "PORTAFOLIO",
            size="5",
            **heading_style,
            _hover={"color": colors['accent']},
            transition="all 0.3s ease"
        ),
        rx.spacer(),
        rx.hstack(
            rx.link("Inicio", href="/", **link_style),
            rx.link("Quién soy", href="/quien-soy", **link_style),
            rx.link("Proyectos", href="/proyectos", **link_style),
            rx.link("Blog", href="/blog", **link_style),
            rx.link("Contacto", href="/contacto", **link_style),
            spacing="2",
            wrap="wrap",
        ),
        width="100vw",
        min_width="100%",
        max_width="100vw",
        padding=["0.5em 1em", "1em 2em"],
        background_color=colors['secondary_bg'],
        position="sticky",
        top="0",
        z_index="1000",
        align_items="center",
        justify_content="space-between",
        box_shadow="0 2px 8px rgba(0,0,0,0.05)",
        style={"left": 0, "right": 0},
    ) 
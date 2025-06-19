import reflex as rx

def menu():
    return rx.hstack(
        rx.heading(
            "PORTAFOLIO",
            size="5",
            color="white",
            font_family="'Montserrat', sans-serif",
            font_weight="700",
            letter_spacing="0.1em",
            _hover={"color": "#888"},
            transition="all 0.3s ease"
        ),
        rx.spacer(),
        rx.hstack(
            rx.link("Inicio", href="/", color="#ccc", _hover={"color": "white", "text_decoration": "underline"}, font_family="sans-serif"),
            rx.link("Quién soy", href="/quien-soy", color="#ccc", _hover={"color": "white", "text_decoration": "underline"}, font_family="sans-serif"),
            rx.link("Proyectos", href="/proyectos", color="#ccc", _hover={"color": "white", "text_decoration": "underline"}, font_family="sans-serif"),
            rx.link("Blog", href="/blog", color="#ccc", _hover={"color": "white", "text_decoration": "underline"}, font_family="sans-serif"),
            rx.link("Contacto", href="/contacto", color="#ccc", _hover={"color": "white", "text_decoration": "underline"}, font_family="sans-serif"),
            spacing="2",
            wrap="wrap",
        ),
        width="100vw",
        min_width="100%",
        max_width="100vw",
        padding=["0.5em 1em", "1em 2em"],
        background_color="#111",
        position="sticky",
        top="0",
        z_index="1000",
        align_items="center",
        justify_content="space-between",
        box_shadow="0 2px 8px rgba(0,0,0,0.05)",
        style={"left": 0, "right": 0},
    ) 
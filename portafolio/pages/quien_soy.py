import reflex as rx

class QuienSoyState(rx.State):
    pass

def quien_soy_page():
    return rx.vstack(
        # Barra superior con logo y menú
        rx.hstack(
            rx.heading(
                "PORTAFOLIO",
                size="xl",
                color="white",
                font_family="'Montserrat', sans-serif",
                font_weight="700",
                letter_spacing="0.1em",
                _hover={"color": "#888"},
                transition="all 0.3s ease"
            ),
            rx.spacer(),
            # Menú horizontal
            rx.hstack(
                rx.link("Inicio", href="/", color="#ccc", _hover={"color": "white", "text_decoration": "underline"}, font_family="sans-serif"),
                rx.link("Quién soy", href="/quien-soy", color="#ccc", _hover={"color": "white", "text_decoration": "underline"}, font_family="sans-serif"),
                rx.link("Proyectos", href="/proyectos", color="#ccc", _hover={"color": "white", "text_decoration": "underline"}, font_family="sans-serif"),
                rx.link("Blog", href="/blog", color="#ccc", _hover={"color": "white", "text_decoration": "underline"}, font_family="sans-serif"),
                rx.link("Contacto", href="/contacto", color="#ccc", _hover={"color": "white", "text_decoration": "underline"}, font_family="sans-serif"),
                spacing="2em",
            ),
            width="100%",
            padding="1em 2em",
            background_color="#111",
            position="sticky",
            top="0",
            z_index="1000"
        ),
        rx.heading("Quién soy", size="2xl", color="white", font_family="sans-serif"),
        rx.hstack(
            rx.image(
                src="https://i.ibb.co/q3MnTrT9/Portafolio-yo.jpg",
                alt="Imagen de Daniel",
                width="100%",
                max_width="400px",
                border_radius="8px",
                flex="1"
            ),
            rx.vstack(
                rx.text(
                    "Mi nombre es Daniel. A diferencia de la mayoría de los desarrolladores me he acercado con pasión a la tecnología en mi madurez. Un aspecto a valorar que me permite ofrecer la ilusión de quién inicia un nuevo camino profesional y la solvencia de la experiencia. Mi formación se ha realizado tanto en cursos guiados como autodidacta. Me ofrezco para participar en proyectos y desplegar todas mis habilidades.",
                    color="gray",
                    font_size="1.2em",
                    text_align="left"
                ),
                padding="2em",
                background_color="#2d2d2d",
                border_radius="lg",
                width="100%",
                align_items="flex-start",
                _hover={"transform": "translateY(-5px)", "transition": "all 0.3s ease"},
                flex="1"
            ),
            spacing="2em",
            width="100%",
            align_items="flex-start",
            flex_direction=["column", "column", "row"]
        ),
        spacing="2em",
        padding="2em",
        background_color="#1a1a1a",
        color="white",
        min_height="100vh",
        width="100%"
    ) 
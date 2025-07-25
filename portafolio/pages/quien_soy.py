import reflex as rx
from portafolio.components.menu import menu
from ..styles import heading_style, colors, animations

class QuienSoyState(rx.State):
    pass

def quien_soy_page():
    return rx.vstack(
        menu(),
        rx.center(
            rx.vstack(
                rx.heading("Quién soy", size="6", **heading_style),
                rx.hstack(
                    rx.image(
                        src="https://i.ibb.co/q3MnTrT9/Portafolio-yo.jpg",
                        alt="Imagen de Daniel",
                        width="100%",
                        max_width=["220px", "300px", "400px"],
                        border_radius="8px",
                        flex="1"
                    ),
                    rx.vstack(
                        rx.text(
                            "Mi nombre es Daniel. A diferencia de la mayoría de los desarrolladores me he acercado con pasión a la tecnología en mi madurez. Un aspecto a valorar que me permite ofrecer la ilusión de quién inicia un nuevo camino profesional y la solvencia de la experiencia. Mi formación se ha realizado tanto en cursos guiados como autodidacta. Me ofrezco para participar en proyectos y desplegar todas mis habilidades.",
                            color=colors['text'],
                            font_size=["1em", "1.1em", "1.2em"],
                            text_align="left"
                        ),
                        padding=["1em", "2em"],
                        background_color=colors['secondary_bg'],
                        border_radius="lg",
                        width="100%",
                        align_items="flex-start",
                        _hover={"transform": "translateY(-5px)", "transition": "all 0.3s ease"},
                        flex="1"
                    ),
                    spacing="2",
                    width="100%",
                    align_items="flex-start",
                    flex_direction=["column", "column", "row"]
                ),
                spacing="2",
                padding=["1em", "2em"],
                width="100%"
            ),
            width="100%",
            min_height="calc(100vh - 64px)",
            align_items="center",
            justify_content="center",
        ),
        width="100%",
        min_height="100vh",
        **animations['fade_in']
    )
import reflex as rx

class QuienSoyState(rx.State):
    pass

def quien_soy_page():
    return rx.vstack(
        rx.heading("Quién soy", size="2xl", color="white", font_family="sans-serif"),
        rx.text(
            "Mi nombre es Daniel. A diferencia de la mayoría de los desarrolladores me he acercado con pasión a la tecnología en mi madurez.",
            color="#ccc",
            margin_bottom="1em",
            font_family="sans-serif"
        ),
        rx.text(
            "Un aspecto a valorar que me permite ofrecer la ilusión de quién inicia un nuevo camino profesional y la solvencia de la experiencia.",
            color="#ccc",
            margin_bottom="1em",
            font_family="sans-serif"
        ),
        rx.text(
            "Mi formación se ha realizado tanto en  cursos guiados como autodidacta.",
            color="#ccc",
            margin_bottom="1em",
            font_family="sans-serif"
        ),
        rx.text(
            "Me ofrezco para participar en proyectos y desplegar todas mis  habilidades.",
            color="#ccc",
            font_family="sans-serif"
        ),
        rx.image(
            src="https://i.ibb.co/q3MnTrT9/Portafolio-yo.jpg",
            alt="Imagen de Daniel",
            width="100%",
            max_width="400px",
            margin_top="2em",
            border_radius="8px"
        ),
        spacing="2em",
        padding="2em",
        background_color="#1a1a1a",
        color="white",
        min_height="100vh",
        width="100%"
    ) 
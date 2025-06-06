"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from portafolio.pages.quien_soy import quien_soy_page
from portafolio.pages.contacto import contacto_page
from portafolio.pages.login import login_page
from portafolio.pages.dashboard import dashboard_page
from portafolio.pages.add_repository import add_repository_page
from portafolio.pages.add_blog_post import add_blog_post_page
from portafolio.pages.proyectos import proyectos_page
from portafolio.pages.blog import blog_page


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    """Renderiza la página principal."""
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
        # Contenido principal
        rx.vstack(
            rx.text(
                "My name is Daniel. A diferencia de la mayoría de los desarrolladores me he acercado con pasión a la tecnología en mi madurez.",
                color="#ccc",
                font_family="sans-serif"
            ),
            rx.text(
                "Un aspecto a valorar que me permite ofrecer la ilusión de quién inicia un nuevo camino profesional y la solvencia de la experiencia.",
                color="#ccc",
                font_family="sans-serif"
            ),
            rx.text(
                "Mi formación se ha realizado tanto en  cursos guiados como autodidacta.",
                color="#ccc",
                font_family="sans-serif"
            ),
            rx.text(
                "Me ofrezco para participar en proyectos y desplegar todas mis  habilidades.",
                color="#ccc",
                font_family="sans-serif"
            ),
            spacing="1em",
            align_items="start",
            width="100%",
            max_width="800px",
            padding="2em"
        ),
        # Pie de página con copyright
        rx.spacer(),
        rx.text("©2023 Daniel", color="#888", margin_bottom="1em", margin_right="1em", align_self="flex-end", font_family="sans-serif"),
        width="100%",
        min_height="100vh",
        background_color="#0a0a0a",
        color="white"
    )


# Define las rutas de la aplicación
app = rx.App()
app.add_page(index, route="/")
app.add_page(quien_soy_page, route="/quien-soy")
app.add_page(contacto_page, route="/contacto")
app.add_page(login_page, route="/login")
app.add_page(dashboard_page, route="/dashboard")
app.add_page(add_repository_page, route="/add-repository")
app.add_page(add_blog_post_page, route="/add-blog-post")
app.add_page(proyectos_page, route="/proyectos")
app.add_page(blog_page, route="/blog")

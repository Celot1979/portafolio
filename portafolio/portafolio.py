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
from portafolio.state.login_state import LoginState
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
                "Desarrollador Full Stack & Entusiasta de la Tecnología",
                font_size="1.2em",
                color="gray",
                margin_bottom="2em",
            ),
            rx.hstack(
                rx.vstack(
                    rx.icon("code", size=32, color="#4CAF50"),
                    rx.heading("Desarrollo", size="3"),
                    rx.text("Creando soluciones digitales innovadoras", color="gray"),
                    padding="2em",
                    background_color="#2d2d2d",
                    border_radius="lg",
                    width="250px",
                    align_items="center",
                    _hover={"transform": "translateY(-5px)", "transition": "all 0.3s ease"},
                ),
                rx.vstack(
                    rx.icon("database", size=32, color="#4CAF50"),
                    rx.heading("Backend", size="3"),
                    rx.text("Arquitectura robusta y escalable", color="gray"),
                    padding="2em",
                    background_color="#2d2d2d",
                    border_radius="lg",
                    width="250px",
                    align_items="center",
                    _hover={"transform": "translateY(-5px)", "transition": "all 0.3s ease"},
                ),
                rx.vstack(
                    rx.icon("palette", size=32, color="#4CAF50"),
                    rx.heading("Diseño", size="3"),
                    rx.text("Interfaces intuitivas y atractivas", color="gray"),
                    padding="2em",
                    background_color="#2d2d2d",
                    border_radius="lg",
                    width="250px",
                    align_items="center",
                    _hover={"transform": "translateY(-5px)", "transition": "all 0.3s ease"},
                ),
                spacing="2",
                margin_bottom="3em",
            ),
            rx.text(
                "Explora mis proyectos y descubre cómo puedo ayudarte a materializar tus ideas",
                color="gray",
                text_align="center",
                max_width="600px",
            ),
            rx.link(
                rx.button(
                    "Ver Proyectos",
                    color_scheme="green",
                    _hover={"background_color": "#45a049"},
                ),
                href="/proyectos",
                margin_top="2em",
            ),
            width="100%",
            align_items="center",
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
app.add_page(dashboard_page, route="/dashboard", on_load=LoginState.check_auth_and_redirect)
app.add_page(add_repository_page, route="/add-repository")
app.add_page(add_blog_post_page, route="/add-blog-post")
app.add_page(proyectos_page, route="/proyectos")
app.add_page(blog_page, route="/blog")

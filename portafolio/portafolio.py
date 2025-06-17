"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config

from portafolio.pages.quien_soy import quien_soy_page
from portafolio.pages.contacto import contacto_page
from portafolio.pages.login import login_page
from portafolio.pages.proyectos import proyectos_page
from portafolio.pages.blog import blog_page
from portafolio.pages.content_manager import content_manager_page
from portafolio.state.login_state import LoginState
from portafolio.components.menu import menu

def index() -> rx.Component:
    """Renderiza la página principal."""
    return rx.vstack(
        menu(),
        rx.vstack(
            rx.heading("Bienvenido a mi Portafolio", size="2xl", color="white", font_family="sans-serif", margin_bottom="1em"),
            rx.text(
                "Desarrollador Full Stack apasionado por crear soluciones innovadoras y experiencias de usuario excepcionales.",
                color="white",
                font_size="1.2em",
                margin_bottom="2em",
            ),
            rx.hstack(
                rx.link(
                    rx.button(
                        "Ver Proyectos",
                        size="lg",
                        color_scheme="blue",
                        _hover={"transform": "scale(1.05)"},
                    ),
                    href="/proyectos",
                ),
                rx.link(
                    rx.button(
                        "Leer Blog",
                        size="lg",
                        color_scheme="green",
                        _hover={"transform": "scale(1.05)"},
                    ),
                    href="/blog",
                ),
                rx.link(
                    rx.button(
                        "Contactar",
                        size="lg",
                        color_scheme="purple",
                        _hover={"transform": "scale(1.05)"},
                    ),
                    href="/contacto",
                ),
                spacing="2em",
                margin_top="2em",
            ),
            width="100%",
            max_width="1200px",
            align="center",
            padding="4em",
        ),
        width="100%",
        min_height="100vh",
        background_color="#1a1a1a",
        background_image="url('/background.jpg')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
    )

# Define las rutas de la aplicación
app = rx.App()
app.add_page(index, route="/")
app.add_page(quien_soy_page, route="/quien-soy")
app.add_page(contacto_page, route="/contacto")
app.add_page(login_page, route="/login")
app.add_page(content_manager_page, route="/content-manager", on_load=LoginState.check_auth_and_redirect)
app.add_page(proyectos_page, route="/proyectos")
app.add_page(blog_page, route="/blog") 
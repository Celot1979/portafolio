"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config

from portafolio.pages.quien_soy import quien_soy_page
from portafolio.pages.contacto import contacto_page
from portafolio.pages.login import login_page
from portafolio.pages.proyectos import proyectos_page
from portafolio.pages.blog import blog_page
from portafolio.pages.content_manager import content_manager_page
from portafolio.pages.content.new_blog import new_blog_page
from portafolio.pages.content.new_repo import new_repo_page
from portafolio.state.login_state import LoginState
from portafolio.components.menu import menu

def index() -> rx.Component:
    """Renderiza la página principal."""
    return rx.vstack(
        menu(),
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Bienvenido a mi Portafolio",
                        size="7",
                        color="cyan",
                        font_family="sans-serif",
                        margin_bottom="1em",
                        text_shadow="0 2px 8px rgba(0,0,0,0.25)"
                    ),
                    rx.text(
                        "Desarrollador Full Stack apasionado por crear soluciones innovadoras y experiencias de usuario excepcionales.",
                        color="white",
                        font_size="1.3em",
                        margin_bottom="2em",
                        text_align="center"
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                "Ver Proyectos",
                                size="4",
                                color_scheme="blue",
                                box_shadow="0 2px 8px rgba(0,0,0,0.15)",
                                _hover={"transform": "scale(1.07)", "box_shadow": "0 4px 16px rgba(0,0,0,0.25)"}
                            ),
                            href="/proyectos",
                        ),
                        rx.link(
                            rx.button(
                                "Leer Blog",
                                size="4",
                                color_scheme="green",
                                box_shadow="0 2px 8px rgba(0,0,0,0.15)",
                                _hover={"transform": "scale(1.07)", "box_shadow": "0 4px 16px rgba(0,0,0,0.25)"}
                            ),
                            href="/blog",
                        ),
                        rx.link(
                            rx.button(
                                "Contactar",
                                size="4",
                                color_scheme="purple",
                                box_shadow="0 2px 8px rgba(0,0,0,0.15)",
                                _hover={"transform": "scale(1.07)", "box_shadow": "0 4px 16px rgba(0,0,0,0.25)"}
                            ),
                            href="/contacto",
                        ),
                        spacing="4",
                        margin_top="2em",
                    ),
                    spacing="2",
                    align_items="center",
                    width="100%"
                ),
                background="linear-gradient(135deg, #232526 0%, #414345 100%)",
                border_radius="xl",
                box_shadow="0 8px 32px rgba(0,0,0,0.35)",
                p="8",
                max_width="600px",
                width="100%",
                transition="all 0.3s"
            ),
            width="100%",
            min_height="calc(100vh - 64px)",
            align_items="center",
            justify_content="center",
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
app.add_page(new_blog_page, route="/content/new-blog", on_load=LoginState.check_auth_and_redirect)
app.add_page(new_repo_page, route="/content/new-repo", on_load=LoginState.check_auth_and_redirect)
app.add_page(proyectos_page, route="/proyectos")
app.add_page(blog_page, route="/blog") 
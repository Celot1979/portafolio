""""""

""""""

import reflex as rx
from rxconfig import config

from portafolio.pages.quien_soy import quien_soy_page
from portafolio.pages.contacto import contacto_page
from portafolio.pages.login import login_page
from portafolio.pages.proyectos import proyectos_page
from portafolio.pages.blog import blog_page
from portafolio.pages.content_manager import content_manager_page
from portafolio.pages.add_blog_post import add_blog_post_page
from portafolio.pages.add_repository import add_repository_page
from portafolio.state.login_state import LoginState
from portafolio.components.menu import menu
from portafolio.pages.blog import blog_detail_page
from .styles import base_style, heading_style, button_style, colors, animations

# DATABASE_URL = "postgresql://postgres:Willtrabajo€_@db.fshpwnmynyucawuyiybb.supabase.co:5432/postgres"

def index() -> rx.Component:
    """Renderiza la página principal con un diseño visual moderno."""
    return rx.box(
        rx.toast.provider(),
        menu(),
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading(
                        "BIENVENIDO A MI PORTAFOLIO",
                        size="9",
                        **heading_style,
                        text_transform="uppercase",
                        text_align="center",
                        letter_spacing="0.05em",
                        z_index="1"
                    ),
                    rx.text(
                        "Desarrollador Full Stack apasionado por crear soluciones innovadoras.",
                        color=colors['text'],
                        font_size="1.3em",
                        text_align="center",
                        margin_bottom="1.5em",
                        z_index="1"
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                "Ver proyectos",
                                **button_style
                            ),
                            href="/proyectos"
                        ),
                        rx.link(
                            rx.button(
                                "Leer blog",
                                **button_style
                            ),
                            href="/blog"
                        ),
                        rx.link(
                            rx.button(
                                "Contactar",
                                **button_style
                            ),
                            href="/contacto"
                        ),
                        spacing="4",
                        z_index="1"
                    ),
                    spacing="4",
                    align_items="center",
                    width="100%",
                    z_index="1"
                ),
                position="relative",
                z_index="1",
                width="100%",
                max_width="700px",
                padding_y="6em"
            ),
            width="100%",
            min_height="calc(100vh - 64px)",
            align_items="center",
            justify_content="center",
            position="relative"
        ),
        width="100%",
        min_height="100vh",
        position="relative",
        overflow="hidden",
        background=f"linear-gradient(45deg, {colors['background']}, {colors['secondary_bg']}, {colors['background']})",
        **animations['gradient_background']
    )

# Define las rutas de la aplicación
app = rx.App(style=base_style)
app.add_page(index, route="/")
app.add_page(quien_soy_page, route="/quien-soy")
app.add_page(contacto_page, route="/contacto")
app.add_page(login_page, route="/login")
app.add_page(content_manager_page, route="/content-manager", on_load=LoginState.check_auth_and_redirect)
app.add_page(add_blog_post_page, route="/content/new-blog", on_load=LoginState.check_auth_and_redirect)
app.add_page(add_repository_page, route="/content/new-repo", on_load=LoginState.check_auth_and_redirect)
app.add_page(proyectos_page, route="/proyectos")
app.add_page(blog_page, route="/blog")
app.add_page(blog_detail_page, route="/blog/[post_id]")
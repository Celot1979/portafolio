""""""

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
from portafolio.pages.blog import blog_detail_page

# DATABASE_URL = "postgresql://postgres:Willtrabajo€_@db.fshpwnmynyucawuyiybb.supabase.co:5432/postgres"

def index() -> rx.Component:
    """Renderiza la página principal con un diseño visual moderno y shapes decorativos."""
    # SVG decorativo superior derecho (onda y blob, escala de grises, más grande)
    top_right_shape = rx.box(
        rx.html(
            '''
            <svg width="540" height="420" viewBox="0 0 540 420" fill="none" xmlns="http://www.w3.org/2000/svg" style="position:absolute;top:0;right:0;z-index:0;">
                <defs>
                    <radialGradient id="grad1" cx="50%" cy="50%" r="80%" fx="50%" fy="50%">
                        <stop offset="0%" style="stop-color:#cccccc;stop-opacity:0.4" />
                        <stop offset="100%" style="stop-color:#232526;stop-opacity:0" />
                    </radialGradient>
                </defs>
                <!-- Blob gris claro -->
                <path d="M500,60 Q540,200 400,320 Q480,160 500,60 Z" fill="#b0b0b0" fill-opacity="0.13"/>
                <!-- Onda gris medio -->
                <path d="M540,0 Q480,120 340,160 Q440,40 540,0 Z" fill="#888888" fill-opacity="0.15"/>
                <!-- Elipse difusa gris -->
                <ellipse cx="400" cy="140" rx="180" ry="100" fill="url(#grad1)" />
            </svg>
            '''
        ),
        position="absolute",
        top="0",
        right="0",
        z_index="0"
    )
    # SVG decorativo inferior izquierdo (onda y blob, escala de grises, más grande)
    bottom_left_shape = rx.box(
        rx.html(
            '''
            <svg width="480" height="360" viewBox="0 0 480 360" fill="none" xmlns="http://www.w3.org/2000/svg" style="position:absolute;bottom:0;left:0;z-index:0;">
                <defs>
                    <linearGradient id="grad2" x1="0" y1="0" x2="1" y2="1">
                        <stop offset="0%" stop-color="#cccccc" stop-opacity="0.3"/>
                        <stop offset="100%" stop-color="#232526" stop-opacity="0"/>
                    </linearGradient>
                </defs>
                <!-- Blob gris claro -->
                <path d="M0,360 Q120,260 360,320 Q200,340 0,360 Z" fill="#b0b0b0" fill-opacity="0.12"/>
                <!-- Onda gris medio -->
                <path d="M0,360 Q160,300 240,200 Q80,300 0,360 Z" fill="#888888" fill-opacity="0.13"/>
                <!-- Elipse difusa gris -->
                <ellipse cx="120" cy="300" rx="140" ry="80" fill="url(#grad2)" />
            </svg>
            '''
        ),
        position="absolute",
        bottom="0",
        left="0",
        z_index="0"
    )
    return rx.box(
        menu(),
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading(
                        "BIENVENIDO A MI PORTAFOLIO",
                        size="9",
                        color="white",
                        font_weight="bold",
                        text_transform="uppercase",
                        text_align="center",
                        letter_spacing="0.05em",
                        line_height="1.1",
                        margin_bottom="0.5em",
                        z_index="1"
                    ),
                    rx.text(
                        "Desarrollador Full Stack apasionado por crear soluciones innovadoras.",
                        color="#e0e0e0",
                        font_size="1.3em",
                        text_align="center",
                        margin_bottom="1.5em",
                        z_index="1"
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                "Ver proyectos",
                                variant="outline",
                                border="2px solid #fff",
                                color="#fff",
                                background="transparent",
                                border_radius="full",
                                px="6",
                                py="4",
                                font_size="1.1em",
                                font_weight="medium",
                                _hover={"background": "#232526", "color": "#00e0ff", "border": "2px solid #00e0ff"}
                            ),
                            href="/proyectos"
                        ),
                        rx.link(
                            rx.button(
                                "Leer blog",
                                variant="outline",
                                border="2px solid #fff",
                                color="#fff",
                                background="transparent",
                                border_radius="full",
                                px="6",
                                py="4",
                                font_size="1.1em",
                                font_weight="medium",
                                _hover={"background": "#232526", "color": "#00ffb8", "border": "2px solid #00ffb8"}
                            ),
                            href="/blog"
                        ),
                        rx.link(
                            rx.button(
                                "Contactar",
                                variant="outline",
                                border="2px solid #fff",
                                color="#fff",
                                background="transparent",
                                border_radius="full",
                                px="6",
                                py="4",
                                font_size="1.1em",
                                font_weight="medium",
                                _hover={"background": "#232526", "color": "#b388ff", "border": "2px solid #b388ff"}
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
        top_right_shape,
        bottom_left_shape,
        width="100%",
        min_height="100vh",
        background_color="#111",
        position="relative",
        overflow="hidden"
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
# Las páginas de blog ahora se registran automáticamente con @rx.page
# app.add_page(blog_page, route="/blog")
# app.add_page(blog_detail_page, route="/blog/[post_id]") 
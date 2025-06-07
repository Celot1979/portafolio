"""Página de login."""

import reflex as rx
from portafolio.components.menu import menu
from portafolio.state.login_state import LoginState


def login_page() -> rx.Component:
    """Renderiza la página de login."""
    return rx.vstack(
        # --- Menú Fijo en la Parte Superior ---
        menu(), 
        
        # --- Contenido Centrado del Formulario ---
        rx.center( 
            rx.vstack(
                rx.heading("Login", size="2xl", color="white", margin_bottom="1em"),
                rx.form(
                    rx.vstack(
                        # --- Campo de Usuario ---
                        rx.text("Usuario", color="white", font_size="1em", margin_bottom="0.2em", align_self="flex-start"),
                        rx.input(
                            id="username",
                            type="text",
                            color="white",
                            background_color="#2a2a2a",
                            border="1px solid #444",
                            border_radius="0.5em",
                            padding="0.5em",
                            width="100%",
                            margin_bottom="1em",
                            # ESTILO PARA EL AUTOCOMPLETADO (LLAVE BLANCA)
                            _autofill={
                                "color": "white",          # Color del texto autocompletado
                                "-webkit-text-fill-color": "white", # Asegura el color del texto
                                "box-shadow": "0 0 0px 1000px #2a2a2a inset", # Mantiene el fondo del input
                                "-webkit-box-shadow": "0 0 0px 1000px #2a2a2a inset" # Para compatibilidad WebKit
                            }
                        ),
                        # --- Campo de Contraseña ---
                        rx.text("Contraseña", color="white", font_size="1em", margin_bottom="0.2em", align_self="flex-start"),
                        rx.input(
                            id="password",
                            type="password",
                            color="white",
                            background_color="#2a2a2a",
                            border="1px solid #444",
                            border_radius="0.5em",
                            padding="0.5em",
                            width="100%",
                            margin_bottom="1em",
                            # ESTILO PARA EL AUTOCOMPLETADO (LLAVE BLANCA)
                            _autofill={
                                "color": "white",
                                "-webkit-text-fill-color": "white",
                                "box-shadow": "0 0 0px 1000px #2a2a2a inset",
                                "-webkit-box-shadow": "0 0 0px 1000px #2a2a2a inset"
                            }
                        ),
                        rx.button(
                            "Iniciar Sesión",
                            type="submit",
                            background_color="#444",
                            color="white",
                            _hover={"background_color": "#555"},
                            width="100%"
                        ),
                        spacing="1em",
                        width="100%",
                        max_width="400px",
                        align_items="center"
                    ),
                    on_submit=LoginState.handle_submit,
                    width="100%",
                    max_width="400px"
                ),
                width="100%", 
                padding="2em", 
                align_items="center"
            ),
            width="100%", 
            flex_grow=1 
        ),
        width="100%",
        min_height="100vh", 
        background_color="#0a0a0a",
    )
import reflex as rx

class ContactoState(rx.State):
    pass

def contacto_page():
    return rx.vstack(
        rx.heading("Contacto", size="2xl", color="white", font_family="sans-serif"),
        rx.link(
            rx.text("Enviar un email", font_size="1.2em", color="#ccc", _hover={"color": "white", "text_decoration": "underline"}, font_family="sans-serif"),
            href="mailto:dgarciamartinez53@gmail.com",
            is_external=True,
            margin_bottom="1em"
        ),
        rx.link(
            rx.text("Contactar por Telegram", font_size="1.2em", color="#ccc", _hover={"color": "white", "text_decoration": "underline"}, font_family="sans-serif"),
            href="https://t.me/celot1979",
            is_external=True,
        ),
        spacing="2em",
        padding="2em",
        background_color="#1a1a1a",
        color="white",
        min_height="100vh",
        width="100%"
    ) 
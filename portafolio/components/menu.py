import reflex as rx

def menu():
    return rx.hstack(
        rx.link(
            rx.text("Portafolio", font_size="1.5em", font_weight="bold", color="white"), # Color blanco para el título
            href="/" # Enlace a la página principal
        ),
        rx.spacer(), # Empuja los siguientes elementos a la derecha
        rx.hstack(
            # Enlaces a redes sociales con estilo sutil
            rx.link("Mail", href="mailto:dgarciamartinez53@gmail.com", is_external=True, color="#888", _hover={"color": "white"}, margin_left="1em", font_size="0.9em"), # Texto/Icono sutil
            rx.link("GitHub", href="#", is_external=True, color="#888", _hover={"color": "white"}, margin_left="1em", font_size="0.9em"), # Texto/Icono sutil (reemplazar # con tu URL)
            rx.link("LinkedIn", href="#", is_external=True, color="#888", _hover={"color": "white"}, margin_left="1em", font_size="0.9em"), # Texto/Icono sutil (reemplazar # con tu URL)
            # Menú de navegación principal (como en la imagen, con enlaces sencillos)
            # rx.link("Projects", href="/proyectos", margin_left="2em") # Podríamos añadir aquí un enlace a proyectos
            spacing="1em", # Espacio entre los enlaces de redes sociales
        ),
        padding="1em",
        # Considerar un color de fondo para la barra superior si es necesario
        # background_color="#f0f0f0",
        width="100%",
    ) 
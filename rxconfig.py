import reflex as rx

APP_MODULE = "portafolio.portafolio:app"

config = rx.Config(
    app_name="portafolio",
    plugins=[rx.plugins.TailwindV3Plugin()],
)
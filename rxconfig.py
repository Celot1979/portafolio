import reflex as rx

APP_MODULE = "portafolio.portafolio:app"

config = rx.Config(
    app_name="portafolio",
    api_url="https://celot1979.github.io/portafolio/",
    next_base_path="/portafolio",
    plugins=[rx.plugins.TailwindV3Plugin()],
)
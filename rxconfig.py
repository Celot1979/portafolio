import reflex as rx

APP_MODULE = "portafolio.portafolio:app"

config = rx.Config(
    app_name="portafolio",
    deploy_url="https://celot1979.github.io/portafolio/",
    plugins=[rx.plugins.TailwindV3Plugin()],
)
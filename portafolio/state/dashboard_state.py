"""Estado para el dashboard."""

import reflex as rx


class DashboardState(rx.State):
    """Estado para la página de dashboard."""

    @staticmethod
    def handle_add_repository(form_data=None):
        return rx.console_log("Repositorio añadido")

    @staticmethod
    def handle_add_blog_post(form_data=None):
        return rx.console_log("Entrada de blog añadida")

    pass  # Por ahora está vacío, pero podemos añadir más funcionalidad más tarde 
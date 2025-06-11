"""Estado para la página de login."""

import reflex as rx


class LoginState(rx.State):
    """Define el estado para la página de login."""
    username: str = ""
    password: str = ""
    error_message: str = ""
    is_authenticated: bool = False

    def handle_submit(self, form_data: dict):
        """Maneja el envío del formulario de login."""
        self.username = form_data.get("username", "")
        self.password = form_data.get("password", "")

        if self.username == "dani" and self.password == "Will€_": # Reemplaza con tu lógica de autenticación real
            self.is_authenticated = True
            return rx.redirect("/dashboard")
        else:
            self.is_authenticated = False
            self.error_message = "Usuario o contraseña incorrectos." 

    def check_auth_and_redirect(self):
        """Verifica si el usuario está autenticado y redirige al login si no lo está."""
        if not self.is_authenticated:
            return rx.redirect("/login")
        return None

    def logout(self):
        """Cierra la sesión del usuario."""
        self.is_authenticated = False
        return rx.redirect("/")
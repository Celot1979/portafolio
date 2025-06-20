"""Estado para la página de login."""

import reflex as rx
from ..models import User
from ..database import get_db


class LoginState(rx.State):
    """Define el estado para la página de login."""
    username: str = ""
    password: str = ""
    error_message: str = ""
    is_authenticated: bool = False

    def handle_login(self):
        """Maneja el inicio de sesión."""
        if not self.username or not self.password:
            self.error_message = "Por favor, completa todos los campos."
            return
        
        if self.username == "dani" and self.password == "Will2024_":
            self.is_authenticated = True
            self.error_message = ""
            return rx.redirect("/content-manager")
        else:
            self.error_message = "Usuario o contraseña incorrectos."

    def logout(self):
        """Cierra la sesión del usuario."""
        self.is_authenticated = False
        self.username = ""
        self.password = ""
        return rx.redirect("/login")

    def check_auth_and_redirect(self):
        """Verifica si el usuario está autenticado y redirige si no lo está."""
        if not self.is_authenticated:
            return rx.redirect("/login")
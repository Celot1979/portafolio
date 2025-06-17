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
            
        try:
            db = next(get_db())
            user = db.query(User).filter(User.username == self.username).first()
            
            if user and user.check_password(self.password):
                self.is_authenticated = True
                self.error_message = ""
                # Redirigir a content-manager en lugar de dashboard
                return rx.redirect("/content-manager")
            else:
                self.error_message = "Usuario o contraseña incorrectos."
                
        except Exception as e:
            self.error_message = f"Error al iniciar sesión: {str(e)}"
        finally:
            db.close()

    def logout(self):
        """Cierra la sesión del usuario."""
        self.is_authenticated = False
        self.username = ""
        self.password = ""
        return rx.redirect("/login")

    @staticmethod
    def check_auth_and_redirect():
        """Verifica si el usuario está autenticado y redirige si no lo está."""
        if not LoginState.is_authenticated:
            return rx.redirect("/login")
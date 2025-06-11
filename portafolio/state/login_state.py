"""Estado para la página de login

import reflex as rx


class LoginState(rx.State):
    #Define el estado para la página de login.
    username: str = ""
    password: str = ""
    error_message: str = ""

    def handle_submit(self, form_data: dict):
        #Maneja el envío del formulario de login.
        self.username = form_data.get("username", "")
        self.password = form_data.get("password", "")
        
        if self.username == "dani" and self.password == "Will€_":
            return rx.redirect("/dashboard")
        else:
            self.error_message = "Usuario o contraseña incorrectos."  ."""

#Estado para la página de login.

import reflex as rx


class LoginState(rx.State):
    #Define el estado para la página de login.
    username: str = ""
    password: str = ""
    error_message: str = ""
    is_authenticated: bool = False

    def handle_submit(self, form_data: dict):
        #Maneja el envío del formulario de login.
        self.username = form_data.get("username", "")
        self.password = form_data.get("password", "")

        if self.username == "dani" and self.password == "Will€_":
            is_authenticated = True
            return rx.redirect("/dashboard")
        else:
            self.error_message = "Usuario o contraseña incorrectos." 

"""Estado para añadir repositorios."""

import reflex as rx
from portafolio.models import Repository


class AddRepositoryState(rx.State):
    """Define el estado para añadir repositorios."""
    repository_url: str = ""
    error_message: str = ""

    def handle_submit(self, form_data: dict):
        """Maneja el envío del formulario para añadir un repositorio."""
        self.repository_url = form_data.get("repository_url", "")
        
        try:
            # Aquí iría la lógica para procesar la URL del repositorio
            # y extraer la información necesaria
            new_repository = Repository(
                name="Nuevo Repositorio",  # Esto debería venir de la API de GitHub
                link=self.repository_url,
                image_url="",  # Esto debería venir de la API de GitHub
                seo_description="",  # Esto debería generarse automáticamente
                seo_keywords=""  # Esto debería generarse automáticamente
            )
            
            with rx.session() as session:
                session.add(new_repository)
                session.commit()
                self.repository_url = ""
                return rx.redirect("/proyectos")
        except Exception as e:
            self.error_message = f"Error al añadir el repositorio: {str(e)}" 